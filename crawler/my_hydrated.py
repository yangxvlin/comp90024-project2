from twarc import Twarc
import json
from pathlib import Path
import os
import gzip
import time
from tqdm import tqdm
from multiprocessing import Process, SimpleQueue

from utils import load_configs

def hydrate(cfs):
    jobs = []
    squeue = SimpleQueue()
    data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04']
    
    # create folder here to avoid data racing
    if not os.path.isdir('hydrated'):
        os.makedirs('hydrated')

    for data_dir in data_dirs:
        full = os.path.join('hydrated', data_dir)
        print(full)
        if not os.path.isdir(full):
            os.makedirs(full)

    fc_process = Process(target=file_creator, args=(squeue, len(cfs),))
    jobs.append(fc_process)
    fc_process.daemon = True
    fc_process.start()

    for cf in cfs:
        # unpack keys
        account = cf['account']
        p = Process(target=hydrated_cycle, args=(account, squeue,))
        jobs.append(p)
        p.daemon = True
        p.start()
    
    [j.join() for j in jobs]


def file_creator(squeue, n_workers):
    data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04']

    for data_dir in data_dirs:

        for p in Path("COVID-19-TweetIDs/" + data_dir).iterdir():

            if p.name.endswith(".txt"):
                partial_path = os.path.join(data_dir, p.name)
                print("inserting:", partial_path)
                squeue.put(partial_path)
    
    # n work done indicator
    for _ in range(n_workers):
        squeue.put("done")


def hydrated_cycle(account, squeue):
    twarc = Twarc(**account)

    while True:
        working_path = squeue.get()

        if(working_path == "done"):
            print('job done')

        gzip_path = os.path.join(
            "hydrated/",
            working_path.split("/")[0],
            working_path.split("/")[-1][:-4]+".jsonl.gz")

        print(gzip_path)

        hydrate_file(working_path, twarc, gzip_path)


def hydrate_file(id_file, twarc, gzip_path):
    print("hydrating ", id_file)

    # getting use the cached work
    if os.path.isfile(gzip_path):
        print("skipping jsonl file already exists: ", gzip_path)
        return

    # # set prograss bar totoal ids
    # f = open(id_file, 'rb')
    # f_gen = _reader_generator(f.raw.read)
    # total_ids = sum(buf.count(b'\n') for buf in f_gen)

    with gzip.open(gzip_path, 'w') as output:
        for tweet in twarc.hydrate(open("COVID-19-TweetIDs/"+id_file)):
            # simply write to a gzip file and remove pbar
            
            if(tweet['place']):
                if(tweet['place']["country_code"].strip() == 'AU'):
                    print(tweet['place']["country_code"], gzip_path)
                    output.write(json.dumps(tweet).encode('utf-8') + b"\n")



def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


if __name__ == "__main__":
    cfs = load_configs()
    hydrate(cfs)

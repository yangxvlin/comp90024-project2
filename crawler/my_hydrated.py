from twarc import Twarc
import json
from pathlib import Path
import os
import gzip
import time
from tqdm import tqdm
from multiprocessing import Process

def hydrate(cfs):
    jobs = []
    for cf in cfs:
        # unpack keys
        account = cf['account']
        p = Process(target=hydrated_cycle, args=(account,))
        jobs.append(p)
        p.daemon = True
        p.start()
        time.sleep(1)
    
    [j.join() for j in jobs]

def hydrated_cycle(account):
    twarc = Twarc(**account)
    data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04']
    
    for data_dir in data_dirs:
        file_pointer = os.path.join(os.getcwd(), "hydrated/", data_dir+"/")

        if not (os.path.isdir(file_pointer)):
            os.makedirs(file_pointer)

        for p in Path("COVID-19-TweetIDs/" + data_dir).iterdir():
            if p.name.endswith(".txt"):
                hydrate_file(p, twarc, file_pointer)

                

def hydrate_file(id_file, twarc, target):
    print("hydrating ", id_file)

    gzip_path = os.path.join(target, id_file.name[:-4]+".jsonl.gz")

    print(gzip_path)
    
    if os.path.isfile(gzip_path):
        print("skipping jsonl file already exists: ", gzip_path)
        return

    # # set prograss bar totoal ids
    # f = open(id_file, 'rb')
    # f_gen = _reader_generator(f.raw.read)
    # total_ids = sum(buf.count(b'\n') for buf in f_gen)

    with gzip.open(gzip_path, 'w') as output:
        for tweet in twarc.hydrate(id_file.open()):
            # simply write to a gzip file and remove pbar
            if(tweet['place']):
                if(tweet['place']["country_code"].strip() == 'AU'):
                    output.write(json.dumps(tweet).encode('utf-8') + b"\n")



def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def load_configs():
    configs = [i for i in os.listdir("./") if 'config' in i]
    print(configs)
    res = []

    if len(configs) < 1:
        print("No config found")
        exit(1)

    for cf in configs:
        try:
            with open(cf, "r") as f:

                try:
                    config = json.load(f)
                except:
                    print('file', cf, 'not looks like a json file')
                    exit(1)

                if 'account' not in config:
                    print("account not found for file", cf)
                    exit(1)

                if 'search_words' not in config:
                    print("search word not found for file", cf)
                    exit(1)

                res.append(config)
        except IOError:
            print("please make sure you have config.json under the current path")
            exit(1)

    print("number of config found are", len(res))
    return res


if __name__ == "__main__":
    cfs = load_configs()
    hydrate(cfs)

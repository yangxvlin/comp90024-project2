from twarc import Twarc
import json
from pathlib import Path
import os
import gzip
from tqdm import tqdm
import time
from DB_Communicator import send_to_db
from workQueue import Workers, workerQueue

def hydrate(account):
    # unpack keys
    twarc = Twarc(**account)
    data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04']

    queue = workerQueue()
    workers = Workers(send_worker, ((queue),))
    workers.start()

    for data_dir in data_dirs:
        file_pointer = os.path.join(os.getcwd(), "hydrated/", data_dir+"/")

        if not (os.path.isdir(file_pointer)):
            os.makedirs(file_pointer)

        for p in Path("COVID-19-TweetIDs/" + data_dir).iterdir():
            if p.name.endswith(".txt"):
                hydrate_file(p, twarc, file_pointer, queue)
                queue.done()
                break
        
        # NOTE : testing
        break

    workers.join()


def hydrate_file(id_file, twarc, target, queue):
    print("hydrating ", id_file)

    gzip_path = os.path.join(target, id_file.name[:-4]+".jsonl.gz")

    print(gzip_path)
    
    if os.path.isfile(gzip_path):
        print("skipping jsonl file already exists: ", gzip_path)
        return

    # set prograss bar totoal ids
    f = open(id_file, 'rb')
    f_gen = _reader_generator(f.raw.read)
    total_ids = sum(buf.count(b'\n') for buf in f_gen)

    # the gzip file can work like a lockfile
    with gzip.open(gzip_path, 'w') as output:
        with tqdm(total=total_ids) as pbar:
            for tweet in twarc.hydrate(id_file.open()):
                writer(queue, tweet, mode='send')
                pbar.update(1)


def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def send_worker(queue):
    while True:
        msg = queue.get()
        print(os.getpid(),': get Msg')
        if msg == 'done':
            break
        
        # TODO : handle poential error here
        send_to_db(msg)


def writer(queue, tweet, mode='send', output_stream=None):
    if mode == 'send':
        queue.put(tweet)
    elif mode == 'save':
        if (output_stream == None):
            print("output_stream cannot be none")
            exit(1)
        output_stream.write(json.dumps(tweet).encode('utf-8') + b"\n")


if __name__ == "__main__":
    try:
        with open('config.json', "r") as f:
            config = json.load(f)

            if 'account' not in config:
                print("account not found")
                exit(1)

            if 'search_words' not in config:
                print("search word not found")
                exit(1)

            account = config['account']
            search_words = config['search_words']
    except IOError:
        print("please make sure you have config.json under the current path")
        exit(1)
    
    hydrate(account)

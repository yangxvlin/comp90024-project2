from multiprocessing import Process, Queue, Pool, cpu_count
import time
import sys


def reader_proc(queue):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        print("received", msg)
        time.sleep(1)
        if (msg == 'DONE'):
            break


def writer(count, queue):
    ## Write to the queue
    for ii in range(count):
        queue.put(ii)             # Write 'count' numbers into the queue
        print("writer send", ii)
    
    for i in range(cpu_count()-1):
        queue.put('DONE')


class workerQueue():
    
    def __init__(self):
        self.pqueue = Queue()
    
    def put(self, tweet):
        self.pqueue.put(tweet)
    
    def get(self):
        print("get one")
        return self.pqueue.get()
    
    def done(self, num=cpu_count()-1):
        for i in range(num):
            self.put('done')
    

class Workers():

    def __init__(self, job, args, num_of_core=cpu_count()-1):
        self.num_of_core = max(1, num_of_core)
        self.workers_list = []
        self.job = job
        self.args = args
        print("start job wiht" , num_of_core)
        self._create_workers()

    def _create_workers(self):
        for _ in range(self.num_of_core):
            self.workers_list.append( Process(target=self.job, args=(self.args)) )
            print('create one')
        
    
    def start(self):
        print("starting")
        for w in self.workers_list:
            w.daemon = True
            w.start()
    
    def join(self):
        print("joining")
        for w in self.workers_list:
            w.join()
    
            


if __name__ == '__main__':
    queue = workerQueue()
    print('creating workers')
    workers = []
    wk = Workers(reader_proc, ((queue),))

    wk.start()

    print("reached")
    _start = time.time()
    count = 100
    writer(count, queue)    # Send a lot of stuff to reader()

    wk.join()

    print("Sending {0} numbers to Queue() took {1} seconds".format(count,
                                                                    (time.time() - _start)))

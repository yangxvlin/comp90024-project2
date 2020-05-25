from utils import load_configs
from twarc import Twarc
import json
import os
import datetime
from multiprocessing import Process

from DB_Communicator import send_to_db

def stream_city(cf, city, keywords=None):
    bbox = {
        "great_syd": [149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993],
        "great_mel": [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995],
        "great_brisbane": [152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942],
        "great_ald": [138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998]
    }
    
    if keywords == None:
        keywords = cf["search_words"]
    
    t = Twarc(**cf['account'])

    # no keyword restriction but from a specific city
    # reason see this https://stackoverflow.com/questions/22889122/how-to-add-a-location-filter-to-tweepy-module
    if not os.path.isdir(city+"/"):
        os.makedirs(city)
    
    path = city + "/" + str(datetime.date.today())+".jsonl"

    locations = ",".join([str(i) for i in bbox[city]])

    for tweet in t.filter(locations=locations):
        print("get one tweet") #TODO
        send_to_db(tweet)


if __name__ == "__main__":
    cfs = load_configs()
    jobs = []
    
    for i in range(len(cfs)):
        boxes = ["great_syd", "great_mel", "great_brisbane", "great_ald"]
        p = Process(target=stream_city, args=((cfs[i], boxes[i],)), daemon=True)
        jobs.append(p)
        p.start()

    [p.join() for p in jobs]

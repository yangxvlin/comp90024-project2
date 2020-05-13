import couchdb
import json
import os

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import box

# with open("coronavirus-tweet-id-2020-03-01-00.jsonl") as f:
#     line = f.readline()
#     doc = json.loads(line)

# data = {'type': 'Person', 'name': 'John Doe'}
host = "115.146.95.30"
port = "5984"
username = password = "admin"
secure_remote_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
db = secure_remote_server.create('tweets')
#

bbox = {
    "great_syd": [149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993],
    "great_mel": [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995],
    "great_brisbane": [152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942],
    "great_ald": [138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998]
}

bbox_shapes = {}
for name, coor in bbox.items():
    bbox_shapes[name] = box(coor[0], coor[1], coor[2], coor[3])

def preprocess(bounding_box):
    # point = Point(0.5, 0.5)
    # polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    # print(polygon.contains(point))
    user_shape = Polygon(bounding_box)
    for name, area_shape in bbox_shapes.items():
        if area_shape.contains(user_shape.centroid):
            return name
    return "Australia other"

tweets = os.listdir("../tweets")
count = 0
for tweet in tweets:
    if count < 10:
        with open("../tweets/" + tweet) as f:
            for line in f:
                tweet_ = json.loads(line)
                tweet_["geo_code"] = preprocess(tweet_['place']["bounding_box"]["coordinates"][0])
                tweet_["_id"] = "%d" % tweet_["id"]
                # print(tweet_)
                db.save(tweet_)
                print(preprocess(tweet_['place']["bounding_box"]["coordinates"][0]))
        count += 1
    else:
        break

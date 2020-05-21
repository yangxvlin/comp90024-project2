import os

import couchdb
import json
from analysis import TwitterClassifier
from shapely.geometry import Polygon, box
from collections import defaultdict
import nltk

nltk.download('punkt')
# Environemt variable:
# - couchdb host ip
# - couchdb host port
# - couchdb username
# - couchdb password
# - the couchdb database name
# - the locatoin standards for mapping bounding box to location

bbox = {
    "great_syd": [149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993],
    "great_mel": [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995],
    "great_brisbane": [152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942],
    "great_ald": [138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998]
}


def connect_to_couch_db_server(host, port, username, password):
    secure_remote_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return secure_remote_server


def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)


## SETUP ######################################################
host = "115.146.95.30"
port = "5984"
username = password = "admin"
server = connect_to_couch_db_server(host, port, username, password)
database = connect_to_database("live-tweets", server)
with open("emotion_lexicon.json", 'r') as f:
    emotion_lexicon = json.load(f)
######################################################


bbox_shapes = {}
for name, coordinates in bbox.items():
    bbox_shapes[name] = box(coordinates[0], coordinates[1], coordinates[2], coordinates[3])


def preprocess(bounding_box):
    user_shape = Polygon(bounding_box)
    for name_, area_shape in bbox_shapes.items():
        if area_shape.contains(user_shape.centroid):
            return name_
    return "Australia other"


def emotion_count(tokens):
    emotion_counter = dict.fromkeys(emotion_lexicon.keys(), 0)
    for token in tokens:
        for emotion, lexicon in emotion_lexicon.items():
            if token in lexicon:
                # print(token, emotion)
                emotion_counter[emotion] += 1
    return emotion_counter


# Short: 1-4 characters
# Medium: 5-8 characters
# Long: 9+ characters
def word_length_distribution(tokens):
    short_thresh = 4
    long_thresh = 8
    word_length_keys = ['short_word_count', 'medium_word_count', 'long_word_count']

    word_length = dict.fromkeys(word_length_keys, 0)
    for token in tokens:
        if len(token) <= short_thresh:
            word_length['short_word_count'] += 1
        elif len(token) > 8:
            word_length['long_word_count'] += 1
        else:
            word_length['medium_word_count'] += 1
    return word_length


# data: the dictionary format of tweet object
def send_to_db(tweet_, db=database):
    # check for duplication first
    if str(tweet_["id"]) not in db:
        # set tweet id as the document id for duplication removal
        tweet_["_id"] = "%d" % tweet_["id"]

        tweet_["geo_code"] = preprocess(tweet_['place']["bounding_box"]["coordinates"][0])  # ADD

        # Rename the full_text fields to text if exits
        if "full_text" in tweet_:
            tweet_["text"] = tweet_["full_text"]
            del tweet_["full_text"]

        # get the full text if the tweets are truncated
        if tweet_["truncated"]:
            tweet_["text"] = tweet_["extended_tweet"]["full_text"]

        p = TwitterClassifier()
        res = p.analyse(tweet_)
        tweet_['polarity'] = res[0]
        tweet_['subjectivity'] = res[1]
        text = tweet_['text']
        sentences = nltk.sent_tokenize(text)
        tokens = []
        for sentence in sentences:
            tokens.extend(nltk.word_tokenize(sentence))
        tweet_.update(emotion_count(tokens))  # ADD EMOTION INFO
        tweet_.update(word_length_distribution(tokens))  # ADD LECXICON INFO
        print(tweet_)
        db.save(tweet_)
        print("saved")  # TODO


root_path = "~/COMP90024/comp90024-project2/crawler"
tweets_great_four = [os.listdir(root_path + "/great_ald"), os.listdir(root_path + "/great_mel"), os.listdir(root_path + "/great_brisbane"),
                     os.listdir(root_path + "/great_syd")]
tweets_great_four_dir = [root_path + "/great_ald", root_path + "/great_mel", root_path + "/great_brisbane", root_path + "/great_syd"]

for i, city_tweets in enumerate(tweets_great_four):
    for tweet in city_tweets:
        with open(tweets_great_four_dir[i] + tweet) as f:
            for line in f:
                tweet__ = json.loads(line)
                send_to_db(tweet__, database)  # GIVE THE TWEET OBJECT AND DATABASE OBJECT TO THIS FUgNCTION

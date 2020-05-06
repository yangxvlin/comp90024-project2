import couchdb
import json

# Environemt variable:
# - couchdb host ip
# - couchdb host port
# - couchdb username
# - couchdb password
# - the couchdb database name
# - the locatoin standards for mapping bounding box to location


def bounding_box_to_location(data, standards=None):
    # TODO: do nothing for now -> change later
    return data

def connect_to_coucbdb_servre(host, port, username, password):
    secure_remote_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return secure_remote_server

def create_databse(db_name, server):
    return server.create(dbname)

# data: the dictionary format of tweet object
def send_to_db(data):
    preprocessed_tweet = bounding_box_to_location(data)
    preprocessed_tweet["_id"] = "%d" % preprocessed_tweet["id"]
    db.save(preprocessed_tweet)

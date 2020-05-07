# -*- coding: utf-8 -*-
import requests
import json

# STATS = {
#     "_id": "_design/stat",
#     "views": {
#         "tweet-daily-time": {
#             "map": "function (doc) {\n  emit(doc.created_at.slice(0, doc.created_at.indexOf(' ')), 1);\n}",
#             "reduce": "_sum"
#         }
#     },
#     "language": "javascript"
# }


# date = {
#   "_id": "_design/loc",
#   "views": {
#     "new-view": {
#       "map": "function (doc) {\n  emit([doc.geo_code, doc.created_at.slice(0, doc.created_at.indexOf(' '))], 1);\n}",
#       "reduce": "_sum"
#     },
#     "date": {
#       "reduce": "_count",
#       "map": "function (doc) {\n  emit(doc.created_at.slice(0, doc.created_at.indexOf(' ')), 1);\n}"
#     }
#   },
#   "language": "javascript"
# }

STATISTICS = {
  "_id": "_design/STATISTICS",
  "language": "javascript",
  "views": {
    "city_hour_day": {
      "reduce": "_sum",
      "map": "function (doc) {\n  if (doc.place && doc.created_at) {\n    date = new Date(doc.created_at);\n    emit([doc.place.full_name, date.getHours(), date.getDay()], 1);\n  }\n}"
    }
  }
}

host = "115.146.93.205"
port = "5984"
username = password = "admin"
database = 'tweets'
design_doc = "STATISTICS"
update_design_doc_url = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}"

# Date: 0-6 represents Sunday to Saturday
req = requests.put(
  update_design_doc_url.format(username=username, password=password, host=host, port=port, database=database, design_doc=design_doc),
  headers={"Content-Type": "application/json"},
  data=json.dumps(STATISTICS)
)

# req = requests.put(
#     'http://' + username + ':' + password + '@' + host + ':' + port + '/' + database + '/_design/' + design_doc,
#     headers={"Content-Type": "application/json"},
#     data=json.dumps(STATS))

# print(requests.get(
#     'http://' + username + ':' + password + '@' + host + ':' + port + '/' + database + '/_design/' + design_doc + '/_view/' + "tweet-daily-time?group_level=1"
# ).content)

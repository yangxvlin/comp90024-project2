# -*- coding: utf-8 -*-
import requests
import json

STATISTICS = {
  "_id": "_design/STATISTICS",
  "language": "javascript",
  "views": {
    "city_hour_day": {
      "map": "function (doc) {\n  if (doc.geo_code && doc.created_at) {\n    city = doc.geo_code;\n    date = new Date(doc.created_at);\n    day = (date.getDay() + 6) % 7;\n    emit([city, date.getHours(), day], date);\n  }\n}",
      "reduce": "_count"
    },
    "city_2020_month_day_hours": {
      "map": "function (doc) {\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  // Hour is ranged from 0 to 23\n  hour = date.getHours();\n  \n  if (doc.geo_code && year == 2020) {\n    if (hour >= 0 && hour <= 7) {\n      emit([doc.geo_code, year, date.getMonth(), date.getDay(), \"00:00-07:59\"], 1);\n    } else if (hour >= 8 && hour <= 15) {\n      emit([doc.geo_code, year, date.getMonth(), date.getDay(), \"08:00-15:59\"], 1);\n    } else if (hour >= 16 && hour <= 23) {\n      emit([doc.geo_code, year, date.getMonth(), date.getDay(), \"16:00-23:59\"], 1);\n    }\n  }\n}",
      "reduce": "_count"
    }
  }
}

host = "115.146.93.205"
port = "5984"
username = password = "admin"
database = 'tweets'
design_doc = "STATISTICS"

update_design_doc_url = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}"
get_view_url = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}/_view/{view_name}?group_level={group_level}"

# Date: 0-6 represents Sunday to Saturday
req = requests.put(
  update_design_doc_url.format(username=username, password=password, host=host, port=port, database=database, design_doc=design_doc),
  headers={"Content-Type": "application/json"},
  data=json.dumps(STATISTICS)
)

def get_city_hour_day(group_level=3):
  """
  According to the group level provided by the user, return all the documents sorted in asending order from city, hour and day.
  """
  return json.loads(requests.get(
    get_view_url.format(username=username, password=password, host=host, port=port, database=database, design_doc=design_doc, view_name="city_hour_day", group_level=group_level)
  ).content.decode("utf-8"))

def get_city_2020_month_day_hours(group_level=5):
  """
  According to the group level provided by the user, return all the documents created in 2020
  sorted in asending order from city, month, day and hours.
  """
  return json.loads(requests.get(
    get_view_url.format(username=username, password=password, host=host, port=port, database=database, design_doc=design_doc, view_name="city_2020_month_day_hours", group_level=group_level)
  ).content.decode("utf-8"))

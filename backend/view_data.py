# -*- coding: utf-8 -*-
import requests
import json

STATISTICS = {
  "_id": "_design/STATISTICS",
  "language": "javascript",
  "views": {
    "city_hour_day": {
      "map": "geo_codes = {\n  \"great_syd\": \"Greater Sydney\",\n  \"great_mel\": \"Greater Melbourne\",\n  \"great_brisbane\": \"Greater Brisbane\",\n  \"great_ald\": \"Greater Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  day = (date.getDay() + 6) % 7;\n  hour = date.getHours();\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  } \n  emit([city, hour, day], date);\n}",
      "reduce": "_count"
    },
    "city_2020_month_day_hours": {
      "map": "geo_codes = {\n  \"great_syd\": \"Greater Sydney\",\n  \"great_mel\": \"Greater Melbourne\",\n  \"great_brisbane\": \"Greater Brisbane\",\n  \"great_ald\": \"Greater Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDay();\n  hour = date.getHours();\n  hours = \"other\"\n  \n  if (doc.place) {\n    city = geo_codes[doc.geo_code];\n  }\n  \n  if (year == 2020) {\n    if (hour >= 0 && hour <= 7) {\n      hours = \"00:00-07:59\";\n    } else if (hour >= 8 && hour <= 15) {\n      hours = \"08:00-15:59\";\n    } else if (hour >= 16 && hour <= 23) {\n      hours = \"16:00-23:59\";\n    }\n    emit([city, year, month, day, hours], 1);\n  }\n}",
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
  update_design_doc_url.format(username=username, 
                               password=password, 
                               host=host, port=port, 
                               database=database, 
                               design_doc=design_doc),
  headers={"Content-Type": "application/json"},
  data=json.dumps(STATISTICS)
)

def get_city_hour_day(group_level=3):
  """
  According to the group level provided by the user, return all the documents 
  sorted in asending order from city, hour and day.

  Parameters
  ----------
  group_level : int, optional
    The number of levels to reduce the documents to
  """
  return json.loads(requests.get(
    get_view_url.format(username=username, 
                        password=password, 
                        host=host, port=port, 
                        database=database, 
                        design_doc=design_doc, 
                        view_name="city_hour_day", 
                        group_level=group_level)
  ).content.decode("utf-8"))

def get_city_2020_month_day_hours(group_level=5):
  """
  According to the group level provided by the user, return all the documents 
  created in 2020 sorted in asending order from city, month, day and hours.

  Parameters
  ----------
  group_level : int, optional
    The number of levels to reduce the documents to
  """
  return json.loads(requests.get(
    get_view_url.format(username=username, 
                        password=password, 
                        host=host, port=port, 
                        database=database, 
                        design_doc=design_doc, 
                        view_name="city_2020_month_day_hours", 
                        group_level=group_level)
  ).content.decode("utf-8"))

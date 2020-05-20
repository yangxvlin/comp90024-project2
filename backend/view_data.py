# -*- coding: utf-8 -*-
import requests
import json

STATISTICS = {
  "_id": "_design/STATISTICS",
  "language": "javascript",
  "views": {
    "city_hour_day": {
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  day = (date.getDay() + 6) % 7;\n  hour = date.getHours();\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  } \n  emit([city, hour, day], 1);\n}",
      "reduce": "_count"
    },
    "city_2020_month_day_hours": {
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDay();\n  hour = date.getHours();\n  hours = \"other\"\n  \n  if (doc.place) {\n    city = geo_codes[doc.geo_code];\n  }\n  \n  if (year === 2020) {\n    if (hour >= 0 && hour <= 7) {\n      hours = \"00:00-07:59\";\n    } else if (hour >= 8 && hour <= 15) {\n      hours = \"08:00-15:59\";\n    } else if (hour >= 16 && hour <= 23) {\n      hours = \"16:00-23:59\";\n    }\n    emit([city, year, month, day, hours], 1);\n  }\n}",
      "reduce": "_count"
    },
    "city_year_month": {
      "reduce": "_count",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  } \n  emit([city, year, month], 1);\n}"
    },
    "English_city_year_month": {
      "reduce": "_count",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  if (doc.lang === \"en\") {\n    city = \"unknown\";\n    date = new Date(doc.created_at);\n    year = date.getFullYear();\n    month = date.getMonth();\n    if (doc.place) {\n      city = geo_codes[doc.geo_code]\n    } \n    emit([\"English\", city, year, month], 1);\n  }\n  \n}"
    },
    "emotion_city": {
      "reduce": "_sum",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nemotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', \n            'negative', 'positive', 'sadness', 'surprise', 'trust']\n\nfunction (doc) {\n  city = \"unknown\"\n  \n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  }\n  \n  for (e of emotions) {\n    emit([e, city], doc[e])\n  }\n}"
    },
    "covid_subjectivity_city_year_month_day": {
      "reduce": "_count",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDate();\n  subj = doc.subjectivity;\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  }\n  \n  if (subj >= 0 && subj <= 1/3) {\n    subj = \"objective\"\n  } \n  else if (subj > 1/3 && subj <= 2/3) {\n    subj = \"neutral\"\n  } else {\n    subj = \"subjective\"\n  }\n  emit([\"COVID-19\", subj, city, year, month, day], 1);\n  \n}"
    },
    "covid_polarity_city_year_month_day": {
      "reduce": "_count",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDate();\n  pol = doc.polarity;\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  }\n  emit([\"COVID-19\", pol, city, year, month, day], 1);\n  \n}"
    },
    "covid_city_year_month_day": {
      "reduce": "_count",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nfunction (doc) {\n  city = \"unknown\";\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDate();\n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  } \n  emit([\"COVID-19\", city, year, month, day], 1);\n}"
    },
    "emotion_city_year_month_day": {
      "reduce": "_sum",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nemotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', \n            'negative', 'positive', 'sadness', 'surprise', 'trust']\n\nfunction (doc) {\n  city = \"unknown\"\n  date = new Date(doc.created_at);\n  year = date.getFullYear();\n  month = date.getMonth();\n  day = date.getDate();\n  \n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  }\n  \n  for (e of emotions) {\n    emit([e, city, year, month, day], doc[e])\n  }\n}"
    },
    "wordlen_city": {
      "reduce": "_sum",
      "map": "geo_codes = {\n  \"great_syd\": \"Greater_Sydney\",\n  \"great_mel\": \"Greater_Melbourne\",\n  \"great_brisbane\": \"Greater_Brisbane\",\n  \"great_ald\": \"Greater_Sydney\",\n  \"Australia other\": \"other\"\n}\n\nwordlen_keys = [\"short_word_count\", \"medium_word_count\", \"long_word_count\"]\n\nfunction (doc) {\n  city = \"unknown\"\n  \n  if (doc.place) {\n    city = geo_codes[doc.geo_code]\n  }\n  \n  for (wordlen_key of wordlen_keys) {\n    emit([wordlen_key, city], doc[wordlen_key])\n  }\n}"
    }
  }
}

host = "115.146.93.205"
port = "5984"
username = password = "admin"
database = 'tweets3'
design_doc = "STATISTICS"

update_design_doc_url = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}"
get_view_url = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}/_view/{view_name}?group_level={group_level}"
get_tweets_url = "http://{username}:{password}@{host}:{port}/{database}/_find"

# Date: 0-6 represents Sunday to Saturday
# req = requests.put(
#   update_design_doc_url.format(username=username,
#                                password=password,
#                                host=host, port=port,
#                                database=database,
#                                design_doc=design_doc),
#   headers={"Content-Type": "application/json"},
#   data=json.dumps(STATISTICS)
# )


def get_view(view_name, group_level):
  """
  This function will retreived the aggregated documents from the database, and
  the aggregation level is determined by the group_level.

  Parameters
  ----------
  view_name: String
  The name of the view to be retrieved

  group_level : int
    The number of levels to reduce the documents to

  Sample return
  -------------
  {'rows': 
    [
      {'key': ['Greater_Brisbane', 2020, 2], 'value': 609}, 
      {'key': ['Greater_Melbourne', 2020, 2], 'value': 1420}, 
      {'key': ['Greater_Sydney', 2020, 2], 'value': 1613}, 
      {'key': ['other', 2020, 2], 'value': 1358}
    ]
  }
  """
  return json.loads(requests.get(
    get_view_url.format(username=username,
                        password=password, 
                        host=host, port=port, 
                        database=database, 
                        design_doc=design_doc, 
                        view_name=view_name, 
                        group_level=group_level)
  ).content.decode("utf-8"))

def get_sample_tweets(condition):
  """
  This function will retrieve tweets, based on the conditions given, form the
  database.

  Parameters
  ----------
  condition: Object
  The filtering condition for the tweets

  Sample return
  -------------
  [
    {doc 1},
    {doc 2},
    ........,
    {doc n}
  ]
  """
  return json.loads(requests.post(
    get_tweets_url.format(username=username,
                               password=password, 
                               host=host, port=port, 
                               database=database),
                    headers={"Content-Type": "application/json"},
                    data=json.dumps(condition)
  ).content.decode("utf-8"))["docs"]


def get_city_hour_day(group_level=3):
  return get_view("city_hour_day", group_level)


def get_city_2020_month_day_hours(group_level=5):
  return get_view("city_2020_month_day_hours", group_level)


def get_city_year_month(group_level=3):
  return get_view("city_year_month", group_level)


def get_English_city_year_month(group_level=4):
  return get_view("English_city_year_month", group_level)


def get_covid_city_year_month_day(group_level=5):
  return get_view("covid_city_year_month_day", group_level)


def get_covid_subjectivity_city_year_month_day(group_level=6):
  return get_view("covid_subjectivity_city_year_month_day", group_level)


def get_language(group_level=1):
  return get_view("language", group_level)


def get_English_tweets(num_of_tweets):
  condition = {
    "selector": {
        "lang": "en"
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_non_English_tweets(num_of_tweets):
  condition = {
    "selector": {
      "$and": [
        {
          "lang": {
            "$ne": "en"
          }
        },
        {
          "lang": {
            "$ne": "und"
          }
        }
      ]
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)

def get_pol_positive_tweets(num_of_tweets):
  condition = {
    "selector": {
      "polarity": {"$gte": 1/3}
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_pol_negative_tweets(num_of_tweets):
  condition = {
    "selector": {
      "polarity": {"$lte": -(1/3)}
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_pol_neutral_tweets(num_of_tweets):
  condition = {
    "selector": {
      "$and": [
        {
          "polarity": {"$gt": -(1/3)}
        },
        {
          "polarity": {"$lt": 1/3}
        }
      ]
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_sub_objective_tweets(num_of_tweets):
  condition = {
    "selector": {
      "subjectivity": {"$lte": 1/3}
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)



def get_sub_neutral_tweets(num_of_tweets):
  condition = {
    "selector": {
      "$and": [
        {
          "subjectivity": {"$gt": 1/3}
        },
        {
          "subjectivity": {"$lte": 2/3}
        }
      ]
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_sub_subjective_tweets(num_of_tweets):
  condition = {
    "selector": {
      "subjectivity": {"$gt": 2/3}
    },
    "limit": num_of_tweets
  }
  return get_sample_tweets(condition)


def get_emotion_city(group_level=2):
  return get_view("emotion_city", group_level)


def get_emotion_city_year_month_day(group_level=5):
  return get_view("emotion_city_year_month_day", group_level)


def get_wordlen_city(group_level=2):
  return get_view("wordlen_city", group_level)


def get_city_subjectivity(group_level=2):
  return get_view("city_subjectivity", group_level)


def get_city_polarity(group_level=2):
  return get_view("city_polarity", group_level)
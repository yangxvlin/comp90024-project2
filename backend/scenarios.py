"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-5-3 22:08:12
Description: api for scenarios
"""
import random
from math import log

from flask import request, jsonify, render_template
from flask_restful import Resource
from resources import api
from settings import SIMPLE_DB
from util import *
from flask_httpauth import HTTPBasicAuth
from view_data import *
import datetime
from graphGeneratorScenario2 import generate, transform

# ****************************************************************************
#                    Authentication starts
# ****************************************************************************

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    print(username, password)
    if username not in SIMPLE_DB or SIMPLE_DB[username] != password:
        return False
    return True


# ****************************************************************************
#                    scenario 1 twitter map starts
# ****************************************************************************


class TwitterMap(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/twittermap
        :return:
        """
        result = {"type": "FeatureCollection", "features": []}
        twitter_count_2020_by_lga_by_month_by_day_by_hour = get_city_2020_month_day_hours(5)
        for row in twitter_count_2020_by_lga_by_month_by_day_by_hour["rows"]:
            feature = {"type": "Feature", "geometry": {}, "properties": {}}
            row_key = row["key"]
            row_lga = row_key[0]

            # unknown location
            if row_lga not in CITY_GEO_POINTS:
                continue

            feature["geometry"] = CITY_GEO_POINTS[row_lga]

            row_year = row_key[1]
            row_month = row_key[2]
            row_day = row_key[3]
            row_time_period = row_key[4]
            row_time_start = row_time_period.split('-')[0]
            row_value = row["value"]

            create_at = "{}-{:02d}-{:02d}T{}:00+00:00Z".format(row_year, row_month, row_day, row_time_start)
            feature["properties"]["create_at"] = create_at
            feature["properties"]["city name"] = row_lga
            feature["properties"]["twitter count"] = row_value

            result["features"].append(feature)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(TwitterMap, "/twittermap", endpoint='twittermap')


# ****************************************************************************
#                    scenario 1 starts
# ****************************************************************************


class Scenario1(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario1?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&weekday=1,2,3&daytime_start=0&daytime_end=24&age_group=0,1,2,17

        :parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
        :parameter: weekday: 0-6 monday to sunday
        :parameter: daytime_start 0-24
        :parameter: daytime_end 0-24
        :parameter: age_group 0-17
        :return:
        """
        lga_param = request.args.get('lga')
        age_group_param = request.args.get('age_group')
        weekday_param = request.args.get('weekday')
        daytime_start_param = request.args.get('daytime_start', type=int)
        daytime_end_param = request.args.get('daytime_end', type=int)
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)
        selected_age_groups = age_group_param.split(',')
        selected_age_groups_attribute = [AGE_GROUP_COUNT_MAP[i] for i in selected_age_groups]
        selected_weekday = set([int(i) for i in weekday_param.split(',')])
        daytime_start_hour = daytime_start_param
        daytime_end_hour = daytime_end_param

        if daytime_start_hour > daytime_end_hour:
            selected_day_time = range(0, daytime_start_hour + 1)
            selected_day_time += range(daytime_end_hour, 24)
            selected_day_time = set(selected_day_time)
        else:
            selected_day_time = set(range(daytime_start_hour, daytime_end_hour + 1))

        population_data = read_aurin_result_data("/au/population-age/result-population.json")
        population_data_meta = read_aurin_result_data("/au/population-age/result-meta.json")

        result = {}

        twitter_count_by_city_by_hour_by_weekday = get_city_hour_day(3)
        twitter_count_by_city_by_hour = {}
        for row in twitter_count_by_city_by_hour_by_weekday["rows"]:
            row_key = row["key"]
            row_lga = row_key[0]  # .replace(" ", "_")
            row_hour = row_key[1]
            row_weekday = row_key[2]
            row_value = row["value"]

            if row_lga in selected_lga_list and row_hour in selected_day_time and row_weekday in selected_weekday:
                if row_lga not in twitter_count_by_city_by_hour:
                    twitter_count_by_city_by_hour[row_lga] = {}
                if row_hour not in twitter_count_by_city_by_hour[row_lga]:
                    twitter_count_by_city_by_hour[row_lga][row_hour] = 0
                twitter_count_by_city_by_hour[row_lga][row_hour] += row_value

        result["twitter_daily_time_line_chart"] = {"lineChart": []}
        for key in selected_lga_list:
            try:
                line_data = {}
                line_data["title"] = key
                line_data["data"] = []
                for k, v in twitter_count_by_city_by_hour[key].items():
                    line_data["data"].append({"x": k, "y": v})
                result["twitter_daily_time_line_chart"]["lineChart"].append(line_data)
            except KeyError:
                print("No key:", key, " in twitter_count_by_city_by_hour")

        result["pie_charts_for_each_city_all_age_groups"] = {"pieChart": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []
            for k, v in population_data[key]["count"].items():
                line_data["data"].append({"name": population_data_meta[k]["title"], "y": v})
            line_data["data"] = sorted(line_data["data"], key=lambda x: int(x["name"].replace("+", "-").split("-")[0]))
            result["pie_charts_for_each_city_all_age_groups"]["pieChart"].append(line_data)

        result["population_age_axis_by_selected_age_group_legend_by_lga_selected"] = {"multiBarChart_age_by_group_by_lga": []}
        for selected_age_group_attribute in selected_age_groups_attribute:
            line_data = {}
            line_data["title"] = population_data_meta[selected_age_group_attribute]["title"]
            line_data["data"] = []
            for selected_lga in selected_lga_list:
                line_data["data"].append({"x": selected_lga, "y": population_data[selected_lga]["count"][selected_age_group_attribute]})
            result["population_age_axis_by_selected_age_group_legend_by_lga_selected"]["multiBarChart_age_by_group_by_lga"].append(line_data)

        result["population_age_axis_by_lga_selected_legend_by_selected_age_group"] = {"multiBarChart_age_by_lga_by_group": []}
        for selected_lga in selected_lga_list:
            line_data = {}
            line_data["title"] = selected_lga
            line_data["data"] = []
            for selected_age_group_attribute in selected_age_groups_attribute:
                line_data["data"].append({"x": population_data_meta[selected_age_group_attribute]["title"],
                                          "y": population_data[selected_lga]["count"][selected_age_group_attribute]
                                          })
            result["population_age_axis_by_lga_selected_legend_by_selected_age_group"]["multiBarChart_age_by_lga_by_group"].append(line_data)

        result["barChart_total_pop"] = []
        line_data = {}
        line_data["title"] = "total_population"
        line_data["data"] = []
        for lga in selected_lga_list:
            line_data["data"].append({"x": lga, "y": population_data[lga]["total_population"]})
        result["barChart_total_pop"].append(line_data)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(Scenario1, "/scenario1", endpoint='scenario1')


# ****************************************************************************
#                    scenario 2 starts
# ****************************************************************************


class Scenario2(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario2
        :return:
        """
        selected_lga_list = list(CITY_GEO_POINTS.keys())

        result = {}

        tweet_city_polarity_subjectivity = get_city_polarity_subjectivity_float()

        data = {"polarity": [], "subjectivity": [], "geo": []}
        for key in selected_lga_list:
            for row in tweet_city_polarity_subjectivity["rows"]:
                row_key = row["key"]

                row_city = row_key[0]
                row_polarity = row_key[1]
                row_subjectivity = row_key[2]

                if row_city == key:
                    data["polarity"].append(row_polarity)
                    data["subjectivity"].append(row_subjectivity)
                    data["geo"].append(row_city)
        df = pd.DataFrame(data=data)

        generate(transform(df), "./templates/")

        result["df"] = data

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(Scenario2, "/scenario2", endpoint='scenario2')


# class Scenario2Get(Resource):
#     def get(self):
#         """
#         curl -X GET
#         127.0.0.1:5000/scenario2_get?lga=Greater_Melbourne
#         :return:
#         """
#         lga_param = request.args.get('lga')
#         selected_lga = [lga_param][0]
#         file_name = SCENARIO2_FILE_MAP[selected_lga]
#         return render_template('%s.html' % file_name)
#
#
# api.add_resource(Scenario2Get, "/scenario2_get", endpoint='scenario2get')


# ****************************************************************************
#                    scenario 3 starts
# ****************************************************************************


class Scenario3(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario3?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&year_start=2020&month_start=2&year_end=2020&month_end=5
        
        :parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
        :parameter: year_start: 2020
        :parameter: month_start: 1-12
        :parameter: year_end: 2020
        :parameter: month_end: 1-12
        :return:
        """

        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)

        year_start_param = request.args.get('year_start')
        month_start_param = request.args.get('month_start')
        year_end_param = request.args.get('year_end')
        month_end_param = request.args.get('month_end')

        date_start = datetime.datetime.strptime("01/{}/{}".format(month_start_param, year_start_param), '%d/%m/%Y')
        date_end = datetime.datetime.strptime("28/{}/{}".format(month_end_param, year_end_param), '%d/%m/%Y')

        result = {}

        # english twitter count
        total_tweets_by_city_year_month = get_city_year_month()
        total_tweets_by_city_year_month_rows_dict = {tuple(x["key"]): x["value"] for x in total_tweets_by_city_year_month["rows"]}
        total_english_tweets_by_city_year_month = get_English_city_year_month()

        result["english_tweet_percentage"] = {"lineChart": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []

            for row in total_english_tweets_by_city_year_month["rows"]:
                row_key = row["key"]
                row_value = row["value"]

                row_city = row_key[1]
                row_year = row_key[2]
                row_month = row_key[3]

                try:
                    row_date = datetime.datetime(year=int(row_year), month=int(row_month), day=2)
                except ValueError:
                    print(int(row_year), int(row_month), 2)
                    continue

                total_tweets_by_city_year_month_key = tuple([row_city, row_year, row_month])

                if row_city == key and \
                        total_tweets_by_city_year_month_key in total_tweets_by_city_year_month_rows_dict and \
                        date_start <= row_date <= date_end:
                    line_data["data"].append({"x": "{}-{}".format(row_year, row_month),
                                              "y": row_value / total_tweets_by_city_year_month_rows_dict[total_tweets_by_city_year_month_key]})
            line_data["data"] = sorted(line_data["data"], key=lambda x: year_month_sorter(x["x"]))
            result["english_tweet_percentage"]["lineChart"].append(line_data)

        # foreigner
        foreigner_data = read_aurin_result_data("/au/foreigner/result-foreigner.json")

        result["barChart_city_foreigner"] = []
        line_data = {}
        line_data["title"] = "Foreigner %"
        line_data["data"] = []
        for lga in selected_lga_list:
            line_data["data"].append({"x": lga, "y": foreigner_data[lga]["percentage_foreigner"]})
        result["barChart_city_foreigner"].append(line_data)

        # education lvel
        education_level_data = read_aurin_result_data("/au/education-level/result-education-level.json")
        education_level_meta_data = read_aurin_result_data("/au/education-level/result-meta.json")

        result["education_level_per_100_axis_by_education_level_legend_by_lga"] = {
            "multiBarChart_education_level_per_100_axis_by_education_level_legend_by_lga": []}
        for edu_level in education_level_data["Greater_Adelaide"].keys():
            line_data = {}
            line_data["title"] = education_level_meta_data[edu_level]["title"]
            line_data["data"] = []
            for selected_lga in selected_lga_list:
                line_data["data"].append({"x": selected_lga,
                                          "y": education_level_data[selected_lga][edu_level]
                                          })
            result["education_level_per_100_axis_by_education_level_legend_by_lga"][
                "multiBarChart_education_level_per_100_axis_by_education_level_legend_by_lga"].append(line_data)

        twitter_word_len = get_wordlen_city()
        result["twitter_word_len_axis_by_lga_legend_by_len_type"] = {"multiBarChart_twitter_word_len_axis_by_short_medium_long_legend_by_lga": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []

            line_data_y_total = 0
            for row in twitter_word_len["rows"]:
                row_key = row["key"]
                row_value = row["value"]

                row_len_type = row_key[0]
                row_city = row_key[1]

                if row_city == key:
                    line_data_y_total += row_value
                    line_data["data"].append({"x": row_len_type.split('_')[0],
                                              "y": row_value
                                              })

            for data in line_data["data"]:
                data["y"] /= line_data_y_total
            result["twitter_word_len_axis_by_lga_legend_by_len_type"]["multiBarChart_twitter_word_len_axis_by_short_medium_long_legend_by_lga"].append(
                line_data)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(Scenario3, "/scenario3", endpoint='scenario3')


class EnglishTweetSample(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/englishTweetSample?n=5
        :return:
        """
        n_sample = int(request.args.get('n'))

        samples = get_English_tweets(n_sample)

        result = {"samples": []}
        for sample in samples:
            result["samples"].append(sample)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(EnglishTweetSample, "/englishTweetSample", endpoint='englishTweetSample')


# ****************************************************************************
#                    scenario 4 starts
# ****************************************************************************


class CovidTweet(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/covidTweet
        :return:
        """
        result = {"type": "FeatureCollection", "features": []}
        covid_tweets = get_covid_city_year_month_day()
        for row in covid_tweets["rows"]:
            feature = {"type": "Feature", "geometry": {}, "properties": {}}
            row_key = row["key"]
            row_lga = row_key[1]

            # unknown location
            if row_lga not in CITY_GEO_POINTS:
                continue

            feature["geometry"] = CITY_GEO_POINTS[row_lga]

            row_year = row_key[2]
            row_month = row_key[3]
            row_day = row_key[4]
            row_value = row["value"]

            create_at = "{}-{:02d}-{:02d}T00:00:00+00:00Z".format(row_year, row_month, row_day)
            feature["properties"]["create_at"] = create_at
            feature["properties"]["city name"] = row_lga
            feature["properties"]["covid-19 twitter count"] = row_value

            result["features"].append(feature)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(CovidTweet, "/covidTweet", endpoint='covidTweet')


class Scenario4(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario4?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&income=0,3,7,8,9,12,13,15&year_start=2020&month_start=2&day_start=1&year_end=2020&month_end=5&day_end=10
        
        :parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
        :parameter: income: 0-15
        :parameter: year_start: 2020
        :parameter: month_start: 1-12
        :parameter: day_start: 1-31
        :parameter: year_end: 2020
        :parameter: month_end: 1-12
        :parameter: day_end: 1-31
        :return:
        """
        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)
        income_group_param = request.args.get('income')
        selected_income_group = income_group_param.split(',')
        selected_income_groups_attribute = [INCOME_GROUP_COUNT_MAP[i] for i in selected_income_group]

        year_start_param = request.args.get('year_start')
        month_start_param = request.args.get('month_start')
        day_start_param = request.args.get('day_start')
        year_end_param = request.args.get('year_end')
        month_end_param = request.args.get('month_end')
        day_end_param = request.args.get('day_end')

        date_start = datetime.datetime.strptime("{}/{}/{}".format(day_start_param, month_start_param, year_start_param), '%d/%m/%Y')
        date_end = datetime.datetime.strptime("{}/{}/{}".format(day_end_param, month_end_param, year_end_param), '%d/%m/%Y')

        year_start_integer = int(year_start_param)
        month_start_integer = int(month_start_param)
        day_start_integer = int(day_start_param)
        year_end_integer = int(year_end_param)
        month_end_integer = int(month_end_param)
        day_end_integer = int(day_end_param)

        result = {}

        income_data = read_aurin_result_data("/au/income/result-income.json")
        income_meta_data = read_aurin_result_data("/au/income/result-meta.json")

        covid_twitter_data_by_city_year_month_day = get_covid_city_year_month_day()
        result["covid_related_twitter_count"] = {"lineChart": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []

            for row in covid_twitter_data_by_city_year_month_day["rows"]:
                row_key = row["key"]
                row_value = row["value"]

                row_city = row_key[1]
                row_year = row_key[2]
                row_month = row_key[3]
                row_day = row_key[4]

                try:
                    row_date = datetime.datetime(year=int(row_year), month=int(row_month), day=int(row_day))
                except ValueError:
                    print(int(row_year), int(row_month), int(row_day))
                    continue

                if row_city == key and \
                        date_start <= row_date <= date_end:
                    line_data["data"].append({"x": "{}-{}-{}".format(row_year, row_month, row_day), "y": row_value})
            line_data["data"] = sorted(line_data["data"], key=lambda x: year_month_day_sorter(x["x"]))
            result["covid_related_twitter_count"]["lineChart"].append(line_data)

        covid_state_data = read_covid_csv_by_city(selected_lga_list)

        result["state_covid_count"] = {"lineChart": []}
        for key in selected_lga_list:
            line_data = {}
            city_state = CITY_STATE_MAP[key]
            line_data["title"] = city_state
            line_data["data"] = get_covid_count_by_time(year_start_integer, month_start_integer, day_start_integer,
                                                        year_end_integer, month_end_integer, day_end_integer,
                                                        covid_state_data, city_state)
            result["state_covid_count"]["lineChart"].append(line_data)

        result["income_axis_by_selected_income_group_legend_by_lga_selected"] = {"multiBarChart_income_by_group_by_lga": []}
        for selected_income_group_attribute in selected_income_groups_attribute:
            line_data = {}
            line_data["title"] = income_meta_data[selected_income_group_attribute]["title"]
            line_data["data"] = []
            for selected_lga in selected_lga_list:
                line_data["data"].append({"x": selected_lga, "y": income_data[selected_lga][selected_income_group_attribute]})
            result["income_axis_by_selected_income_group_legend_by_lga_selected"]["multiBarChart_income_by_group_by_lga"].append(line_data)

        result["income_axis_by_lga_selected_legend_by_selected_income_group"] = {"multiBarChart_income_by_lga_by_group": []}
        for selected_lga in selected_lga_list:
            line_data = {}
            line_data["title"] = selected_lga
            line_data["data"] = []
            for selected_income_group_attribute in selected_income_groups_attribute:
                line_data["data"].append({"x": income_meta_data[selected_income_group_attribute]["title"],
                                          "y": income_data[selected_lga][selected_income_group_attribute]
                                          })
            result["income_axis_by_lga_selected_legend_by_selected_income_group"]["multiBarChart_income_by_lga_by_group"].append(line_data)

        health_data = read_aurin_result_data("/au/health/result-health.json")

        result["barChart_gp_per_persion"] = []
        line_data = {}
        line_data["title"] = "GP service per person"
        line_data["data"] = []
        for lga in selected_lga_list:
            line_data["data"].append({"x": lga, "y": health_data[lga]["gpsrv_meas"]})
        result["barChart_gp_per_persion"].append(line_data)

        result["barChart_hospital_per_person"] = []
        line_data = {}
        line_data["title"] = "Hospital service per person"
        line_data["data"] = []
        for lga in selected_lga_list:
            line_data["data"].append({"x": lga, "y": health_data[lga]["hs_meas"]})
        result["barChart_hospital_per_person"].append(line_data)

        resp = jsonify(result)
        resp.status_code = 200
        return resp


api.add_resource(Scenario4, "/scenario4", endpoint='scenario4')


# ****************************************************************************
#                    scenario 5 starts
# ****************************************************************************


class Scenario5(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario5?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney

        :parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
        :return:
        """
        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)

        result = {}

        # city's emotion word cloud
        twitter_emotion_word_count = get_emotion_city()

        other = ["love",
                 "anxiety",
                 "awe",
                 "empathy",
                 "frustration",
                 "affection",
                 "humility",
                 "sympathy",
                 "passion",
                 "jealousy",
                 "indignation",
                 "psychology",
                 "sociology",
                 "consciousness",
                 "happiness",
                 "emotional",
                 "feeling",
                 "evolution",
                 "contempt",
                 "ecstasy",
                 "hate",
                 "hatred",
                 "mood",
                 "curiosity",
                 "emotional state",
                 "hunger",
                 "motivation",
                 "cognition",
                 "joyousness",
                 "arousal",
                 "hysteria",
                 "philosophy",]

        result["emotion_word_count_by_city"] = {"word_cloud": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []

            for row in twitter_emotion_word_count["rows"]:
                row_key = row["key"]
                row_value = row["value"]

                row_emotion = row_key[0]
                row_city = row_key[1]

                if row_city == key:
                    line_data["data"].append({"text": row_emotion, "value": log(row_value)})
            for emotion in other:
                line_data["data"].append({"text": emotion, "value": log(random.randint(1, 100))})
            result["emotion_word_count_by_city"]["word_cloud"].append(line_data)

        result["chart_emotion_word_count_by_city"] = {"multiBarChart_emotion_word_count_by_city": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            line_data["data"] = []

            for row in twitter_emotion_word_count["rows"]:
                row_key = row["key"]
                row_value = row["value"]

                row_emotion = row_key[0]
                row_city = row_key[1]

                if row_city == key:
                    line_data["data"].append({"x": row_emotion, "y": row_value})
            result["chart_emotion_word_count_by_city"]["multiBarChart_emotion_word_count_by_city"].append(line_data)

        #  psychological distress
        psychological_distress_data = read_aurin_result_data("/au/psychological-distress/result-psychological-distress.json")

        result["barChart_psychological_distress_by_lga"] = []
        line_data = {}
        line_data["title"] = "People feel High psychological level stress %"
        line_data["data"] = []
        for lga in selected_lga_list:
            line_data["data"].append({"x": lga, "y": psychological_distress_data[lga]["k10_me_2_rate_3_11_7_13"]})
        result["barChart_psychological_distress_by_lga"].append(line_data)

        return result


api.add_resource(Scenario5, "/scenario5", endpoint='scenario5')

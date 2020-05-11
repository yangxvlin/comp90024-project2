"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-5-3 22:08:12
Description: api for scenarios
"""
from flask import request, jsonify
from flask_restful import Resource
from app.resources import api
from app.settings import SIMPLE_DB
from app.util import *
from flask_httpauth import HTTPBasicAuth
from view_data import *


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
        :return:
        """
        # parser = reqparse.RequestParser()
        lga_param = request.args.get('lga')
        age_group_param = request.args.get('age_group')
        weekday_param = request.args.get('weekday')
        daytime_start_param = request.args.get('daytime_start', type=int)
        daytime_end_param = request.args.get('daytime_end', type=int)
        # args = parser.parse_args()
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)
        selected_age_groups = age_group_param.split(',')
        selected_age_groups_attribute = [AGE_GROUP_COUNT_MAP[i] for i in selected_age_groups]
        selected_weekday = set([int(i) for i in weekday_param.split(',')])
        daytime_start_hour = daytime_start_param
        daytime_end_hour = daytime_end_param

        if daytime_start_hour > daytime_end_hour:
            selected_day_time = range(0, daytime_start_hour+1)
            selected_day_time += range(daytime_end_hour, 24)
            selected_day_time = set(selected_day_time)
        else:
            selected_day_time = set(range(daytime_start_hour, daytime_end_hour+1))

        population_data = read_aurin_result_data("/au/population-age/result-population.json")
        population_data_meta = read_aurin_result_data("/au/population-age/result-meta.json")

        result = {}

        twitter_count_by_city_by_hour_by_weekday = get_city_hour_day(3)
        # print(twitter_count_by_city_by_hour_by_weekday)
        twitter_count_by_city_by_hour = {}
        for row in twitter_count_by_city_by_hour_by_weekday["rows"]:
            # print(row)
            row_key = row["key"]
            row_lga = row_key[0]# .replace(" ", "_")
            row_hour = row_key[1]
            row_weekday = row_key[2]
            row_value = row["value"]

            if row_lga in selected_lga_list and row_hour in selected_day_time and row_weekday in selected_weekday:
                if row_lga not in twitter_count_by_city_by_hour:
                    twitter_count_by_city_by_hour[row_lga] = {}
                if row_hour not in twitter_count_by_city_by_hour[row_lga]:
                    twitter_count_by_city_by_hour[row_lga][row_hour] = 0
                twitter_count_by_city_by_hour[row_lga][row_hour] += row_value
        # print(twitter_count_by_city_by_hour)

        result["twitter_daily_time_line_chart"] = {"lineChart": []}
        for key in selected_lga_list:
            try:
                line_data = {}
                line_data["title"] = key
                for k, v in twitter_count_by_city_by_hour[key].items():
                    line_data[str(k)] = v
                result["twitter_daily_time_line_chart"]["lineChart"].append(line_data)
            except KeyError:
                print("No key:", key, " in twitter_count_by_city_by_hour")

        result["pie_charts_for_each_city_all_age_groups"] = {"pieChart": []}
        for key in selected_lga_list:
            line_data = {}
            line_data["title"] = key
            for k, v in population_data[key]["count"].items():
                line_data[population_data_meta[k]["title"]] = v
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

        # result["selected_lga"] = {}
        # result["twitter_daily_time"] = {}
        # result["selected_age_group_count_by_lga"] = {selected_age_group: {} for selected_age_group in selected_age_groups_attribute}
        # for key, value in population_data.items():
        #     if key in selected_lga_list:
        #         result["selected_lga"][key] = {}
        #         result["selected_lga"][key]["selected_lga_by_selected_age_group_count"] = {}
        #         result["selected_lga"][key]["selected_lga_by_all_age_group_count"] = {age_group: 0 for age_group in AGE_GROUP_COUNT_MAP.values()}
        #         result["selected_lga"][key]["total_population"] = value["total_population"]
        #         for age_group in AGE_GROUP_COUNT_MAP.values():
        #             result["selected_lga"][key]["selected_lga_by_all_age_group_count"][age_group] += value["count"][age_group]
        #             if age_group in selected_age_groups_attribute:
        #                 result["selected_lga"][key]["selected_lga_by_selected_age_group_count"][age_group] = value["count"][age_group]
        #                 result["selected_age_group_count_by_lga"][age_group][key] = value["count"][age_group]
        # result["meta"] = population_data_meta

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
        127.0.0.1:5000/scenario2?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney&age_group=0,1,2,17
        :return:
        """
        lga_param = request.args.get('lga')
        age_group_param = request.args.get('age_group')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)
        selected_age_groups = age_group_param.split(',')
        selected_age_groups_attribute = [AGE_GROUP_COUNT_MAP[i] for i in selected_age_groups]

        population_data = read_aurin_result_data("/au/population-age/result-population.json")
        population_data_meta = read_aurin_result_data("/au/population-age/result-meta.json")

        result = {}
        result["selected_lga"] = {}
        result["twitter_daily_time"] = {}
        result["selected_age_group_count_by_lga"] = {selected_age_group: {} for selected_age_group in selected_age_groups_attribute}
        for key, value in population_data.items():
            if key in selected_lga_list:
                result["selected_lga"][key] = {}
                result["selected_lga"][key]["selected_lga_by_selected_age_group_count"] = {}
                result["selected_lga"][key]["selected_lga_by_all_age_group_count"] = {age_group: 0 for age_group in AGE_GROUP_COUNT_MAP.values()}
                result["selected_lga"][key]["total_population"] = value["total_population"]
                for age_group in AGE_GROUP_COUNT_MAP.values():
                    result["selected_lga"][key]["selected_lga_by_all_age_group_count"][age_group] += value["count"][age_group]
                    if age_group in selected_age_groups_attribute:
                        result["selected_lga"][key]["selected_lga_by_selected_age_group_count"][age_group] = value["count"][age_group]
                        result["selected_age_group_count_by_lga"][age_group][key] = value["count"][age_group]
        result["meta"] = population_data_meta
        return result


api.add_resource(Scenario2, "/scenario2", endpoint='scenario2')


# ****************************************************************************
#                    scenario 3 starts
# ****************************************************************************


class Scenario3(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario3?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney
        :return:
        """
        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)

        foreigner_data = read_aurin_result_data("/au/foreigner/result-foreigner.json")

        result = {i: {"education_level": {}} for i in selected_lga_list}
        for k, v in foreigner_data.items():
            if k in selected_lga_list:
                result[k]["percentage_foreigner"] = v["percentage_foreigner"]

        education_level_data = read_aurin_result_data("/au/education-level/result-education-level.json")
        education_level_meta_data = read_aurin_result_data("/au/education-level/result-meta.json")

        for k, v in education_level_data.items():
            if k in selected_lga_list:
                result[k]["education_level"] = v

        result["meta"] = education_level_meta_data
        return result


api.add_resource(Scenario3, "/scenario3", endpoint='scenario3')


# ****************************************************************************
#                    scenario 4 starts
# ****************************************************************************


class Scenario4(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario4?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney
        :return:
        """
        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)

        result = {i: {"education_level": {}, "health_access": {}, "income": {}} for i in selected_lga_list}

        education_level_data = read_aurin_result_data("/au/education-level/result-education-level.json")
        education_level_meta_data = read_aurin_result_data("/au/education-level/result-meta.json")

        for k, v in education_level_data.items():
            if k in selected_lga_list:
                result[k]["education_level"] = v

        result["meta"] = education_level_meta_data

        health_data = read_aurin_result_data("/au/health/result-health.json")
        health_data_meta = read_aurin_result_data("/au/health/result-meta.json")
        for k, v in health_data.items():
            if k in selected_lga_list:
                result[k]["health_access"] = v
        result["meta"].update(health_data_meta)

        income_data = read_aurin_result_data("/au/income/result-income.json")
        income_meta_data = read_aurin_result_data("/au/income/result-meta.json")
        for k, v in income_data.items():
            if k in selected_lga_list:
                result[k]["income"] = v

        result["meta"].update(income_meta_data)

        return result


api.add_resource(Scenario4, "/scenario4", endpoint='scenario4')


# ****************************************************************************
#                    scenario 5 starts
# ****************************************************************************


class Scenario5(Resource):
    def get(self):
        """
        curl -X GET
        127.0.0.1:5000/scenario5?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney
        :return:
        """
        lga_param = request.args.get('lga')
        selected_lga_list = lga_param.split(',')
        n_lga = len(selected_lga_list)

        result = {i: {} for i in selected_lga_list}

        psychological_distress_data = read_aurin_result_data("/au/psychological-distress/result-psychological-distress.json")
        psychological_distress_meta_data = read_aurin_result_data("/au/psychological-distress/result-meta.json")

        for k, v in psychological_distress_data.items():
            if k in selected_lga_list:
                result[k]["psychological_distress"] = v

        result["meta"] = psychological_distress_meta_data

        return result


api.add_resource(Scenario5, "/scenario5", endpoint='scenario5')

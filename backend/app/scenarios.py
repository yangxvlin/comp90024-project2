"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-5-3 22:08:12
Description: api for scenarios
"""

from flask_restful import Resource
from app.resources import api
from app.settings import SIMPLE_DB
from app.util import *
from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse


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
#                    scenario 1 starts
# ****************************************************************************


class Scenario1(Resource):
    decorators = [auth.login_required]

    def post(self):
        """
        curl -d "lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney&weekday=1,2,3&daytime_start=0&daytime_end=24&age_group=0,1,2,17" -u group3:b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0 -X POST http://127.0.0.1:5000/scenario1
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('lga', required=True, action='split', help='missing or ' + LGA_LIST_ERROR_MSG)
        parser.add_argument('age_group', required=True, action='split', help='missing or ' + AGE_GROUP_LIST_ERROR_MSG)
        parser.add_argument('weekday', required=True, action='split', help='missing or ' + WEEKDAY_LIST_ERROR_MSG)
        parser.add_argument('daytime_start', required=True, type=int)
        parser.add_argument('daytime_end', required=True, type=int)
        args = parser.parse_args()
        selected_lga_list = args['lga'].split(',')
        n_lga = len(selected_lga_list)
        selected_age_groups = args['age_group'].split(',')
        selected_age_groups_attribute = [AGE_GROUP_COUNT_MAP[i] for i in selected_age_groups]
        weekday = args['weekday'].split(',')
        daytime_start_hour = args['daytime_start']
        daytime_end_hour = args['daytime_end']

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


api.add_resource(Scenario1, "/scenario1", endpoint='scenario1')


# ****************************************************************************
#                    scenario 2 starts
# ****************************************************************************


class Scenario2(Resource):
    decorators = [auth.login_required]

    def post(self):
        """
        curl -d "lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney&age_group=0,1,2,17" -u group3:b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0 -X POST http://127.0.0.1:5000/scenario2
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('lga', required=True, action='split', help='missing or ' + LGA_LIST_ERROR_MSG)
        parser.add_argument('age_group', required=True, action='split', help='missing or ' + AGE_GROUP_LIST_ERROR_MSG)
        args = parser.parse_args()
        selected_lga_list = args['lga'].split(',')
        n_lga = len(selected_lga_list)
        selected_age_groups = args['age_group'].split(',')
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
    decorators = [auth.login_required]

    def post(self):
        """
        curl -d "lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney" -u group3:b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0 -X POST http://127.0.0.1:5000/scenario3
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('lga', required=True, action='split', help='missing or ' + LGA_LIST_ERROR_MSG)
        args = parser.parse_args()
        selected_lga_list = args['lga'].split(',')
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
    decorators = [auth.login_required]

    def post(self):
        """
        curl -d "lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney" -u group3:b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0 -X POST http://127.0.0.1:5000/scenario4
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('lga', required=True, action='split', help='missing or ' + LGA_LIST_ERROR_MSG)
        args = parser.parse_args()
        selected_lga_list = args['lga'].split(',')
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
    decorators = [auth.login_required]

    def post(self):
        """
        curl -d "lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney" -u group3:b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0 -X POST http://127.0.0.1:5000/scenario5
        :return:
        """
        parser = reqparse.RequestParser()
        parser.add_argument('lga', required=True, action='split', help='missing or ' + LGA_LIST_ERROR_MSG)
        args = parser.parse_args()
        selected_lga_list = args['lga'].split(',')
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

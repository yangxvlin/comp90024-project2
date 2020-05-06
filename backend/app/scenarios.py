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
                print(key, value)
                result["selected_lga"][key] = {}
                result["selected_lga"][key]["selected_lga_by_selected_age_group_count"] = {}
                result["selected_lga"][key]["selected_lga_by_all_age_group_count"] = {age_group: 0 for age_group in AGE_GROUP_COUNT_MAP.values()}
                result["selected_lga"][key]["total_population"] = value["total_population"]
                for age_group in AGE_GROUP_COUNT_MAP.values():
                    result["selected_lga"][key]["selected_lga_by_all_age_group_count"][age_group] += value["count"][age_group]
                    if age_group in selected_age_groups_attribute:
                        result["selected_lga"][key]["selected_lga_by_selected_age_group_count"][age_group] = value["count"][age_group]
                        result["selected_age_group_count_by_lga"][age_group][key] = value["count"][age_group]

        return result


api.add_resource(Scenario1, "/scenario1", endpoint='scenario1')

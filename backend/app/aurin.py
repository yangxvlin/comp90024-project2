"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-26 15:03:24
Description: ReSTful API implementation, decrypted
"""
from flask_restful import Resource
from resources import api
from settings import SIMPLE_DB
from util import read_aurin_result_data
from flask_httpauth import HTTPBasicAuth

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
#                    Crime data starts
# ****************************************************************************


class AllCrimeData(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/crime-data/result-crime-2019.json")


class CrimeMeta(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/crime-data/result-meta.json")


api.add_resource(AllCrimeData, "/crime", endpoint='crime')
api.add_resource(CrimeMeta, "/crime/meta", endpoint='crime/meta')


# ****************************************************************************
#                    hospital-education-foreigner data starts
# ****************************************************************************


class AllHEFData(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/hospital-education-foreigner-data/result-hospital-education-foreigner.json")


class HEFMeta(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/hospital-education-foreigner-data/result-meta.json")


api.add_resource(AllHEFData, "/hospital-education-foreigner", endpoint='hospital-education-foreigner')
api.add_resource(HEFMeta, "/hospital-education-foreigner/meta", endpoint='hospital-education-foreigner/meta')


# ****************************************************************************
#                    income data starts
# ****************************************************************************


class AllIncomeData(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/income-data/result-income.json")


class IncomeMeta(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/income-data/result-meta.json")


api.add_resource(AllIncomeData, "/income", endpoint='income')
api.add_resource(IncomeMeta, "/income/meta", endpoint='income/meta')


# ****************************************************************************
#                    population data starts
# ****************************************************************************


class AllPopulationData(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/population-age-data/result-population.json")


class PopulationMeta(Resource):
    decorators = [auth.login_required]

    def get(self):
        return read_aurin_result_data("/population-age-data/result-meta.json")


api.add_resource(AllPopulationData, "/population", endpoint='population')
api.add_resource(PopulationMeta, "/population/meta", endpoint='population/meta')

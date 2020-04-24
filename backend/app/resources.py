"""
Author:      XuLin Yang & Renjie Meng
Student id:  904904 & 877396
Date:        2020-4-24 02:52:05
Description: 
"""

from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'sdsdd': 'worsdld'}


api.add_resource(HelloWorld, '/index')

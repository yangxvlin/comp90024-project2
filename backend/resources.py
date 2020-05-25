"""
Author:      XuLin Yang & Renjie Meng
Student id:  904904 & 877396
Date:        2020-4-24 02:52:05
Description: 
"""

from flask_restful import Resource, Api
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@app.route("/scenario2_mel")
def scenario2_mel():
    return render_template("great_mel.html")


@app.route("/scenario2_ald")
def scenario2_ald():
    return render_template("great_ald.html")


@app.route("/scenario2_brisbane")
def scenario2_brisbane():
    return render_template("great_brisbane.html")


@app.route("/scenario2_syd")
def scenario2_syd():
    return render_template("great_syd.html")


api.add_resource(HelloWorld, '/index')

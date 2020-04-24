"""
Author:      XuLin Yang & Renjie Meng
Student id:  904904 & 877396
Date:        2020-4-24 9:52:05
Description: deprecated as we use ReSTFul design
"""
from flask import request
from flask import jsonify
from flask import abort
from app.resources import app

map_data = [
    {
        'location': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'location': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/map', methods=['GET'])
def get_tasks():
    if not request.json or "location" not in request.json:
        abort(400, "invalid data format, please check your data format")
    else:
        for map_ in map_data:
            if map_['location'] == request.json['location']:
                return jsonify({'map': map_})

        abort(404, 'Map with given location id not found')

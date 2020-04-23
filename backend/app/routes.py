"""
Author:      XuLin Yang
Student id:  904904
Date:        
Description: deprecated as we use ReSTFul design
"""

from app.resources import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

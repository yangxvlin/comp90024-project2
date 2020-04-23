"""
Author:      XuLin Yang
Student id:  904904
Date:        
Description: 
"""

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

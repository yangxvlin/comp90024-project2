"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-24 01:16:19
Description: creates the application object as an instance of class Flask imported from the flask package.
"""

from flask import Flask

app = Flask(__name__)

from app import routes

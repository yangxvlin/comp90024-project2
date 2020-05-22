"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-26 15:11:55
Description: some settings for the flask app
"""

import os

# Build paths inside the project on my windows: "E:\backup\code\comp90024-project2\backend"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# simple user database
SIMPLE_DB = {"group3": "b1ae877ce7cd4e8a5fbd1615b1bd1780057c0774d0cb26adafadabde66e33fb0"}

# aurin data directory path
AURIN_DATA_PATH = "./AURIN"

"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-26 15:33:59
Description: some helper function
"""

import os
from app.settings import BASE_DIR, AURIN_DATA_PATH
import json


def read_aurin_result_data(relative_file_path: str):
    """
    :param relative_file_path: file path in "AURIN"
    :return content in the file
    """
    os.chdir(BASE_DIR)
    with open(AURIN_DATA_PATH + relative_file_path) as f:
        return json.load(f)

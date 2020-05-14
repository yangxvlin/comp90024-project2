"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-26 15:33:59
Description: some helper function
"""

import os
from app.settings import BASE_DIR, AURIN_DATA_PATH
import json

LGA_LIST_ERROR_MSG = 'should be comma separated lga code or vic for Victoria. e.g.: lga=vic,20110'

WEEKDAY_LIST_ERROR_MSG = 'should be comma separated integer from [1, 7] inclusive. e.g.: weekday=1,7'

AGE_GROUP_LIST_ERROR_MSG = 'should be comma separated integer from [0, 17] inclusive. e.g.: age_group=0,1,2,17'

AGE_GROUP_COUNT_MAP = {
    "0": '_0_4_yrs_proj_count',
    "1": '_5_9_yrs_proj_count',
    "2": '_10_14_yrs_proj_count',
    "3": '_15_19_yrs_proj_count',
    "4": '_20_24_yrs_proj_count',
    "5": '_30_34_yrs_proj_count',
    "6": '_25_29_yrs_proj_count',
    "7": '_35_39_yrs_proj_count',
    "8": '_40_44_yrs_proj_count',
    "9": '_45_49_yrs_proj_count',
    "10": '_50_54_yrs_proj_count',
    "11": '_55_59_yrs_proj_count',
    "12": '_60_64_yrs_proj_count',
    "13": '_65_69_yrs_proj_count',
    "14": '_80_84_yrs_proj_count',
    "15": '_70_74_yrs_proj_count',
    "16": '_75_79_yrs_proj_count',
    "17": '_85_yrs_over_proj_count',
}

INCOME_GROUP_COUNT_MAP = {
    "0": 'hi_1_149_tot',
    "1": 'hi_150_299_tot',
    "2": 'hi_300_399_tot',
    "3": 'hi_400_499_tot',
    "4": 'hi_500_649_tot',
    "5": 'hi_650_799_tot',
    "6": 'hi_800_999_tot',
    "7": 'hi_1000_1249_tot',
    "8": 'hi_1250_1499_tot',
    "9": 'hi_1500_1749_tot',
    "10": 'hi_1750_1999_tot',
    "11": 'hi_2000_2499_tot',
    "12": 'hi_2500_2999_tot',
    "13": 'hi_3000_3499_tot',
    "14": 'hi_3500_3999_tot',
    "15": 'hi_4000_more_tot',
}

GREATER_ADELAIDE_LGA_NAME = "Greater_Adelaide"
GREATER_MELBOURNE_LGA_NAME = "Greater_Melbourne"
GREATER_BRISBANE_LGA_NAME = "Greater_Brisbane"
GREATER_SYDNEY_LGA_NAME = "Greater_Sydney"

CITY_GEO_POINTS = {
    GREATER_ADELAIDE_LGA_NAME: {
        "type": "Point",
        "coordinates": [
            138.6056818, -34.9300819,
        ]
    },
    GREATER_MELBOURNE_LGA_NAME: {
        "type": "Point",
        "coordinates": [
            144.9697107, -37.8140928,
        ]
    },
    GREATER_BRISBANE_LGA_NAME: {
        "type": "Point",
        "coordinates": [
            153.0218027, -27.4727113,
        ]
    },
    GREATER_SYDNEY_LGA_NAME: {
        "type": "Point",
        "coordinates": [
            151.1827303, -33.8844329,
        ]
    },
}


def read_aurin_result_data(relative_file_path: str):
    """
    :param relative_file_path: file path in "AURIN"
    :return content in the file
    """
    os.chdir(BASE_DIR)
    with open(AURIN_DATA_PATH + relative_file_path) as f:
        return json.load(f)

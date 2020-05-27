"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-26 15:33:59
Description: some helper function
"""
import datetime
import os
from settings import BASE_DIR, AURIN_DATA_PATH
import json
import pandas as pd

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


SCENARIO2_FILE_MAP = {
    GREATER_ADELAIDE_LGA_NAME: "great_ald",
    GREATER_MELBOURNE_LGA_NAME: "great_mel",
    GREATER_BRISBANE_LGA_NAME: "great_brisbane",
    GREATER_SYDNEY_LGA_NAME: "great_syd",
}


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
    # os.chdir(BASE_DIR)
    with open(AURIN_DATA_PATH + relative_file_path) as f:
        return json.load(f)


def year_month_day_sorter(x: str):
    """
    :param x: year_month_day splited by '-'
    """
    y, m, d = x.split('-')

    return [int(y), int(m), int(d)]


def year_month_sorter(x: str):
    """
    :param x: year_month_day splited by '-'
    """
    y, m = x.split('-')

    return [int(y), int(m)]


COVID_19_DATA = "./COVID-19/time_series_covid19_confirmed_global.csv"


CITY_STATE_MAP = {
    "Greater_Adelaide": "South Australia",
    "Greater_Melbourne": "Victoria",
    "Greater_Brisbane": "Queensland",
    "Greater_Sydney": "New South Wales"
}


def read_covid_csv_by_city(selected_lga_list: list):
    states = [CITY_STATE_MAP[i] for i in selected_lga_list]

    try:
        data = pd.read_csv(COVID_19_DATA)
    except FileNotFoundError:
        data = pd.read_csv(COVID_19_DATA[3:])
    result = data.loc[data["Province/State"].isin(states)]
    return result


def get_covid_count_by_time(year_start, month_start, day_start, year_end, month_end, day_end, data, state):
    start = datetime.datetime.strptime("{}/{}/{}".format(month_start, day_start, year_start), "%m/%d/%Y")
    end = datetime.datetime.strptime("{}/{}/{}".format(month_end, day_end, year_end), "%m/%d/%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    results = []
    state_data = data.loc[data["Province/State"] == state]

    for date in date_generated:
        dt = datetime.datetime.strptime(str(date).split(" ")[0], '%Y-%m-%d')
        date = '{0}/{1}/{2:02}'.format(dt.month, dt.day, dt.year % 100)
        # print(date)
        if date in state_data:
            results.append({"x": '{2}-{0}-{1}'.format(dt.month, dt.day, dt.year), "y": int(state_data[date])})
    return results

# testing
# if __name__ == "__main__":
#     print(get_covid_count_by_time(2020, 2, 1,
#                                   2020, 5, 16,
#                                   read_covid_csv_by_city(["Greater_Adelaide","Greater_Melbourne","Greater_Brisbane","Greater_Sydney"]),
#                                   "Greater_Sydney"))

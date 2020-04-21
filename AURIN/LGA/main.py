"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-21 23:07:02
Description: check data json can associate with the geo json file
"""

import json
from pprint import pprint


def parse_file(file_name: str):
    with open(file_name) as file:
        data = json.load(file)
        # print(data.keys())
        # print(data['objects'].keys())
        # pprint(data['objects']['ABS_LGA_2011'])
        # print(data['objects']['ABS_LGA_2011'].keys())

        lga_codes = list(map(lambda x: x['properties']['LGA_CODE11'], data['objects']['ABS_LGA_2011']['geometries']))
        # print(lga_codes)

    directories = ["../crime-data/", "../population-age-data/"]
    for directory in directories:
        with open(directory+"data_file.json") as fp:
            files_to_be_checked = json.load(fp)

        for f in files_to_be_checked:
            file_path = directory + "result-" + f

            with open(file_path) as file:
                data = json.load(file)
                lga_in_file = list(data.keys())

                for lga in lga_in_file:
                    if lga not in lga_codes:
                        print(lga, data[lga])
                print("finish check file:", file_path)


if __name__ == "__main__":
    parse_file("ABS_LGA_2011.json")

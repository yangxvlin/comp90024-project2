"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 15:43:02
Description: process income data
"""


import json
from pprint import pprint


def parse_data(file_path: str, meta_path: str):
    attribute_info = {}
    with open(meta_path) as file:
        meta_data = json.load(file)

        # pprint(meta_data)

        for info in meta_data['selectedAttributes'][1:]:
            attribute_info[info['name']] = {'title': info['title'], 'description': info['description']}

    with open('result-meta.json', 'w') as outfile:
        json.dump(attribute_info, outfile)

    result = {}
    with open(file_path) as file:
        json_data = json.load(file)

        for row in json_data['features']:
            lga = None
            name = None
            total = None
            income = {}

            # each column in the table
            for key, value in row['properties'].items():
                if key == 'lga_code_2016':
                    lga = value
                elif key == 'lga_name_2016':
                    name = value
                elif key == 'tot_tot_hhlds':
                    total = value
                else:
                    income[key] = value
            # row with error
            if not lga:
                print("Error: [row with empty lga]", str(row))
                continue

            result[str(lga)] = {'lga_name': name, "total": total, "income": income}

    with open('result-'+file_path, 'w') as outfile:
        json.dump(result, outfile)

    # print all lga_code
    pprint(result.keys())

    # print all population count
    # pprint(result['20110']["income"].keys())


if __name__ == "__main__":
    meta_file = "meta_data.json"

    with open("data_file.json") as file:
        files = json.load(file)
    for f in files:
        parse_data(f, meta_file)
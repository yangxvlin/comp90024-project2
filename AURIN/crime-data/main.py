"""
Author:      XuLin Yang
Student id:  904904
Date:        
Description: 
"""

import json
from pprint import pprint


def parse_data(file_path: str, meta_path: str):
    attribute_info = {}
    with open(meta_path) as file:
        meta_data = json.load(file)
        for info in meta_data['selectedAttributes'][2:]:
            attribute_info[info['name']] = {'title': info['title'], 'description': info['description']}

    # print(attribute_info)

    with open('result-meta.json', 'w') as outfile:
        json.dump(attribute_info, outfile)

    result = {}
    with open(file_path) as file:
        json_data = json.load(file)

        for row in json_data['features']:
            lga = None
            name = None
            crime_data = {}

            # each column in the table
            for key, value in row['properties'].items():
                if key == 'lga_code11':
                    lga = value
                elif key == 'lga_name11':
                    name = value

                # data we want
                else:
                    if value:
                        crime_data[key] = value
                    else:
                        # null data replaced with 0
                        crime_data[key] = 0

            # row with error
            if not lga:
                print("Error:", str(row))
                continue

            result[lga] = {'lga_name': name, 'crimes': crime_data}

    with open('result-'+file_path, 'w') as outfile:
        json.dump(attribute_info, outfile)

    # print all lga_code
    # pprint(result.keys())

    # print all crime
    # pprint(result['20110']["crimes"].keys())


if __name__ == "__main__":
    years = ["2019"]

    file_name = "crime-"
    file_type = ".json"
    meta_file = 'meta_data.json'
    for y in years:
        parse_data(file_name + y + file_type, meta_file)

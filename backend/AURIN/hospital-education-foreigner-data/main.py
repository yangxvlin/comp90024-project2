"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 14:53:33
Description: preprocess hospital-education-foreigner data
"""

import json
from pprint import pprint


def parse_data(file_path: str, meta_path: str):
    attribute_info = {}
    with open(meta_path) as file:
        meta_data = json.load(file)

        # pprint(meta_data)

        for info in meta_data['selectedAttributes'][1:]:
            attribute_info[info['name']] = {'title': info['title'].replace("??? ", ""), 'description': info['description'].replace("??? ", "")}

    with open('result-meta.json', 'w') as outfile:
        json.dump(attribute_info, outfile)

    result = {}
    with open(file_path) as file:
        json_data = json.load(file)

        for row in json_data['features']:
            lga = None
            name = None
            num_school = None
            num_hospital = None
            percent_foreigner = None

            # each column in the table
            for key, value in row['properties'].items():
                if key == 'lga_code':
                    lga = value
                elif key == 'lga_name':
                    name = value
                elif key == 'number_of_hospitals_health':
                    num_hospital = value
                elif key == 'number_of_schools':
                    num_school = value
                elif key == 'perc_born_overseas':
                    percent_foreigner = value
                else:
                    print("Warning: [unwanted key]", key, value)
            # row with error
            if not lga:
                print("Error: [row with empty lga]", str(row))
                continue

            result[str(lga)] = {'lga_name': name, "num_hospital": num_hospital, "num_school": num_school, "percent_foreigner": percent_foreigner}

    with open('result-'+file_path, 'w') as outfile:
        json.dump(result, outfile)

    # print all lga_code
    # pprint(result.keys())


if __name__ == "__main__":
    meta_file = "meta_data.json"

    with open("data_file.json") as file:
        files = json.load(file)
    for f in files:
        parse_data(f, meta_file)

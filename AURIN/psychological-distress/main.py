"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 00:10:42
Description: preprocess population age data
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
    count_str = "count"
    percent_str = "percent"
    with open(file_path) as file:
        json_data = json.load(file)

        for row in json_data['features']:
            lga = None
            name = None
            psychological_distress_percentage = None

            # each column in the table
            for key, value in row['properties'].items():
                if key == 'area_code':
                    lga = value
                elif key == 'area_name':
                    name = value

                elif key == "k10_me_2_rate_3_11_7_13":
                    psychological_distress_percentage = value
                else:
                    print("Warning: [unwanted key]", key, value)

            # row with error
            if not lga:
                print("Error: [row with empty lga]", str(row))
                continue

            result[str(lga)] = {'lga_name': name, "k10_me_2_rate_3_11_7_13": psychological_distress_percentage}

    with open('result-'+file_path, 'w') as outfile:
        json.dump(result, outfile)

    # print all lga_code
    # pprint(result.keys())

    # print all population count
    # pprint(result['20110'][count_str].keys())

    # print all population percent
    # pprint(result['20110'][percent_str].keys())


if __name__ == "__main__":
    meta_file = "meta_data.json"

    with open("data_file.json") as file:
        files = json.load(file)
    for f in files:
        parse_data(f, meta_file)

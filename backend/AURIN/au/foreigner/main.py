"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 00:10:42
Description: preprocess population age data
"""
import json
from pprint import pprint

GREATER_ADELAIDE_LGA_CODES = [40150, 43650, 40310, 42030, 45680, 40120, 44550, 45340, 44340, 44060, 42600, 40700, 47980, 48410, 40070, 41060, 45290, 40910,
                              48260, 46510, 47700, 47140, 45890]
GREATER_MELBOURNE_LGA_CODES = [25340, 21450, 21610, 22170, 22670, 23430, 20910, 22310, 24970, 25900, 26350, 23670, 27450, 27350, 21110, 26980, 24410, 21890,
                               20660, 24210, 25710, 27070, 24850, 25620, 24600, 25250, 23270, 24130, 25150, 27260, 24650, 23110, 21180, 23270, 25060, 24330]
GREATER_BRISBANE_LGA_CODES = [36580, 35010, 31000, 36250, 34590, 36510, 34580, 33960]
GREATER_SYDNEY_LGA_CODES = [18550, 13100, 14000, 16370, 18000, 14500, 17420, 13800, 10750, 16350, 10900, 14900, 18400, 16100, 11500, 11450, 17150, 10750, 12850,
                            13950, 16250, 10350, 16700, 14100, 14700, 18250, 15950, 15350, 15150, 10200, 11520, 14800, 17200, 18500, 18050, 16550, 11100, 16650,
                            14450, 14150, 17100, 11550, 11300, 10150, 15200]
GREATER_ADELAIDE_LGA_NAME = "Greater_Adelaide"
GREATER_MELBOURNE_LGA_NAME = "Greater_Melbourne"
GREATER_BRISBANE_LGA_NAME = "Greater_Brisbane"
GREATER_SYDNEY_LGA_NAME = "Greater_Sydney"

CODE_TO_NAME = {}

GREATER_AREA = {
    GREATER_ADELAIDE_LGA_NAME: GREATER_ADELAIDE_LGA_CODES,
    GREATER_MELBOURNE_LGA_NAME: GREATER_MELBOURNE_LGA_CODES,
    GREATER_BRISBANE_LGA_NAME: GREATER_BRISBANE_LGA_CODES,
    GREATER_SYDNEY_LGA_NAME: GREATER_SYDNEY_LGA_CODES,
}

for i, j in GREATER_AREA.items():
    for k in j:
        CODE_TO_NAME[k] = i


def parse_data(file_path: str, meta_path: str):
    attribute_info = {}
    with open(meta_path) as file:
        meta_data = json.load(file)

        # pprint(meta_data)

        for info in meta_data['selectedAttributes'][1:]:
            attribute_info[info['name']] = {'title': info['title'].replace("??? ", "").replace(" ", "_").replace("-", "_to_"),
                                            'description': info['description'].replace("??? ", "")}

    with open('result-meta.json', 'w') as outfile:
        json.dump(attribute_info, outfile)

    result = {
        GREATER_ADELAIDE_LGA_NAME: {"percentage_foreigner": 0},
        GREATER_MELBOURNE_LGA_NAME: {"percentage_foreigner": 0},
        GREATER_BRISBANE_LGA_NAME: {"percentage_foreigner": 0},
        GREATER_SYDNEY_LGA_NAME: {"percentage_foreigner": 0},
    }
    result_counted = {
        GREATER_ADELAIDE_LGA_NAME: 0,
        GREATER_MELBOURNE_LGA_NAME: 0,
        GREATER_BRISBANE_LGA_NAME: 0,
        GREATER_SYDNEY_LGA_NAME: 0,
    }
    with open(file_path) as file:
        json_data = json.load(file)

        for row in json_data['features']:

            lga = int(row['properties']['lga_code18'])
            if lga not in CODE_TO_NAME:
                continue
            area = CODE_TO_NAME[lga]
            result_counted[area] += 1

            # each column in the table
            for key, value in row['properties'].items():
                if key == "citizenship_status_p_brn_ovs_aus_citizen_pr100":
                    if value:
                        result[area]["percentage_foreigner"] += 100 - value

                else:
                    print("Warning: [unwanted key]", key, value)

            # row with error
            if not lga:
                print("Error: [row with empty lga]", str(row))
                continue

    for area in result:
        result[area]["percentage_foreigner"] /= result_counted[area]

    with open('result-' + file_path, 'w') as outfile:
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

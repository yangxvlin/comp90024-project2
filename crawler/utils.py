import os
import json

def load_configs():
    configs = [i for i in os.listdir("./") if 'config' in i]
    print(configs)
    res = []

    if len(configs) < 1:
        print("No config found")
        exit(1)

    for cf in configs:
        try:
            with open(cf, "r") as f:

                try:
                    config = json.load(f)
                except:
                    print('file', cf, 'not looks like a json file')
                    exit(1)

                if 'account' not in config:
                    print("account not found for file", cf)
                    exit(1)

                if 'search_words' not in config:
                    print("search word not found for file", cf)
                    exit(1)

                res.append(config)
        except IOError:
            print("please make sure you have config.json under the current path")
            exit(1)

    print("number of config found are", len(res))
    return res

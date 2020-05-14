"""
Author:      XuLin Yang
Student id:  904904
Date:        
Description: convert processed.json to processed.geojson
"""
import json

if __name__ == "__main__":
    with open("processed.json") as f:
        data = json.load(f)

        result = {"type": "FeatureCollection", "features": []}
        for tweet in data["tweets"]:
            feature = {"type": "Feature", "geometry": {}, "properties": {}}

            feature["geometry"] = {"type": "Point",
                                   "coordinates": tweet["geo"]}
            feature["properties"]["polarity"] = tweet["polarity"]
            feature["properties"]["subjectivity"] = tweet["subjectivity"]

            result["features"].append(feature)

        with open('processed.geojson', 'w') as fp:
            json.dump(result, fp)

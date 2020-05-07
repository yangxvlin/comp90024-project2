import json
import geopandas as god
from shapely.geometry import Polygon, shape
import geojsonio
import shapely

# with open("./ABS_LGA_2011_compressed_geojson.geojson") as f:
#     data = json.load(f)
#
# print(data['type'])
states = god.read_file('./ABS_LGA_2011_compressed_geojson.geojson')


# print(states.info())


#
# with open("./")
#
#
def check_lag(coordinates_):
    P = Polygon(coordinates_)
    point = P.centroid
    # print(point)
    for i in range(0, len(states)):
        if states['geometry'].iloc[i] is not None:
            polygon = shape(states['geometry'].iloc[i])
            # if type(polygon) is shapely.geometry.multipolygon.MultiPolygon:
            #     print(type(polygon))
            #     print(1)
            try:
                if polygon.contains(point):
                    # print(type(polygon))
                    print("=+++++++++++", i, "find")
                    return states['LGA_CODE11'].iloc[i], states['LGA_NAME11'].iloc[i], states['STE_NAME11'].iloc[i]
            except:
                print("========",i, "error")
                print("========",point, "point")
                print(polygon)


# LGA_CODE
# STATE_NAME
with open("../tweets/coronavirus-tweet-id-2020-03-01-00.jsonl") as f:
    for line in f:
        doc = json.loads(line)
        coordinates = doc['place']['bounding_box']['coordinates'][0]
        print(check_lag(coordinates))

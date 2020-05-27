import pandas as pd
import plotly.express as px
import json

polarity_lists = ["positive_pol", "neutral_pol", "negative_pol"]
subjectivity_list = ["subjective", "objective"]
geo = ["great_mel", "great_syd", "great_brisbane", "great_ald"]


def transform(data: pd.DataFrame):
    """
    transform the give data to accumulated version
    """

    positive_pol = (0.1 < data["polarity"]) & (data["polarity"] <= 1.0)
    neutral_pol = (-0.1 <= data["polarity"]) & (data["polarity"] <= 0.1)
    negative_pol = (-0.1 > data["polarity"]) & (data["polarity"] >= -1.0)

    # subjectivity
    subjective = (1 >= data['subjectivity']) & (data['subjectivity'] > 0.5)
    objective = (0.5 >= data['subjectivity']) & (data['subjectivity'] >= 0)

    new_df = pd.DataFrame(data={"polarity": [], "subjectivity": [], "size": [], "geo": []})

    for p in polarity_lists:
        for s in subjectivity_list:
            for g in geo:
                p_df = data[eval(p) & eval(s) & (data['geo'] == g)]
                tamp = pd.DataFrame(
                    data={"polarity": [p.split("_")[0]], "subjectivity": [s], "size": [len(p_df)], "geo": [g]})
                new_df = new_df.append(tamp, ignore_index=True)

    return new_df


def generate(new_data: pd.DataFrame, path="./"):
    for g in geo:
        pie_df = new_data[new_data['geo'] == g]
        fig = px.sunburst(pie_df, path=['geo', 'polarity', "subjectivity"],
                          values="size", color="size", color_continuous_scale='RdBu')

        fig.write_html(path + g + ".html")
        fig.write_image(path + g + ".svg")


def load_json_data(path):
    with open(path) as f:
        data_json = json.load(f)['df']

    geo_list = []
    pol_list = []
    sub_list= []

    for i in range(len(data_json['geo'])):
        geo_list.append(data_json['geo'][i])
        pol_list.append(data_json['polarity'][i])
        sub_list.append(data_json['subjectivity'][i])
    
    global geo
    geo = set(geo_list)

    return pd.DataFrame(data = {"polarity":pol_list, "subjectivity":sub_list,
        "geo":geo_list})


if __name__ == "__main__":
    data = load_json_data("2.json")
    # assign data here
    generate(transform(data))

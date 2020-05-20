import pandas as pd
import plotly.express as px

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


def generate(new_data: pd.DataFrame):
    for g in geo:
        pie_df = new_data[new_data['geo'] == g]
        fig = px.sunburst(pie_df, path=['geo', 'polarity', "subjectivity"],
                          values="size", color="size", color_continuous_scale='RdBu')

        fig.write_html("./" + g + ".html")
        fig.write_image("./" + g + ".svg")


if __name__ == "__main__":
    data = pd.read_csv("../sentiment-analysis/test.csv")
    generate(transform(data))

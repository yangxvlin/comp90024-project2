import React from "react";
import { Grid, Row, Col, Panel } from "rsuite";
import MultiBars from "./MultiBars";
import BarChart from "./BarChart";

export default class Scenario3 extends React.Component {
  constructor(props) {
    super(props);
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    this.state = {
      isLoading: true,
      url: props.data,
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muitiBarChartData1: muitiBarChartData1,
      muiltiLineChartData: muiltiLineChartData
    };
  }

  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    if (nextProps.data !== this.state.url) {
      this.state.url = nextProps.data;
      fetch(this.state.url)
        .then(function(res) {
          if (res.status >= 400) {
            alert("Bad response from server: " + res.status);
            throw new Error("Bad response from server");
          }
          return res.json();
        })
        .then(data => {
          console.log(data);
          barChartData = data.barChart_city_foreigner;
          muitiBarChartData1 =
            data.education_level_per_100_axis_by_education_level_legend_by_lga
              .multiBarChart_education_level_per_100_axis_by_education_level_legend_by_lga;
          muitiBarChartData =
            data.twitter_word_len_axis_by_lga_legend_by_len_type
              .multiBarChart_twitter_word_len_axis_by_short_medium_long_legend_by_lga;
          muiltiLineChartData = data.english_tweet_percentage.lineChart;
          this.setState({
            barChartData: barChartData,
            muitiBarChartData: muitiBarChartData,
            muitiBarChartData1: muitiBarChartData1,
            muiltiLineChartData: muiltiLineChartData,
            isLoading: false
          });
          console.log(this.state.muitiBarChartData1);
        })
        .then(
          res => {
            if (res.ok) {
              console.log("ok");
            } else {
              console.log("error");
            }
            console.log(res.json());
          },
          err => {
            console.log(err);
          }
        )
        .then(
          data => {
            console.log(data);
          },
          err => {
            console.log(err);
          }
        );
    }
  }

  componentDidMount() {
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    fetch(this.state.url)
      .then(function(res) {
        if (res.status >= 400) {
          alert("Bad response from server: " + res.status);
          throw new Error("Bad response from server");
        }
        return res.json();
      })
      .then(data => {
        console.log(data);
        barChartData = data.barChart_city_foreigner;
        muitiBarChartData1 =
          data.education_level_per_100_axis_by_education_level_legend_by_lga
            .multiBarChart_education_level_per_100_axis_by_education_level_legend_by_lga;
        muitiBarChartData =
          data.twitter_word_len_axis_by_lga_legend_by_len_type
            .multiBarChart_twitter_word_len_axis_by_short_medium_long_legend_by_lga;
        muiltiLineChartData = data.english_tweet_percentage.lineChart;
        this.setState({
          barChartData: barChartData,
          muitiBarChartData: muitiBarChartData,
          muitiBarChartData1: muitiBarChartData1,
          muiltiLineChartData: muiltiLineChartData,
          isLoading: false
        });
        console.log(this.state.muitiBarChartData1);
      })
      .then(
        res => {
          if (res.ok) {
            console.log("ok");
          } else {
            console.log("error");
          }
          console.log(res.json());
        },
        err => {
          console.log(err);
        }
      )
      .then(
        data => {
          console.log(data);
        },
        err => {
          console.log(err);
        }
      );
  }

  render() {
    return this.state.isLoading ? (
      "loading"
    ) : (
      <Grid fluid>
        <Row className="show-grid" gutter={30}>
          {this.state.barChartData.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <BarChart data={item} title={item.title} />
                </Panel>
              </Col>
            );
          })}
          {
            <Col md={12} sm={12}>
              <Panel shaded bordered expanded>
                <MultiBars
                  width="100%"
                  height="100%"
                  type="line"
                  data={this.state.muiltiLineChartData}
                  title="English tweet(%)"
                />
              </Panel>
            </Col>
          }
        </Row>

        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                width="100%"
                height="100%"
                type="column"
                data={this.state.muitiBarChartData}
                title="Twitter word by length"
              />
            </Panel>
          </Col>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                width="100%"
                height="100%"
                type="column"
                data={this.state.muitiBarChartData1}
                title="Education by city"
              />
            </Panel>
          </Col>
        </Row>
      </Grid>
    );
  }
}

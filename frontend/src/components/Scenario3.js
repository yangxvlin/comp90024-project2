import React from "react";
//import CanvasJSReact from "../assets/canvasjs.react";
//import LineChart from "./LineChart";
import PieChart from "./PieChart";
//import Paraluna from "./Paraluna";
import scenario3 from "../testData/scenario3.json";
import { Grid, Row, Col, Panel } from "rsuite";
import MultiLines from "./MultiLines";
import MultiBars from "./MultiBars";
import BarChart from "./BarChart";

export default class Scenario3 extends React.Component {
  constructor(props) {
    super(props);
    console.log(this.props.match.params.url + this.props.location.search);
    var url = this.props.match.params.url + this.props.location.search;
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    this.state = {
      isLoading: true,
      url: url,
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muitiBarChartData1: muitiBarChartData1,
      muiltiLineChartData: muiltiLineChartData
    };

    //  this.fetchData();
  }

  componentWillMount() {
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;
    fetch("http://172.26.131.223/" + "scenario3?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&year_start=2020&month_start=2&year_end=2020&month_end=5")//this.state.url)
      .then(res => res.json())
      .then(data => {
     //   var data = scenario3;
        console.log(data);
        barChartData = data.barChart_city_foreigner;
        muitiBarChartData1 = data.education_level_per_100_axis_by_education_level_legend_by_lga.multiBarChart_education_level_per_100_axis_by_education_level_legend_by_lga;
        muitiBarChartData =
          data.twitter_word_len_axis_by_lga_legend_by_len_type
            .multiBarChart_twitter_word_len_axis_by_short_medium_long_legend_by_lga;
        muiltiLineChartData = data.english_tweet_percentage.lineChart;
        this.setState({
          barChartData: barChartData,
          muitiBarChartData: muitiBarChartData,
          muitiBarChartData1:muitiBarChartData1,
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
            alert("error")
          }
          console.log(res.json());
        },
        err => {
          console.log(err);
          alert("error")
        }
      )
      .then(
        data => {
          console.log(data);
        },
        err => {
          console.log(err);
          alert("error")
        }
      );
  }

  render() {
    return this.state.isLoading ? (
      "loading"
    ) : (
      <Grid fluid >
        <Row className="show-grid" gutter={30}>
          {this.state.barChartData.map(item => {
            return (
              <Col md={12} sm={12} >
                <Panel shaded bordered expanded>
                  <BarChart data={item} title={item.title} />
                </Panel>
              </Col>
            );
          })}
          {
            <Col md={12} sm={12}>
              <Panel shaded bordered expanded>
                <MultiBars width='100%' height='100%'
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
              <MultiBars width='100%' height='100%'
                type="column"
                data={this.state.muitiBarChartData}
                title="Twitter word by length"
              />
            </Panel>
          </Col>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars width='100%' height='100%'
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

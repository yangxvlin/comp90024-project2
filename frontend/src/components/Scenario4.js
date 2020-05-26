import React from "react";
import { Grid, Row, Col, Panel } from "rsuite";
import MultiBars from "./MultiBars";
import BarChart from "./BarChart";

export default class Scenario4 extends React.Component {
  constructor(props) {
    super(props);
    var barChartData;
    var barChartData1;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;
    var muiltiLineChartData1;

    this.state = {
      isLoading: true,
      url: props.data,
      barChartData: barChartData,
      barChartData1: barChartData1,
      muitiBarChartData: muitiBarChartData,
      muitiBarChartData1: muitiBarChartData1,
      muiltiLineChartData: muiltiLineChartData,
      muiltiLineChartData1: muiltiLineChartData1
    };

  }

  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);
    var barChartData;
    var barChartData1;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;
    var muiltiLineChartData1;
    if (nextProps.data !== this.state.url) {
      this.state.url = nextProps.data;
      fetch(this.state.url) //+ "scenario4?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&income=0,3,7,8,9,12,13,15&year_start=2020&month_start=2&day_start=1&year_end=2020&month_end=5&day_end=10")//this.state.url)
        .then(function(res) {
          if (res.status >= 400) {
            alert("Bad response from server: " + res.status);
            throw new Error("Bad response from server");
          }
          return res.json();
        })
        .then(data => {
          console.log(data);
          barChartData = data.barChart_gp_per_persion;
          barChartData1 = data.barChart_hospital_per_person;
          muitiBarChartData =
            data.income_axis_by_lga_selected_legend_by_selected_income_group
              .multiBarChart_income_by_lga_by_group;

          muitiBarChartData1 =
            data.income_axis_by_selected_income_group_legend_by_lga_selected
              .multiBarChart_income_by_group_by_lga;
          muiltiLineChartData = data.state_covid_count.lineChart;
          muiltiLineChartData1 = data.covid_related_twitter_count.lineChart;
          this.setState({
            barChartData: barChartData,
            barChartData1: barChartData1,
            muitiBarChartData: muitiBarChartData,
            muitiBarChartData1: muitiBarChartData1,
            muiltiLineChartData: muiltiLineChartData,
            muiltiLineChartData1: muiltiLineChartData1,
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
    var barChartData1;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;
    var muiltiLineChartData1;
    fetch(this.state.url) //+ "scenario4?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&income=0,3,7,8,9,12,13,15&year_start=2020&month_start=2&day_start=1&year_end=2020&month_end=5&day_end=10")//this.state.url)
      .then(function(res) {
        if (res.status >= 400) {
          alert("Bad response from server: " + res.status);
          throw new Error("Bad response from server");
        }
        return res.json();
      })
      .then(data => {
        console.log(data);
        barChartData = data.barChart_gp_per_persion;
        barChartData1 = data.barChart_hospital_per_person;
        muitiBarChartData =
          data.income_axis_by_lga_selected_legend_by_selected_income_group
            .multiBarChart_income_by_lga_by_group;

        muitiBarChartData1 =
          data.income_axis_by_selected_income_group_legend_by_lga_selected
            .multiBarChart_income_by_group_by_lga;
        muiltiLineChartData = data.state_covid_count.lineChart;
        muiltiLineChartData1 = data.covid_related_twitter_count.lineChart;
        this.setState({
          barChartData: barChartData,
          barChartData1: barChartData1,
          muitiBarChartData: muitiBarChartData,
          muitiBarChartData1: muitiBarChartData1,
          muiltiLineChartData: muiltiLineChartData,
          muiltiLineChartData1: muiltiLineChartData1,
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
          {this.state.barChartData1.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <BarChart data={item} title={item.title} />
                </Panel>
              </Col>
            );
          })}
        </Row>

        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                type="line"
                data={this.state.muiltiLineChartData1}
                title="Covid19 related tweets per state"
              />
            </Panel>
          </Col>
          {
            <Col md={12} sm={12}>
              <Panel shaded bordered expanded>
                <MultiBars
                  type="line"
                  data={this.state.muiltiLineChartData}
                  title="Covid19 per state"
                />
              </Panel>
            </Col>
          }
        </Row>
        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                type="column"
                data={this.state.muitiBarChartData1}
                title="City by income group"
              />
            </Panel>
          </Col>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                type="column"
                data={this.state.muitiBarChartData}
                title="Income by city"
              />
            </Panel>
          </Col>
        </Row>
      </Grid>
    );
  }
}

import React from "react";
import PieChart from "./PieChart";
import fetch from 'fetch-with-proxy';

import { Grid, Row, Col, Panel } from "rsuite";
import MultiLines from "./MultiLines";
import MultiBars from "./MultiBars";
import BarChart from "./BarChart";

export default class Diagrams extends React.Component {
  constructor(props) {
    super(props);
    var pieChartData;
    var barChartData;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    this.state = {
      isLoading: true,
      url: props.data,
      pieChartData: pieChartData,
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muitiBarChartData1: muitiBarChartData1,
      muiltiLineChartData: muiltiLineChartData
    };

  }


  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);
    var pieChartData;
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
        pieChartData = data.pie_charts_for_each_city_all_age_groups.pieChart;
        barChartData = data.barChart_total_pop;
        muitiBarChartData =
          data.population_age_axis_by_selected_age_group_legend_by_lga_selected
            .multiBarChart_age_by_group_by_lga;
        muitiBarChartData1 =
          data.population_age_axis_by_lga_selected_legend_by_selected_age_group
            .multiBarChart_age_by_lga_by_group;
        muiltiLineChartData = data.twitter_daily_time_line_chart.lineChart;
        this.setState({
          pieChartData: pieChartData,
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
    var pieChartData;
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
        pieChartData = data.pie_charts_for_each_city_all_age_groups.pieChart;
        barChartData = data.barChart_total_pop;
        muitiBarChartData =
          data.population_age_axis_by_selected_age_group_legend_by_lga_selected
            .multiBarChart_age_by_group_by_lga;
        muitiBarChartData1 =
          data.population_age_axis_by_lga_selected_legend_by_selected_age_group
            .multiBarChart_age_by_lga_by_group;
        muiltiLineChartData = data.twitter_daily_time_line_chart.lineChart;
        this.setState({
          pieChartData: pieChartData,
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
      <Grid fluid width={window.innerWidth} height={window.innerHeight}>
        <Row className="show-grid" gutter={30}>
          {this.state.barChartData.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <BarChart data={item} title="Total Population" />
                </Panel>
              </Col>
            );
          })}
          {
            <Col md={12} sm={12}>
              <Panel shaded bordered expanded>
                <MultiLines
                  type="line"
                  data={this.state.muiltiLineChartData}
                  title="Twitter Daily Time"
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
                data={this.state.muitiBarChartData}
                title="Age Group by city"
              />
            </Panel>
          </Col>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                type="column"
                data={this.state.muitiBarChartData1}
                title="City by Age Group"
              />
            </Panel>
          </Col>
        </Row>
        <Row className="show-grid" gutter={30}>
          {this.state.pieChartData.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <PieChart data={item} />
                </Panel>
              </Col>
            );
          })}
        </Row>
      </Grid>
    );
  }
}

import React from "react";
import ReactWordcloud from "react-wordcloud";
import { Grid, Row, Col, Panel } from "rsuite";
import MultiBars from "./MultiBars";
import BarChart from "./BarChart";


export default class Scenario5 extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);

    var barChartData;
    var barChartData1;
    var muitiBarChartData;
    var muitiBarChartData1;
    var muiltiLineChartData;

    this.state = {
      isLoading: true,
      url: props.data,
      barChartData: barChartData,
      barChartData1: barChartData1,
      muitiBarChartData: muitiBarChartData,
      muitiBarChartData1: muitiBarChartData1,
      muiltiLineChartData: muiltiLineChartData
    };
   
  }


  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);

    if (nextProps.data !== this.state.url) {
      this.setState({
        url: nextProps.data
      });
      var barChartData;
      var barChartData1;
      var muitiBarChartData;
  
        fetch(nextProps.data)
        .then(function(res) {
          if (res.status >= 400) {
            alert("Bad response from server: " + res.status);
            throw new Error("Bad response from server");
          }
          return res.json();
        })
        .then(data => {
          console.log(data);
          barChartData = data.barChart_psychological_distress_by_lga;
          barChartData1 = data.emotion_word_count_by_city;
          muitiBarChartData =
            data.chart_emotion_word_count_by_city
              .multiBarChart_emotion_word_count_by_city;
          console.log(barChartData1.word_cloud);
         
          this.setState({
            barChartData: barChartData,
            barChartData1: barChartData1.word_cloud,
            word_cloud2: barChartData1.word_cloud[0],
            word_cloud3: barChartData1.word_cloud[2],
            word_cloud4: barChartData1.word_cloud[3],
            muitiBarChartData: muitiBarChartData,
            isLoading: false
          });
          console.log(this.state.barChartData);
          this.forceUpdate();
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
        barChartData = data.barChart_psychological_distress_by_lga;
        barChartData1 = data.emotion_word_count_by_city;
        muitiBarChartData =
          data.chart_emotion_word_count_by_city
            .multiBarChart_emotion_word_count_by_city;
        console.log(barChartData1.word_cloud);
       
        this.setState({
          barChartData: barChartData,
          barChartData1: barChartData1.word_cloud,
          word_cloud2: barChartData1.word_cloud[0],
          word_cloud3: barChartData1.word_cloud[2],
          word_cloud4: barChartData1.word_cloud[3],
          muitiBarChartData: muitiBarChartData,
          isLoading: false
        });
        console.log(this.state.barChartData);
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
          {" "}
          {this.state.barChartData.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel shaded bordered expanded>
                  <BarChart data={item} title={item.title} />{" "}
                </Panel>{" "}
              </Col>
            );
          })}{" "}
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <MultiBars
                type="column"
                data={this.state.muitiBarChartData}
                title="Emotion word count by city"
              />
            </Panel>{" "}
          </Col>{" "}
        </Row>{" "}
        <Row className="show-grid" gutter={30}></Row>{" "}
        <Row className="show-grid" gutter={30}>
          {this.state.barChartData1.map(item => {
            return (
              <Col md={12} sm={12}>
                <Panel
                  shaded
                  bordered
                  expanded
                  header={`${item.title}` + "'s emotion: log(count)"}
                >
                  <div style={{ height: 400, width: 600 }} title="">
                    <ReactWordcloud words={item.data} />{" "}
                  </div>{" "}
                </Panel>
              </Col>
            );
          })}
        </Row>{" "}
      </Grid>
    );
  }
}

import React from "react";
//import CanvasJSReact from "../assets/canvasjs.react";
//import LineChart from "./LineChart";
import PieChart from "./PieChart";
//import Paraluna from "./Paraluna";
import great_brisbane from "../testData/great_brisbane.svg";
import great_mel from "../testData/great_mel.svg";
import { ReactComponent as Brisbane } from "../scenario2/great_brisbane.svg";
import { ReactComponent as Melbourne } from "../scenario2/great_mel.svg";
import { ReactComponent as Ald } from "../scenario2/great_ald.svg";
import { ReactComponent as Syd } from "../scenario2/great_syd.svg";
import { Grid, Row, Col, Panel, Icon } from "rsuite";
import MultiLines from "./MultiLines";
import MultiBars from "./MultiBars";
//import aldhtml from "../scenario2/great_ald.html";
//var htmlDoc1 = {__html: aldhtml};

export default class Scenario2 extends React.Component {
  constructor(props) {
    super(props);
    console.log(this.props.match.params.url + this.props.location.search);
    var url = this.props.match.params.url + this.props.location.search;
    var barChartData;
    var muitiBarChartData;
    var muiltiLineChartData;
    console.log(great_brisbane);
    this.state = {
      isLoading: true,
      url: url,
      __html: "",
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muiltiLineChartData: muiltiLineChartData
    };

    //  this.fetchData();
  }
  componentWillMount() {
    // fetch the HTML fragment with a local API request
    fetch()
      .then(resp => {
        // fetch returns a readable stream, so translate it into stringified HTML
        return resp.text();
      })
      .then(content => {
        // dangerouslySetInnerHTML requires using an object with an `__html` key
        this.setState({
          __html: content
        });
      })
      .catch(err => {
        // handle the error
      });
  }
  render() {
    return (
      <Grid fluid>
        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <Brisbane
                width="100%"
                height="100%"
                onClick={() => {
                  window.open(
                    "http://172.26.131.223/scenario2_brisbane",
                    "_blank"
                  );
                }}
              />
              {
                // <button onClick={()=>{window.open("http://172.26.131.223/scenario2_brisbane", "_blank")}}>Brisbane</button>
              }
            </Panel>
          </Col>

          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
              <Melbourne
                width="100%"
                height="100%"
                onClick={() => {
                  window.open("http://172.26.131.223/scenario2_mel", "_blank");
                }}
              />
            </Panel>
          </Col>
        </Row>
        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel
              shaded
              bordered
              expanded
              onClick={() => {
                window.open("http://172.26.131.223/scenario2_syd", "_blank");
              }}
            >
              <Syd width="100%" height="100%" />
            </Panel>
          </Col>

          <Col md={12} sm={12}>
            <Panel
              shaded
              bordered
              expanded
              onClick={() => {
                window.open("http://172.26.131.223/scenario2_ald", "_blank");
              }}
            >
              <Ald width="100%" height="100%" />
            </Panel>
          </Col>
        </Row>
      </Grid>
    );
  }
}

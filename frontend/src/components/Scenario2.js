import React from "react";
import great_brisbane from "../testData/great_brisbane.svg";
import { ReactComponent as Brisbane } from "../scenario2/Greater_Brisbane.svg";
import { ReactComponent as Melbourne } from "../scenario2/Greater_Melbourne.svg";
import { ReactComponent as Ald } from "../scenario2/Greater_Adelaide.svg";
import { ReactComponent as Syd } from "../scenario2/Greater_Sydney.svg";
import { Grid, Row, Col, Panel } from "rsuite";

export default class Scenario2 extends React.Component {
  constructor(props) {
    super(props);
    var barChartData;
    var muitiBarChartData;
    var muiltiLineChartData;
    console.log(great_brisbane);
    this.state = {
      isLoading: true,
   //   url: url,
      __html: "",
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muiltiLineChartData: muiltiLineChartData
    };

  }
  componentWillMount() {
    fetch()
      .then(resp => {
        return resp.text();
      })
      .then(content => {
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

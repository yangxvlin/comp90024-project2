import React from "react";
//import CanvasJSReact from "../assets/canvasjs.react";
//import LineChart from "./LineChart";
import PieChart from "./PieChart";
//import Paraluna from "./Paraluna";
import great_brisbane from "../testData/great_brisbane.svg";
import great_mel from "../testData/great_mel.svg";
import { ReactComponent as Brisbane } from "../testData/great_brisbane.svg";
import { ReactComponent as Melbourne } from "../testData/great_mel.svg";
import { Grid, Row, Col, Panel, Icon } from "rsuite";
import MultiLines from "./MultiLines";
import MultiBars from "./MultiBars";

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
      barChartData: barChartData,
      muitiBarChartData: muitiBarChartData,
      muiltiLineChartData: muiltiLineChartData
    };

    //  this.fetchData();
  }

  render() {
    return (
      <Grid fluid>
        <Row className="show-grid" gutter={30}>
          <Col md={12} sm={12}>
            <Panel shaded bordered expanded >
             <Brisbane width='100%' height='100%'/>
            </Panel>
          </Col>

          <Col md={12} sm={12}>
            <Panel shaded bordered expanded>
            <Melbourne width='100%'  height='100%'/>
            </Panel>
          </Col>
        </Row>
      </Grid>
    );
  }
}

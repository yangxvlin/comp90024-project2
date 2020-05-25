import React from "react";
import CanvasJSReact from "../assets/canvasjs.react";
//import { Grid, Row, Col, Panel } from "rsuite";
//import data from "../testData/data.json";

//var CanvasJSReact = require('./canvasjs.react');
//var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class BarChart extends React.Component {
  constructor(props) {
    super(props);
    var datas = [];
    var data = props.data.data;
    console.log(data);
    this.state = {
      title: props.title,
      data: data,
      showData: datas
    };
    for (var i = 0; i < data.length; i++) {
    console.log(data[i].lable);
    datas.push({
      label: data[i].x,
        y: data[i].y,
      });
      
    }
    console.log(this.state.showData);
  }

 

  render() {
    const options = {
			title: {
				text: this.state.title
      },
      axisX: {
        valueFormatString: "#,###"
      },
			data: [
			{
				// Change type to "doughnut", "line", "splineArea", etc.
        type: "column",
        xValueFormatString: "##",
				yValueFormatString: "#,###",
				dataPoints: this.state.showData
			}
			]
		    
    };

    return (
     
        <CanvasJSChart options={options} onRef={ref => (this.chart = ref)}  style={{width:100}}/>
      
    );
  }
}

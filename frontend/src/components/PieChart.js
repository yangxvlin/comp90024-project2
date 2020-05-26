import React from "react";
import CanvasJSReact from "../assets/canvasjs.react";
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class PieChart extends React.Component {
  constructor(props) {
    super(props);
    console.log(props.data);
    var showData = [];
    var sum;
    var data = props.data.data;
   
    for (var i = 0; i < data.length; i++) {
            showData.push({
               name: data[i].name,
               y: data[i].y,
             });
    }



    this.state = {
      title: props.data.title,
      data: showData,
      sum: sum
    };
  }
  render() {
    const options = {
      animationEnabled: true,
      title: {
        text: this.state.title
      },
      axisX: {
				title: "Apps",
      },
      subtitles: [
        {
          text: "Age Group",
          verticalAlign: "center",
          fontSize: 22,
          dockInsidePlotArea: true
        }
      ],
      data: [
        {
          type: "doughnut",
          showInLegend: true,
          indexLabel: "{name}: {y}",
          yValueFormatString: "#,###",
          dataPoints: 
            this.state.data
        }
      ]
    };
    return (
          <CanvasJSChart options={options} width='100%' height='100%'/>
    );
  }
}

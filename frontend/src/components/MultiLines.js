import React from "react";
import CanvasJSReact from "../assets/canvasjs.react";
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class MultiLines extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.state = {
      data: props.data,
      type: props.type,
      title: props.title,
      showData: []
    };

    var data = props.data;
    for (var i = 0; i < data.length; i++) {
      var dataPoints = [];
      for (var j = 0; j < data[i].data.length; j++) {
        console.log(data[i].data[j].x);
        dataPoints.push({
          x: data[i].data[j].x,
          y: data[i].data[j].y
        });
      }
      this.state.showData.push({
        type: "line",
        name: data[i].title,
        showInLegend: true,
        xValueFormatString: "Time: ##",
        yValueFormatString: "#,###",
        dataPoints: dataPoints
      });
    }

    this.toggleDataSeries = this.toggleDataSeries.bind(this);
    this.addSymbols = this.addSymbols.bind(this);
  }

  UNSAFE_componentWillUpdate(nextProps, nextState) {
    console.log(nextProps);
    
    if(nextProps.data !== this.state.data){
      var data = nextProps.data;
      this.state.showData = [];
         for (var i = 0; i < data.length; i++) {
           var dataPoints = [];
           for (var j = 0; j < data[i].data.length; j++) {
             dataPoints.push({
               label: data[i].data[j].x,
               y: data[i].data[j].y
             });
           }
           this.state.showData.push({
             type: "line",
             name: data[i].title,
             showInLegend: true,
             xValueFormatString: "#",
             yValueFormatString: "#,###,###",
             dataPoints: dataPoints
           })
         }

    }
  }


  addSymbols(e) {
    var suffixes = ["", "K", "M", "B"];
    var order = Math.max(Math.floor(Math.log(e.value) / Math.log(1000)), 0);
    if (order > suffixes.length - 1) order = suffixes.length - 1;
    var suffix = suffixes[order];
    return CanvasJS.formatNumber(e.value / Math.pow(1000, order)) + suffix;
  }
  toggleDataSeries(e) {
    if (typeof e.dataSeries.visible === "undefined" || e.dataSeries.visible) {
      e.dataSeries.visible = false;
    } else {
      e.dataSeries.visible = true;
    }
    this.chart.render();
  }
  render() {
    const options = {
      animationEnabled: true,
      colorSet: "colorSet2",
      title: {
        text: this.state.title
      },
      axisX: {
        valueFormatString: "##"
      },
      axisY: {
        prefix: "",
        labelFormatter: this.addSymbols
      },
      toolTip: {
        shared: true
      },
      legend: {
        cursor: "pointer",
        itemclick: this.toggleDataSeries,
        verticalAlign: "top"
      },
      data: this.state.showData
    };
    return (
      <div>
        <CanvasJSChart
          options={options}
          onRef={ref => (this.chart = ref)}
          width="100%"
          height="100%"
        />
        {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
      </div>
    );
  }
}

import React from "react";
import CanvasJSReact from "../assets/canvasjs.react";
//import { Grid, Row, Col, Panel } from "rsuite";

//var CanvasJSReact = require('./canvasjs.react');
//var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class PieChart extends React.Component {
  constructor(props) {
    super(props);
    console.log(props.data);
    var showData = [];
    var sum;
    var data = props.data.data;
   
    for (var i = 0; i < data.length; i++) {
       //    console.log(data[i]);
         //  var dataPoints = [];
        //   for (var j = 0; j < 7; j++) {
            showData.push({
               name: data[i].name,
               y: data[i].y,
             });
            
          //   console.log(showData);
      //     }
    }

    
    /*
    var sum =
      (data.People_aged_0_to_4_years_count) +
      (data.People_aged_5_to_9_years_count) +
      (data.People_aged_10_to_14_years_count) +
      (data.People_aged_15_to_19_years_count) +
      (data.People_aged_20_to_24_years_count) +
      (data.People_aged_25_to_29_years_count) +
      (data.People_aged_30_to_34_years_count) +
      (data.People_aged_35_to_39_years_count) +
      (data.People_aged_40_to_44_years_count) +
      (data.People_aged_45_to_49_years_count) +
      (data.People_aged_50_to_54_years_count) +
      (data.People_aged_55_to_59_years_count) +
      (data.People_aged_60_to_64_years_count) +
      (data.People_aged_65_to_69_years_count) +
      (data.People_aged_70_to_74_years_count) +
      (data.People_aged_75_to_79_years_count) +
      (data.People_aged_80_to_84_years_count) +
      (data.People_aged_85_years_and_over_count);
      console.log(sum);

    
    showData.push({
      name: "0-4",
      y: data.People_aged_0_to_4_years_count
    });
    showData.push({
      name: "5-9",
      y: data.People_aged_5_to_9_years_count
    });
    showData.push({
      name: "10-14",
      y: data.People_aged_10_to_14_years_count
    })
    showData.push({
      name: "Age group: 15-19",
      y: data.People_aged_15_to_19_years_count
    });
    showData.push({
      name: "Age group: 20-24",
      y: data.People_aged_20_to_24_years_count
    });
    showData.push({
      name: "Age group: 25-29",
      y: data.People_aged_25_to_29_years_count
    })
    showData.push({
      name: "Age group: 30-34",
      y: data.People_aged_30_to_34_years_count
    });
    showData.push({
      name: "Age group: 35-39",
      y: data.People_aged_35_to_39_years_count
    });
    showData.push({
      name: "Age group: 40-44",
      y: data.People_aged_40_to_44_years_count
    })
    showData.push({
      name: "Age group: 45-49",
      y: data.People_aged_45_to_49_years_count
    });
    showData.push({
      name: "Age group: 50-54",
      y: data.People_aged_50_to_54_years_count
    });
    showData.push({
      name: "Age group: 55-59",
      y: data.People_aged_55_to_59_years_count
    })
    showData.push({
      name: "Age group: 60-64",
      y: data.People_aged_60_to_64_years_count
    });
    showData.push({
      name: "Age group: 65-69",
      y: data.People_aged_65_to_69_years_count
    });
    showData.push({
      name: "Age group: 70-74",
      y: data.People_aged_70_to_74_years_count
    })
    showData.push({
      name: "Age group: 75-79",
      y: data.People_aged_75_to_79_years_count
    });
    showData.push({
      name: "Age group: 80-84",
      y: data.People_aged_80_to_84_years_count
    });
    showData.push({
      name: "Age group: above 85 ",
      y: data.People_aged_85_years_and_over_count
    })
   */

    this.state = {
      title: props.data.title,
      data: showData,
      sum: sum
 /*     Adelaide: parseInt(props.data._0_4_yrs_proj_count.Adelaide),
      Brisbane: parseInt(props.data._0_4_yrs_proj_count.Brisbane),
      Melbourne: parseInt(props.data._0_4_yrs_proj_count.Melbourne),
      Sydney: parseInt(props.data._0_4_yrs_proj_count.Sydney),
      sum: sum*/
    };
  //  console.log(this.state.data.People_aged_0_4_years_count);
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
          /*  {
              name: this.state.title,
              y: this.state.Adelaide*100/this.state.sum
            },
            { name: "Brisbane", y: this.state.Brisbane*100/this.state.sum },
            { name: "Melbourne", y: this.state.Melbourne*100/this.state.sum},
            { name: "Sydney", y: this.state.Sydney*100/this.state.sum }
            //     { name: "Neutral", y: 7 }*/
          
        }
      ]
    };
    return (
          <CanvasJSChart options={options} width='100%' height='100%'/>
    );
  }
}

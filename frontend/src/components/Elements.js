import React from "react";
import comparisonMenu from "../testData/comparisonMenu.json";
import scenario1 from "../testData/s1.json";
import {
  TagPicker,
  SelectPicker,
  InputNumber,
  Button
} from "rsuite";
import Diagrams from "./Diagrams.js";

export default class Elements extends React.Component {
  constructor(props) {
    super(props);
    //  console.log(comparisonMenu[2]);
    // 默认Alert隐藏
    this.state = {
      visible: false,
      url:"",
      data:[],
      scena: "",
      lga: "",
      weekday: "",
      age_group: "",
      daytime_start: 0,
      endtime: 24,
      scenario: comparisonMenu[0].level_1,
      city: comparisonMenu[1].city,
      week: comparisonMenu[2].week,
      community: comparisonMenu[3].age_group
    };

    this.clickSubmit = this.clickSubmit.bind(this);
    this.onChange = this.onChange.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);
  }

  handleUpdate() {
    if (this.state.community.length === 0) {
      setTimeout(() => {
        //   this.setState({ community: topic[this.state.topicId].community });
      }, 1000);
    }
  }


  clickSubmit(e) {
    //    e.preventDefault();
    var scena = this.state.scena;
    var lga = this.state.lga;
    var weekday = this.state.weekday;
    var age_group = this.state.age_group;
    var daytime_start = this.state.daytime_start;
    var endtime = this.state.endtime;
    var url =
      "scenario" +
      scena +
      "?&lga=" +
      lga +
      "&weekday=" +
      weekday +
      "&daytime_start=" +
      daytime_start +
      "&daytime_end=" +
      endtime +
      "&age_group=" +
      age_group;
    console.log(url);

 //   this.props.handleEmail = scenario1;
    this.setState({
      url: url,
      data: scenario1
  })
  // 触发回调 传递给父组件
  this.props.getChildrenMsg(url);
 
/*
    
    fetch(
      "http://172.26.132.122:5000/"+url
    )
      .then(res => res.json())
      .then(data => {
        console.log(data);
      //  this.props.getChildrenMsg(data);
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
*/
    // alert(e);
    if (this.state.visible) {
      // Alert隐藏
      this.setState({ visible: false });
    } else {
      // Alert显示
      this.setState({ visible: true });
    }
  //  return (render(<Diagrams data={this.state.url}/>));
  }

  handleChange(value) {
    console.log(value);

    this.setState({
      value1: value
    });
  }

  onChange(value, item, event) {
    //  console.log(event + value + item.topic);
    this.setState({ topicId: parseInt(value) - 1 });
    this.setState({ value1: "--- Please choosing community here ---" });
    //  this.setState({community: topic[parseInt(value)-1].community});
    //   console.log(topic[parseInt(value)-1].community)
    //   console.log(Object.keys(topic[parseInt(value)-1].community))
    // console.log(Object.keys(topic))
  }

  onChoose(value, item, event) {
    /*    console.log(event + value + item);
    this.setState({
        value1: item.community
      });
    console.log(item.community);
   // this.state.value1 = item.community;
    console.log(this.state.value1)*/
  }

  render() {
    return (
      <div>
        
          <div style={{ align: "center", width: 250 }}>
            <SelectPicker
              data={this.state.scenario}
              style={{ width: 250 }}
              onSelect={item => {
                this.setState({ scena: item });
              }}
              appearance="default"
              searchable={false}
              placeholder="--- Please choose topic here ---"
            ></SelectPicker>
            <br />
            <br />
            <TagPicker
              data={this.state.city}
              appearance="subtle"
              style={{ width: 250 }}
              menuStyle={{ width: 250 }}
              onSelect={item => {
                this.setState({ lga: item });
              }}
              placeholder="--- Please choose cities here ---"
            />
            <br />
            <br />
            <TagPicker
              data={this.state.community}
              appearance="subtle"
              style={{ width: 250 }}
              menuStyle={{ width: 250 }}
              onSelect={item => {
                this.setState({ age_group: item });
              }}
              placeholder="--- Please choose community here ---"
            />
            <br />
            <br />
            <SelectPicker
              data={this.state.week}
              style={{ width: 250 }}
              appearance="default"
              searchable={false}
              onSelect={item => {
                this.setState({ weekday: item });
              }}
              placeholder="--- Please choose a day here ---"
            />
            <br />
            <br />
            <div>
              <InputNumber
                prefix="StartTime"
                onChange={item => {
                  this.setState({ daytime_start: item });
                  if (parseInt(item) !== 0) {
                    if (parseInt(item) !== 24)
                      this.setState({ endtime: parseInt(item) });
                    else this.setState({ endtime: 0 });
                  } else {
                    this.setState({ endtime: 24 });
                  }
                }}
                defaultValue={0}
                max={24}
                min={0}
                //  style={{ width: 150 }} }
              />
              <hr />
              <p>EndTime: {this.state.endtime}</p>
              <p></p>
            </div>
            <hr />
            <Button appearance="primary" onClick={this.clickSubmit}
             //href={"/comparison/"+`${this.state.url}`}> 
             href={"/comparison/"+`${this.state.url}`}
            >
              Submit
            </Button>
            <Button
              color="red"
              appearance="ghost"
              onClick={() => {
                this.render();
              }}
            >
              Cancel
            </Button>
          </div>
          <div>{this.state.visible ? <p>You can see me.</p> : null}</div>
      </div>
    );
  }
}

import React from "react";
import comparisonMenu from "../testData/comparisonMenu.json";
import scenario1 from "../testData/s1.json";

import { TagPicker, SelectPicker, InputNumber, Button } from "rsuite";

export default class Elements extends React.Component {
  constructor(props) {
    super(props);
    console.log(comparisonMenu);
    // 默认Alert隐藏
    this.state = {
      visible: false,
      url: "",
      data: [],
      scena: "0",
      lga: "",
      weekday: "",
      age_group: "",
      daytime_start: 0,
      endtime: 24,
      month_start: "2",
      month_end: "5",
      year: 2020,
      day_start: "",
      day_end: "",
      income: "",
      scenario: comparisonMenu[0].level_1,
      city: comparisonMenu[1].city,
      week: comparisonMenu[2].week,
      incomes: comparisonMenu[4].income,
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
    var month_start = this.state.month_start;
    var month_end = this.state.month_end;
    var income = this.state.income;
    var day_start = this.state.day_start;
    var day_end = this.state.day_end;
    var url;
    if (this.state.scena == "1")
      url =
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

    if (this.state.scena == "2") 
      url = "scenario" + scena;

    if (this.state.scena == "3")
      url =
        "scenario" +
        scena +
        "?&lga=" +
        lga +
        "&year_start=2020&month_start=" +
        month_start +
        "&year_end=2020&month_end=" +
        month_end;

    if (this.state.scena == "4")
      url =
        "scenario" +
        scena +
        "?&lga=" +
        lga +
        "&income=" +
        income +
        "&year_start=2020&month_start=" +
        month_start +
        "&day_start=" +
        day_start +
        "&year_end=2020&month_end=" +
        month_end +
        "&day_end=" +
        day_end;

    if (this.state.scena == "5") url = "scenario" + scena + "?&lga=" + lga;

    console.log(url);

    //   this.props.handleEmail = scenario1;
    this.setState({
      url: url,
      data: scenario1
    });
    console.log(url);
    // 触发回调 传递给父组件
    this.props.getChildrenMsg(url);
    console.log(this.state.url);
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

          {this.state.scena == "1" || this.state.scena == "3" || this.state.scena == "4" || this.state.scena == "5"? ( //
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
          ) : null}
          <br />
          <br />
          {this.state.scena == "1" ? (
            <div>
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
            </div>
          ) : null}
          {this.state.scena == "1" ? (
            <div>
              <TagPicker
                data={this.state.week}
                appearance="subtle"
                style={{ width: 250 }}
                menuStyle={{ width: 250 }}
                onSelect={item => {
                  this.setState({ weekday: item });
                }}
                placeholder="--- Please choose week here ---"
              />
              <br />
              <br />
            </div>
          ) : null}
          {this.state.scena == "4" ? (
            <div>
              <TagPicker
                data={this.state.incomes}
                appearance="subtle"
                style={{ width: 250 }}
                menuStyle={{ width: 250 }}
                onSelect={item => {
                  this.setState({ income: item });
                }}
                placeholder={"--- Please choose income here ---"}
              />
              <br />
              <br />
            </div>
          ) : null}

          {this.state.scena == "1" || this.state.scena == "4" ? (
            <div>
              <InputNumber
                prefix="StartTime"
                onChange={item => {
                  if (this.state.scena == "1")
                    this.setState({ daytime_start: item });
                  if (this.state.scena == "4")
                    this.setState({ day_start: item });
                }}
                defaultValue={0}
                max={24}
                min={0}
                //  style={{ width: 150 }} }
              />

              <br />
            </div>
          ) : null}

          {this.state.scena == "1" || this.state.scena == "4" ? (
            <div>
              <InputNumber
                prefix="EndTime"
                onChange={item => {
                  if (this.state.scena == "1") this.setState({ endtime: item });
                  if (this.state.scena == "4") this.setState({ day_end: item });
                }}
                defaultValue={0}
                max={24}
                min={0}
                //  style={{ width: 150 }} }
              />

              <br />
            </div>
          ) : null}
          {this.state.scena == "3" || this.state.scena == "4" ? (
            <div>
              <InputNumber
                prefix="StartMonth"
                value={2}
                onChange={item => {
                  this.setState({ month_start: item });
                }}
                defaultValue={0}
                max={12}
                min={1}
                //  style={{ width: 150 }} }
              />

              <br />
            </div>
          ) : null}

          {this.state.scena == "3" || this.state.scena == "4" ? (
            <InputNumber
              prefix="EndMonth"
              value={5}
              onChange={item => {
                this.setState({ month_end: item });
              }}
              defaultValue={0}
              max={12}
              min={1}
              //  style={{ width: 150 }} }
            />
          ) : null}

          <hr />
          <div  style={{marginLeft:100}}>
          <Button 
            appearance="primary"
            onClick={this.clickSubmit}
            //href={"/comparison/"+`${this.state.url}`}>
            href={"/comparison/" + `${this.state.url}`}
          >
            Submit
          </Button>
          </div>
          

        </div>
        <div>{this.state.visible ? <p>You can see me.</p> : null}</div>
      </div>
    );
  }
}

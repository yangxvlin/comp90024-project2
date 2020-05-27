import React from "react";
import "rsuite/dist/styles/rsuite-default.css";

import KeplermapDaily from "./KeplermapDaily";
import KeplermapCovid from "./KeplermapCovid";
import KeplermapHome from "./KeplermapHome";
import Elements from "./Elements";
import Diagrams from "./Diagrams";
import Scenario5 from "./Scenario5";
import Scenario4 from "./Scenario4";
import Scenario3 from "./Scenario3";
import Scenario2 from "./Scenario2";
import scenario1 from "../testData/s1.json";
import AboutUs from "../testData/aboutUs.jpg";

import { BrowserRouter as Router } from "react-router-dom";

import {
  Icon,
  Sidenav,
  Nav,
  Dropdown,
  Container,
  Navbar,
  Sidebar,
  Header,
  Content
} from "rsuite";

const headerStyles = {
  padding: 18,
  fontSize: 16,
  height: 56,
  background: "#34c3ff",
  color: " #fff",
  whiteSpace: "nowrap",
  overflow: "hidden"
};

const iconStyles = {
  width: 56,
  height: 56,
  lineHeight: "56px",
  textAlign: "center"
};

const NavToggle = ({ expand, onChange }) => {
  return (
    <Navbar appearance="subtle" className="nav-toggle">
      <Navbar.Body>
        <Nav>
          <Dropdown
            placement="topStart"
            trigger="click"
            renderTitle={children => {
              return <Icon style={iconStyles} icon="cog" />;
            }}
          >
            <Dropdown.Item>Help</Dropdown.Item>
            <Dropdown.Item>Settings</Dropdown.Item>
            <Dropdown.Item>Sign out</Dropdown.Item>
          </Dropdown>
        </Nav>

        <Nav pullRight>
          <Nav.Item
            onClick={onChange}
            style={{ width: 56, textAlign: "center" }}
          >
            <Icon icon={expand ? "angle-left" : "angle-right"} />
          </Nav.Item>
        </Nav>
      </Navbar.Body>
    </Navbar>
  );
};

export default class MainContainer extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.state = {
      expand: true,
      url: "",
      diagramData: ""
    };
    this.handleToggle = this.handleToggle.bind(this);
  }

  getChildrenMsg = msg => {
    console.log(msg);

    this.state.diagramData = msg;
    console.log(this.state.diagramData);
    var urlm;
    if(this.state.diagramData === "" || this.state.diagramData === null){
      alert("Please choose one senario for comparison");
    }else{
      urlm = this.state.diagramData.split("?");
      console.log(urlm[0]);
      this.setState({ diagramData: urlm[0], url: msg });
      this.forceUpdate();
    }
  };

  handleToggle() {
    this.setState({
      expand: !this.state.expand
    });
  }

  fetchDate() {
    console.log(scenario1);
  }

  render() {
    const { expand } = this.state;
    return (
      <div className="show-fake-browser sidebar-page">
        <Router>
          <Container>
            <Sidebar
              style={{ display: "flex", flexDirection: "column" }}
              width={expand ? 260 : 56}
              collapsible
            >
              <Sidenav.Header>
                <div style={headerStyles}>
                  <Icon
                    icon="logo-analytics"
                    size="lg"
                    style={{ verticalAlign: 0 }}
                  />
                  <span style={{ marginLeft: 12 }}> COMP90024: team3</span>
                </div>
              </Sidenav.Header>
              <Sidenav
                expanded={expand}
                defaultOpenKeys={["3"]}
                appearance="default"
              >
                <Sidenav.Body>
                  <Nav>
                    <Dropdown
                      eventKey="3"
                      trigger="hover"
                      title="Animation"
                      icon={<Icon icon="magic" />}
                      placement="rightStart"
                    >
                      <Dropdown.Item
                        onClick={() => this.setState({ diagramData: "s1" })}
                      >
                        Twitter Daily Time
                      </Dropdown.Item>
                      <Dropdown.Item
                        onClick={() => this.setState({ diagramData: "s4" })}
                      >
                        Covid-19 Tweet
                      </Dropdown.Item>
                    </Dropdown>
                    <Dropdown
                      eventKey="4"
                      trigger="hover"
                      title="Comparison"
                      placement="rightStart"
                      icon={<Icon icon="gear-circle" />}
                    >
                      <Elements getChildrenMsg={this.getChildrenMsg} />
                    </Dropdown>

                    <Nav.Item
                      eventKey="2"
                      icon={<Icon icon="group" />}
                      onClick={() => this.setState({ diagramData: "aboutUs" })}
                    >
                      About Us
                    </Nav.Item>
                  </Nav>
                </Sidenav.Body>
              </Sidenav>
              <NavToggle expand={expand} onChange={this.handleToggle} />
            </Sidebar>

            <Container>
              <Header></Header>
              <Content>
                {this.state.diagramData == "scenario1" ? (
                  <Diagrams data={this.state.url} />
                ) : null}
                {this.state.diagramData == "scenario2" ? (
                  <Scenario2 data={this.state.url} />
                ) : null}
                {this.state.diagramData == "scenario3" ? (
                  <Scenario3 data={this.state.url} />
                ) : null}
                {this.state.diagramData == "scenario4" ? (
                  <Scenario4 data={this.state.url} />
                ) : null}
                {this.state.diagramData == "scenario5" ? (
                    <Scenario5 data={this.state.url} />
                ) : null}
                {this.state.diagramData == "s1" ? (
                  <KeplermapDaily scenario="1" />
                ) : null}
                {this.state.diagramData == "s4" ? (
                  <KeplermapCovid scenario="4" />
                ) : null}
                {this.state.diagramData == "" ? (
                  <KeplermapHome />
                ) : null}
                {this.state.diagramData == "aboutUs" ? (
                  <img src={AboutUs} width="100%" height="100%" />
                ) : null}
              </Content>
            </Container>
          </Container>
        </Router>
      </div>
    );
  }
}
function Home() {
  return <h2>Home</h2>;
}

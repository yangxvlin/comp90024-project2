import React from "react";
import "rsuite/dist/styles/rsuite-default.css";
import topic from "../testData/topic.json";
import cities from "../testData/au.json";
import Keplermap from "./Keplermap";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import {
  Icon,
  Sidenav,
  Nav,
  Dropdown,
  Container,
  Navbar,
  Sidebar,
  Header,
  Content,
  TagPicker,
  SelectPicker,
  DateRangePicker
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
    this.state = {
      expand: true
    };
    this.handleToggle = this.handleToggle.bind(this);
  }
  handleToggle() {
    this.setState({
      expand: !this.state.expand
    });
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
             //   style={{ background: "black" }}
              >
                <Sidenav.Body>
                  <Nav>
                    <Nav.Item
                      eventKey="1"
                      active
                      icon={<Icon icon="dashboard" />}
                    >
                      Dashboard
                    </Nav.Item>
                    <Dropdown
                      eventKey="3"
                      trigger="hover"
                      title="Scenarios"
                      icon={<Icon icon="magic" />}
                      placement="rightStart"
                    >
                      <Dropdown.Item href="/scenario1">
                        Twitter Daily Time
                      </Dropdown.Item>
                      <Dropdown.Item href="/scenario2">
                        Twitter Popularity
                      </Dropdown.Item>
                      <Dropdown.Item href="/senario3">
                        Twitter Language Usage
                      </Dropdown.Item>
                      <Dropdown.Item href="/scenario4">
                       COVID-19 on twitter and attention in community
                      </Dropdown.Item>
                      <Dropdown.Item href="/scenario5">
                       People Emotion
                      </Dropdown.Item>
                    </Dropdown>
                    <Dropdown
                      eventKey="4"
                      trigger="hover"
                      title="Comparison"
                      placement="rightStart"
                      icon={<Icon icon="gear-circle" />}
                    >
                      <div style={{ align: "center", width: 250 }}>
                        <br />
                        <SelectPicker
                          data={topic}
                          labelKey="topic"
                          style={{ width: 250 }}
                          appearance="default"
                          searchable={false}
                          placeholder="--- Please choose topic here ---"
                        ></SelectPicker>
                        <br />
                        <br />
                        <TagPicker
                          data={cities}
                          labelKey="city"
                          appearance="subtle"
                          style={{ width: 250 }}
                          menuStyle={{ width: 250 }}
                          placeholder="--- Please choose cities here ---"
                        />
                        <br />
                        <br />
                        <DateRangePicker
                          appearance="default"
                          placeholder="--- Please setting date range ---"
                          style={{ width: 280 }}
                        />
                        <hr />
                       
                        <button align='center'>Submit</button>
                        
                      </div>
                      
                    </Dropdown>
                    <Nav.Item eventKey="2" icon={<Icon icon="group" />}>
                      User Group
                    </Nav.Item>
                  </Nav>
                </Sidenav.Body>
              </Sidenav>
              <NavToggle expand={expand} onChange={this.handleToggle} />
            </Sidebar>

            <Container>
              <Header>
                
              </Header>
              <Content>
                <Switch>
                  <Route path="/team">
                    <Keplermap scenario="0" />
                  </Route>
                  <Route path="/home">
                    <Home />
                  </Route>
                  <Route path="/senario1">
                    <Keplermap scenario="1" />
                  </Route>
                  <Route path="/senario2">
                    <Keplermap scenario="2" />
                  </Route>
                  <Route path="/senario3">
                    <Keplermap scenario="3" />
                  </Route>
                  <Route path="/senario4">
                    <Keplermap scenario="4" />
                  </Route>
                  <Route path="/senario5">
                    <Keplermap scenario="5" />
                  </Route>
                  <Route path="/">
                    <Keplermap scenario="0" />
                  </Route>
                </Switch>
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

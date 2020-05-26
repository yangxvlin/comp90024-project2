import React from "react";
import "rsuite/dist/styles/rsuite-default.css";

import Keplermap from "./Keplermap";
import Elements from "./Elements";
import Diagrams from "./Diagrams";
import Scenario5 from "./Scenario5";
import Scenario4 from "./Scenario4";
import Scenario3 from "./Scenario3";
import Scenario2 from "./Scenario2";
import scenario1 from "../testData/s1.json";

import { BrowserRouter as Router, Switch, Route} from "react-router-dom";

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
      diagramData: []
    };
    this.handleToggle = this.handleToggle.bind(this);
  }

  getChildrenMsg = msg => {
    console.log(msg);
    this.setState({ diagramData: msg });
    //   console.log(this.state.diagramData);
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
                //   style={{ background: "black" }}
              >
                <Sidenav.Body>
                  <Nav>
                 { /*  <Nav.Item
                      eventKey="1"
                      active
                      icon={<Icon icon="dashboard" />}
                      href="/dashboard"
                    >
                      Dashboard
                 </Nav.Item>*/}
                    <Dropdown
                      eventKey="3"
                      trigger="hover"
                      title="Animation"
                      icon={<Icon icon="magic" />}
                      placement="rightStart"
                    >
                      <Dropdown.Item href="/scenario1">
                        Twitter Daily Time
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
                      <Elements getChildrenMsg={this.getChildrenMsg} />
                    </Dropdown>

                    <Nav.Item eventKey="2" icon={<Icon icon="group" />}>
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
                <Switch>
                  <Route path="/team">
                    <Keplermap scenario="0" />
                  </Route>
                    <Route path={"/comparison/:url"} 
                      render={(props) => {
                    //    return <Diagrams {...props} items={this.state.data}
                    console.log(props)
                     if(props.match.params.url === "scenario1")
                        return <Diagrams {...props} items={this.state.data}/>
                     else if(props.match.params.url === "scenario2")
                      return <Scenario2 {...props} items={this.state.data}/>
                        
                     if(props.match.params.url === "scenario3")
                        return <Scenario3 {...props} items={this.state.data}/>
                     if(props.match.params.url === "scenario4")
                       return <Scenario4 {...props} items={this.state.data}/>
                     if(props.match.params.url === "scenario5")
                       return <Scenario5 {...props} items={this.state.data}/>
                        
                    //    return <Scenario5 {...props} items={this.state.data}
                    
                        
                      }}
                   />
                      

                  <Route path="/home">
                    <Home />
                  </Route>
                  <Route path="/scenario1">
                    <Keplermap scenario="1" />
                  </Route>
                  <Route path="/scenario2">
                    <Keplermap scenario="2" />
                  </Route>
                  <Route path="/scenario3">
                    <Keplermap scenario="3" />
                  </Route>
                  <Route path="/scenario4">
                    <Keplermap scenario="4" />
                  </Route>
                  <Route path="/scenario5">
                    <Keplermap scenario="5" />
                  </Route>
                  <Route path="/111">
                    <Keplermap scenario="1" />
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

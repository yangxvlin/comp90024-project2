import React, { Component } from "react";
import Keplermap from "./Keplermap";
import { Navbar, Nav, NavDropdown, Form, FormControl, Button,Container } from "react-bootstrap";
import Sidepanel from "./Sidepanel";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.min.css';

export default class Navibar extends Component {
  constructor(props){
    super(props);
    this.state = {isOpen: false};

    this.handleToggle = this.handleToggle.bind(this);
  }
  
  greeting(scenario){
    this.setState({
      scenario
    });
  }

  handleToggle = () => {
    this.setState({ isOpen: !this.state.isOpen });
  };


 
 selectedToggle(selectedKey){
  if(selectedKey === "1"){
  //  alert(`selected ${selectedKey}`)
 //     this.props.getData(selectedKey)
  }
  
 }

  render() {
    return (
     

      
      <Router>
         <Container width={30}>
    <Navbar bg="dark" variant="dark" pullLeft={true}> 
      <Navbar.Brand href="/home"> COMP90024:Team 3</Navbar.Brand>
        <Nav className="mr-auto" pullRight={true} navbar={true}
         onSelect={(selectedKey) => this.selectedToggle(selectedKey)}>
        <Nav.Link href="/home">Home</Nav.Link>
        <NavDropdown title="Scenarios" id="basic-nav-dropdown">
        <NavDropdown.Item href="/scenarios/income" >Income</NavDropdown.Item>
        <NavDropdown.Item href="/scenarios/crimerate">Crime Rate</NavDropdown.Item>
        <NavDropdown.Item href="/scenarios/education">Education</NavDropdown.Item>
        <NavDropdown.Item href="/scenarios/hospitals">Hospitals</NavDropdown.Item>
        <NavDropdown.Item href="/scenarios/population">Population</NavDropdown.Item>
        <NavDropdown.Item href="/scenarios/race">Race</NavDropdown.Item>
        <NavDropdown.Divider />
      </NavDropdown>   
        <Nav.Link href="/team">Team</Nav.Link>
        </Nav>
      <Form inline>
        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
        <Button variant="outline-info">Search</Button>
      </Form>
    </Navbar>
    </Container>
    <Switch>
        <Route path="/team">
          <Sidepanel a="1"/>
          <Keplermap scenario = "0"/>
        </Route>
        <Route path="/home">
          <Home/>
        </Route>
        <Route path="/scenarios/income">
          <Keplermap scenario = "1"/>
        </Route>
        <Route path="/scenarios/crimerate">
          <Keplermap scenario = "2"/>
        </Route>
        <Route path="/scenarios/education">
          <Keplermap scenario = "3"/>
        </Route>
        <Route path="/scenarios/hospitals">
          <Keplermap scenario = "4"/>
        </Route>
        <Route path="/">
          <Keplermap scenario = "0"/>
        </Route>
      </Switch>
   
    </Router>
    );
  }
}

function Side(){
  return(
    <Sidepanel a="1"/>
  )
  }
  function Home(){
    return <h2>Home</h2>
  
}



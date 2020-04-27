import React, { Component } from "react";
import { Navbar, Nav, NavDropdown, Form, FormControl, Button } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';

export default class Navibar extends Component {
  state = {
    isOpen: false
  };
  handleToggle = () => {
    this.setState({ isOpen: !this.state.isOpen });
  };
  render() {
    return (
    <Navbar bg="dark" variant="dark">
      <Navbar.Brand href="#home"> COMP90024:Team 3</Navbar.Brand>
        <Nav className="mr-auto">
        <Nav.Link href="#home">Home</Nav.Link>
        <NavDropdown title="Scenarios" id="basic-nav-dropdown">
        <NavDropdown.Item href="#action/3.1">Income</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.2">Crime Rate</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.3">Education</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.3">Hospitals</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.3">population</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.3">Race</NavDropdown.Item>
        <NavDropdown.Divider />
      </NavDropdown>   
        <Nav.Link href="#team">Team</Nav.Link>
        </Nav>
      <Form inline>
        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
        <Button variant="outline-info">Search</Button>
      </Form>
    </Navbar>

    );
  }
}

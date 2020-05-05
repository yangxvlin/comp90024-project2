import React from 'react';
import { Nav, NavItem } from "react-bootstrap";

function handleSelect(selectedKey) {
    alert('选择 ' + selectedKey);
  }

export default function Comparison(){
    return(
        <Nav bsStyle="pills" stacked activeKey={1} onSelect={handleSelect}>
        <NavItem eventKey={1} href="/home">导航条目 1 的内容</NavItem>
        <NavItem eventKey={2} title="Item">导航条目 2 的内容</NavItem>
        <NavItem eventKey={3} disabled>导航条目 3 的内容</NavItem>
        </Nav>
    )
}


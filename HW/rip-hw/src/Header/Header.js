import { Link } from 'react-router-dom';
import logo from '../logo.png';
import './Header.css'

import Navbar from "react-bootstrap/Navbar"
import Nav from "react-bootstrap/Nav"
import Form from "react-bootstrap/Form"
import FormControl from "react-bootstrap/FormControl"
import Button from "react-bootstrap/Button"

function Header() {
    return(
        <div>
            <Navbar bg="light" expand="lg">
                <div className="logo">
                    <img src={logo} height="20" alt="app-logo"/>
                </div>
                <Navbar.Brand href="/">PinNote</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                    <Link class="nav-link" to="/list">Заметки</Link>
                    <Link class="nav-link" to='/add-note'>Добавление</Link>
                    </Nav>
                    <Form inline>
                    <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                    <Button variant="outline-success">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
        </div>
    )
}

export default Header
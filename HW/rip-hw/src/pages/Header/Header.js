import { Link } from 'react-router-dom'
import logo from '../logo.png'
import './Header.css'

import Navbar from "react-bootstrap/Navbar"
import Nav from "react-bootstrap/Nav"
import Form from "react-bootstrap/Form"
import FormControl from "react-bootstrap/FormControl"
import Button from "react-bootstrap/Button"
import { Component } from 'react'

class Header extends Component{

    constructor(props){
        super(props);
        this.state = { data: {} };
    }

    componentDidMount(){
        document.getElementById("enter").onclick = this.authentication.bind(this)
    }

    authentication(){
        this.setState({
            data: Array.from(document.querySelectorAll('#registration input')).reduce((acc,  input) => ({...acc, [input.id]: input.value}), {})
        });
        console.log(this.state.data)
    }

    render() {
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
                        <Form inline id="registration">
                            <FormControl type="text" placeholder="Логин" className="mr-sm-2" id="login"/>
                            <FormControl type="text" placeholder="Пароль" className="mr-sm-2" id="password"/>
                            <Button variant="outline-dark" id="enter">Вход</Button>
                        </Form>
                    </Navbar.Collapse>
                </Navbar>
            </div>
        )
    }
}

export default Header
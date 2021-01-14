import "./DetailPage.css"

import Button from "react-bootstrap/Button"
import Card from "react-bootstrap/Card"
import Image from "react-bootstrap/Image"
import { Component } from "react"

class DetailPage extends Component{

    constructor(props){
        super(props);
        this.state = { apiText: {}, apiImage: [], id: window.location.pathname};
    }

    callAPI(){
        const id = this.state.id.substr(this.state.id.length - 1)

        fetch("https://ya-russkiy.tk:9000/list/" + id)
        .then(res => res.json())
        .then(res => this.setState({ apiText: res[0] }))
        .catch(err => err);

        fetch("https://ya-russkiy.tk:9000/images/" + id)
        .then(res => res.json())
        .then(res => this.setState({ apiImage: res }))
        .catch(err => err);
    }

    componentDidMount(){
        this.callAPI()
    }

    render() {
        return(
            <div className="container">
                <Button style = {{ margin: '15px', width: 'inherit' }} variant="outline-dark" href="/list">На главную</Button>
                <Button style = {{ margin: '15px', width: 'inherit' }} variant="outline-dark" href={ "/change/" + this.state.id.substr(this.state.id.length - 1)}>Изменить</Button>
                <Card className="textconttitle">
                    <Card.Body className="text">
                        <Card.Title>{this.state.apiText.title}</Card.Title>
                        <hr/>
                        <Card.Text className="text">{this.state.apiText.info}</Card.Text>
                    </Card.Body>
                </Card>
                <div className="imgcont">
                    { this.state.apiImage.map(img =>
                        <Image className="images" src={'https://ya-russkiy.tk:9000/images/' + img.image} thumbnail />
                    )}
                </div>
            </div>
        )
    }
}

export default DetailPage
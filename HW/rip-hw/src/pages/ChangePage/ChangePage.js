import "./ChangePage.css"

import { Component } from "react"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"

class ChangePage extends Component{

    constructor(props){
        super(props);
        this.state = { apiText: {}, id: window.location.pathname};
    }

    getAPI(){
        const id = this.state.id.substr(this.state.id.length - 1)

        fetch("https://ya-russkiy.tk:9000/list/" + id)
        .then(res => res.json())
        .then(res => this.setState({ apiText: res[0] }))
        .catch(err => err);

    }

    sendAPi(){
        const id = parseInt(this.state.id)
        const body = Array.from(document.querySelectorAll('#changesform input')).reduce((acc,  input) => ({...acc, [input.id]: input.value}), {})

        const requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        };
        fetch("https://ya-russkiy.tk:9000/change/" + id, requestOptions)
            .then(response => response.json())
            .then(data => this.setState({ postId: data.id }));
    }

    componentDidMount(){
        this.getAPI()
        document.getElementById("sendChanges").onclick = this.sendAPi.bind(this)
    }

    render(){
        return(
            <div className="container">
                <Form id = "changesform">
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label>Название</Form.Label>
                        <Form.Control type="text" placeholder={this.state.apiText.title} id="title"/>
                        <Form.Text className="text-muted">
                            Название заметки
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>Информация</Form.Label>
                        <Form.Control type="text" placeholder={this.state.apiText.info} id="info"/>
                        <Form.Text className="text-muted">
                            Описание заметки
                        </Form.Text>
                    </Form.Group>
                    <Button variant="outline-dark" id="sendChanges">
                        Сохранить изменения
                    </Button>
                </Form>
            </div>
        )
    }
}

export default ChangePage
import {Component} from "react"
import "./ListPage.css"

import Card from '../components/Cards/Card'

class ListPage extends Component{
    
    constructor(props){
        super(props);
        this.state = { apiResponse: "" };
    }

    callAPI(){
        fetch("http://localhost:9000/")
        .then(res => res.text())
        .then(res => this.setState({ apiResponse: res }))
        .catch(err => err);
    }

    componentDidMount(){
        this.callAPI()
    }
    
    render() {
        return(
            <body className="list-body">
                <Card title={this.state.apiResponse}/>
            </body>
        )
    }
}

export default ListPage
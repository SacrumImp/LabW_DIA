import {Component} from "react"
import "./ListPage.css"

import Card from '../components/Cards/Card'

class ListPage extends Component{
    
    constructor(props){
        super(props);
        this.state = { apiResponse: [] };
    }

    callAPI(){
        fetch("http://ya-russkiy.tk:9000/")
        .then(res => res.json())
        .then(res => this.setState({ apiResponse: res }))
        .catch(err => err);
    }

    componentDidMount(){
        this.callAPI()
    }
    
    render() {
        return(
            <body className="list-body">
                <div className="row">
                    {this.state.apiResponse.map(res => <Card data={res}/>)}
                </div>
            </body>
        )
    }
}

export default ListPage
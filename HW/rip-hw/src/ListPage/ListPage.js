import {Component} from "react"
import "./ListPage.css"

import NoteCard from '../components/Cards/NoteCard'

class ListPage extends Component{
    
    constructor(props){
        super(props);
        this.state = { apiText: [], apiImage: []};
    }

    callAPI(){
        fetch("https://ya-russkiy.tk:9000/")
        .then(res => res.json())
        .then(res => this.setState({ apiText: res }))
        .catch(err => err);

        fetch("https://ya-russkiy.tk:9000/images")
        .then(res => res.json())
        .then(res => this.setState({ apiImage: res }))
        .catch(err => err);
    }

    componentDidMount(){
        this.callAPI()
    }
    
    render() {
        return(
            <div className="list-body">
                <div className="row">
                    {this.state.apiText.map(res => <NoteCard data={res} images={this.state.apiImage.filter(img => img.note === res.id)}/>)}
                </div>
            </div>
        )
    }
}

export default ListPage
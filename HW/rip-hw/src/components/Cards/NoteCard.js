import './NoteCard.css'
import Carousel from 'react-bootstrap/Carousel' 
import Card from 'react-bootstrap/Card'

function NoteCard(props) {
    return(
        <Card className="card">
            <Carousel>
                {props.images.map(img => 
                            <Carousel.Item>
                                <img
                                className="d-block w-100"
                                src={'http://ya-russkiy.tk:9000/images/' + img.image}
                                alt="slide"
                                />
                            </Carousel.Item>
                )}       
            </Carousel>
            <Card.Body>
                <Card.Text>{props.data.location.x + ' ' + props.data.location.y}</Card.Text>
                <Card.Title>{props.data.title}</Card.Title>
                <Card.Text>{props.data.info}</Card.Text>
            </Card.Body>
        </Card>
    )
}

export default NoteCard
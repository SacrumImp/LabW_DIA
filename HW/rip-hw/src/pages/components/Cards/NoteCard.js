import './NoteCard.css'
import Carousel from 'react-bootstrap/Carousel' 
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'

function NoteCard(props) {
    return(
        <Card className="card">
            <Carousel>
                {props.images.map(img => 
                            <Carousel.Item>
                                <img
                                className="d-block w-100"
                                src={'https://ya-russkiy.tk:9000/images/' + img.image}
                                alt="slide"
                                />
                            </Carousel.Item>
                )}       
            </Carousel>
            <Card.Body>
                <Card.Text>{props.data.location.x + ' ' + props.data.location.y}</Card.Text>
                <Card.Title>{props.data.title}</Card.Title>
            </Card.Body>
            <Button style = {{ margin: '15px' }} variant="outline-dark" href={"/list/"+props.data.id}>Подробнее</Button>
        </Card>
    )
}

export default NoteCard
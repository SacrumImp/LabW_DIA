import './Card.css'

function Card(props) {
    return(
        <div class="card">
                <img src="..." class="card-img-top" alt="..."/>
                <div class="card-body">
                    <p class="card-text">{props.data.location.x + ' ' + props.data.location.y}</p>
                    <h5 class="card-title">{props.data.title}</h5>
                    <p class="card-text">{props.data.info}</p>
                </div>
        </div>
    )
}

export default Card
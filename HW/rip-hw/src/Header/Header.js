import { Link } from 'react-router-dom';
import logo from '../logo.png';
import './Header.css'

function Header() {
    return(
        <div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <div className="logo">
                    <img src={logo} height="20" alt="app-logo"/>
                </div>
                <Link class="navbar-brand" to="/">PinNote</Link>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <Link class="nav-link" to="/list">Notes</Link>
                        </li>
                        <li class="nav-item">
                            <Link class="nav-link" to='/add-note'>Add Note</Link>
                        </li>
                    </ul>
                    <form class="form-inline my-2 my-lg-0">
                        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"></input>
                        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </nav>
        </div>
    )
}

export default Header
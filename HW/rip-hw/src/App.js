import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Header from './pages/Header/Header'
import MainPage from './pages/MainPage/MainPage'
import ListPage from './ListPage/ListPage'
import DetailPage from './pages/DetailPage/DetailPage'
import ChangePage from './pages/ChangePage/ChangePage'

import './App.css';

function App() {
  return (
    <div className="App">
      <Router basename="/">
        <Header />
        <Switch>
          <Route path = "/change/:id">
            <ChangePage />
          </Route>
          <Route path = "/list/:id">
            <DetailPage />
          </Route>
          <Route path = "/list">
            <ListPage />
          </Route>
          <Route path = "/">
            <MainPage />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

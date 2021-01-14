import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Header from './Header/Header'
import MainPage from './MainPage/MainPage'
import ListPage from './ListPage/ListPage'
import DetailPage from './DetailPage/DetailPage'

import './App.css';

function App() {
  return (
    <div className="App">
      <Router basename="/">
        <Header />
        <Switch>
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

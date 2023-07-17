import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import './App.css';
import HomePage from './components/homepage';
import MenuPage from './components/menupage';
function App() {
  return (
    <Router>
       <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/menu" component={MenuPage} />
      </Switch>
    </Router>
  );
}

export default App;

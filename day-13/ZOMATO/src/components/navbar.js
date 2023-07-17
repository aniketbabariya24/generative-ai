import React from 'react';
import './styles/navbar.css';
import logo from './pngegg.png';
import { Link } from 'react-router-dom';


const NavBar = () => {
  return (
    <nav>
      <div className="logo">
        <h1>FastX</h1>
        <img src={logo} alt="Logo" />
      </div>
      <ul className="menu">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/menu">Menu</Link></li>
        <li><Link to="#">Orders</Link></li>
        <li><a to="#">Restaurants</a></li>
        <li><a to="#">About</a></li>
        <li><a to="./register.html">Logout</a></li>
      </ul>
    </nav>
  );
}

export default NavBar;

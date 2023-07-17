import React from 'react';
import './styles/navbar.css';
import logo from './pngegg.png';
import { Link } from 'react-router-dom';
import NavBar from './navbar';
import Blog from './blogs';

const HomePage = () => {
  return (
   <div>
    <NavBar />
    <Blog />
   </div>
  );
}

export default HomePage;

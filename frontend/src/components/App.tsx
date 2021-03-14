import React, { useState, useEffect } from 'react';
import Login from './Login'
import Signup from './Signup'
import logo from '../assets/logo.png';
import '../styles/App.scss';

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const url = "http://localhost:5000";
      const result = await fetch(url);
      const body = await result.json();
      setData(body.data);
      console.log('body', body);
    }
    fetchData();
  }, [])

  return (
    <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to Course Compare. Hello!
        </p>
        <Signup />
        <Login />
    </div>
  );
}

export default App;

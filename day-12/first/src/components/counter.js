import React, { useState } from 'react';
import './CounterApp.css';

function CounterApp() {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    setCount(count - 1);
  };

  const handleReset = () => {
    setCount(0);
  };

  return (
    <div className="counter-app">
      <h1>Counter App</h1>
      <div className="counter-display">
        <p>{count}</p>
      </div>
      <div className="counter-buttons">
        <button onClick={handleDecrement}>-</button>
        <button onClick={handleIncrement}>+</button>
        <button onClick={handleReset}>Reset</button>
      </div>
    </div>
  );
}

export default CounterApp;

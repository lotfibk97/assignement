import './App.css';
import React, { useState } from 'react';
function App() {
  const [inputString, setInputString] = useState('');
  const [inputNumber, setInputNumber] = useState('');
  const [outputString, setOutputString] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    setErrorMessage('');
    if (inputString.trim() === '') {
      setErrorMessage('Please enter a string.');
      return;
    }
    if (isNaN(inputNumber) || !Number.isInteger(parseInt(inputNumber))  ) {
      setErrorMessage('Please enter a valid number.');
      return;
    }
    if (inputNumber < 0 ) {
      setErrorMessage('Please enter a positive number.');
      return;
    }
    setOutputString(inputString.repeat(inputNumber));
    setInputString('');
    setInputNumber('');
  };
  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label htmlFor="stringInput">String:</label>
        <input
          type="text"
          id="stringInput"
          value={inputString}
          onChange={(event) => setInputString(event.target.value)}
        />
        <br />
        <label htmlFor="numberInput">Number:</label>
        <input  
          type="number"
          id="numberInput"
          value={inputNumber}
          onChange={(event) => setInputNumber(event.target.value)}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
      {outputString && <p>{outputString}</p>}
      
    </div>
  );
}

export default App;

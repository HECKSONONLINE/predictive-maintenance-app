import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handlePredict = async () => {
    const values = input.split(',').map(Number);
    const res = await axios.post('http://localhost:5000/predict', { features: values });
    setPrediction(res.data.prediction);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h2>Predictive Maintenance App</h2>
      <p>Enter values: temperature, pressure, vibration</p>
      <input
        type="text"
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="e.g., 150,90,0.6"
      />
      <button onClick={handlePredict}>Predict</button>
      {prediction !== null && (
        <p>
          Prediction: {prediction === 1 ? "⚠️ Failure likely" : "✅ No failure expected"}
        </p>
      )}
    </div>
  );
}

export default App;
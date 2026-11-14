import React, { useState } from 'react';
import './PredictPage.css';

function PredictPage() {
  const [formData, setFormData] = useState({
    hour: '8',
    day: '1',
    vehicleCount: '120',
    roadType: '1',
    weather: '0'
  });

  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  const roadTypes = ['City', 'Highway', 'Residential'];
  const weatherTypes = ['Clear', 'Fog', 'Rain'];

  const validateForm = () => {
    const newErrors = {};

    if (!formData.hour || formData.hour < 0 || formData.hour > 23) {
      newErrors.hour = 'Hour must be between 0 and 23';
    }

    if (!formData.day) {
      newErrors.day = 'Please select a day';
    }

    if (!formData.vehicleCount || formData.vehicleCount < 0 || formData.vehicleCount > 500) {
      newErrors.vehicleCount = 'Vehicle count must be between 0 and 500';
    }

    if (!formData.roadType) {
      newErrors.roadType = 'Please select a road type';
    }

    if (!formData.weather) {
      newErrors.weather = 'Please select weather condition';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    // Clear error for this field
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const features = [
        parseInt(formData.hour),
        parseInt(formData.day),
        parseInt(formData.vehicleCount),
        parseInt(formData.roadType),
        parseInt(formData.weather)
      ];

      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Prediction failed');
      }

      // Save to history
      const prediction = {
        id: Date.now(),
        timestamp: new Date().toISOString(),
        inputs: {
          hour: formData.hour,
          day: dayNames[formData.day],
          vehicleCount: formData.vehicleCount,
          roadType: roadTypes[formData.roadType],
          weather: weatherTypes[formData.weather]
        },
        result: data.traffic_level,
        confidence: data.confidence,
        probabilities: data.probabilities
      };

      // Save to localStorage
      const history = JSON.parse(localStorage.getItem('predictionHistory') || '[]');
      history.unshift(prediction);
      localStorage.setItem('predictionHistory', JSON.stringify(history));

      setResult(data);
    } catch (error) {
      alert('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFormData({
      hour: '8',
      day: '1',
      vehicleCount: '120',
      roadType: '1',
      weather: '0'
    });
    setErrors({});
    setResult(null);
  };

  const getResultIcon = (level) => {
    switch (level) {
      case 'Low': return '🟢';
      case 'Medium': return '🟡';
      case 'High': return '🔴';
      default: return '⚪';
    }
  };

  return (
    <div className="predict-page">
      <div className="page-header">
        <h1>Traffic Prediction</h1>
        <p>Enter traffic conditions to predict congestion levels</p>
      </div>

      <div className="predict-container">
        <div className="predict-form-card card">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="form-label">Hour of Day</label>
              <input
                type="number"
                name="hour"
                className="form-input"
                value={formData.hour}
                onChange={handleChange}
                min="0"
                max="23"
              />
              <span className="form-hint">0-23 (24-hour format)</span>
              {errors.hour && <span className="form-error">{errors.hour}</span>}
            </div>

            <div className="form-group">
              <label className="form-label">Day of Week</label>
              <select
                name="day"
                className="form-select"
                value={formData.day}
                onChange={handleChange}
              >
                {dayNames.map((day, index) => (
                  <option key={index} value={index}>{day}</option>
                ))}
              </select>
              {errors.day && <span className="form-error">{errors.day}</span>}
            </div>

            <div className="form-group">
              <label className="form-label">Vehicle Count</label>
              <input
                type="number"
                name="vehicleCount"
                className="form-input"
                value={formData.vehicleCount}
                onChange={handleChange}
                min="0"
                max="500"
              />
              <span className="form-hint">Number of vehicles (0-500)</span>
              {errors.vehicleCount && <span className="form-error">{errors.vehicleCount}</span>}
            </div>

            <div className="form-group">
              <label className="form-label">Road Type</label>
              <select
                name="roadType"
                className="form-select"
                value={formData.roadType}
                onChange={handleChange}
              >
                {roadTypes.map((type, index) => (
                  <option key={index} value={index}>{type}</option>
                ))}
              </select>
              {errors.roadType && <span className="form-error">{errors.roadType}</span>}
            </div>

            <div className="form-group">
              <label className="form-label">Weather Condition</label>
              <select
                name="weather"
                className="form-select"
                value={formData.weather}
                onChange={handleChange}
              >
                {weatherTypes.map((type, index) => (
                  <option key={index} value={index}>{type}</option>
                ))}
              </select>
              {errors.weather && <span className="form-error">{errors.weather}</span>}
            </div>

            <div className="form-actions">
              <button type="submit" className="btn btn-primary" disabled={loading}>
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Predicting...
                  </>
                ) : (
                  'Predict Traffic'
                )}
              </button>
              <button type="button" className="btn btn-secondary" onClick={handleReset}>
                Reset Form
              </button>
            </div>
          </form>
        </div>

        {result && (
          <div className="result-card card">
            <h2>Prediction Result</h2>
            <div className="result-main">
              <span className="result-icon">{getResultIcon(result.traffic_level)}</span>
              <div className="result-info">
                <span className={`badge badge-${result.traffic_level.toLowerCase()}`}>
                  {result.traffic_level}
                </span>
                <p className="result-confidence">Confidence: {result.confidence}%</p>
              </div>
            </div>

            <div className="probabilities">
              <h3>Probability Distribution</h3>
              <div className="prob-bars">
                {Object.entries(result.probabilities).map(([level, prob]) => (
                  <div key={level} className="prob-item">
                    <div className="prob-label">
                      <span>{level}</span>
                      <span>{prob}%</span>
                    </div>
                    <div className="prob-bar-container">
                      <div
                        className={`prob-bar prob-bar-${level.toLowerCase()}`}
                        style={{ width: `${prob}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default PredictPage;

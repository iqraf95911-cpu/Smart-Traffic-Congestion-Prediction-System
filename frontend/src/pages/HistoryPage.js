import React, { useState, useEffect } from 'react';
import './HistoryPage.css';

function HistoryPage() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = () => {
    const savedHistory = JSON.parse(localStorage.getItem('predictionHistory') || '[]');
    setHistory(savedHistory);
  };

  const clearHistory = () => {
    if (window.confirm('Are you sure you want to clear all history?')) {
      localStorage.removeItem('predictionHistory');
      setHistory([]);
    }
  };

  const deleteEntry = (id) => {
    if (window.confirm('Delete this entry?')) {
      const updatedHistory = history.filter(item => item.id !== id);
      localStorage.setItem('predictionHistory', JSON.stringify(updatedHistory));
      setHistory(updatedHistory);
    }
  };

  const formatDate = (isoString) => {
    const date = new Date(isoString);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getResultClass = (result) => {
    return `result-badge badge-${result.toLowerCase()}`;
  };

  return (
    <div className="history-page">
      <div className="page-header">
        <div>
          <h1>Prediction History</h1>
          <p>View and manage your past predictions</p>
        </div>
        {history.length > 0 && (
          <button className="btn btn-danger" onClick={clearHistory}>
            Clear All History
          </button>
        )}
      </div>

      {history.length === 0 ? (
        <div className="empty-state card">
          <div className="empty-icon">📝</div>
          <h2>No Predictions Yet</h2>
          <p>Your prediction history will appear here once you make your first prediction.</p>
          <a href="/predict" className="btn btn-primary">Make a Prediction</a>
        </div>
      ) : (
        <div className="history-table-container">
          <table className="history-table">
            <thead>
              <tr>
                <th>Timestamp</th>
                <th>Hour</th>
                <th>Day</th>
                <th>Vehicles</th>
                <th>Road Type</th>
                <th>Weather</th>
                <th>Result</th>
                <th>Confidence</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {history.map((entry) => (
                <tr key={entry.id} className={`history-row row-${entry.result.toLowerCase()}`}>
                  <td className="timestamp-cell">{formatDate(entry.timestamp)}</td>
                  <td>{entry.inputs.hour}:00</td>
                  <td>{entry.inputs.day}</td>
                  <td>{entry.inputs.vehicleCount}</td>
                  <td>{entry.inputs.roadType}</td>
                  <td>{entry.inputs.weather}</td>
                  <td>
                    <span className={getResultClass(entry.result)}>
                      {entry.result}
                    </span>
                  </td>
                  <td>{entry.confidence}%</td>
                  <td>
                    <button
                      className="btn-icon btn-delete"
                      onClick={() => deleteEntry(entry.id)}
                      title="Delete"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {history.length > 0 && (
        <div className="history-stats card">
          <h3>Quick Stats</h3>
          <div className="stats-grid">
            <div className="stat-item">
              <span className="stat-value">{history.length}</span>
              <span className="stat-label">Total Predictions</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">
                {history.filter(h => h.result === 'Low').length}
              </span>
              <span className="stat-label">Low Congestion</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">
                {history.filter(h => h.result === 'Medium').length}
              </span>
              <span className="stat-label">Medium Congestion</span>
            </div>
            <div className="stat-item">
              <span className="stat-value">
                {history.filter(h => h.result === 'High').length}
              </span>
              <span className="stat-label">High Congestion</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default HistoryPage;

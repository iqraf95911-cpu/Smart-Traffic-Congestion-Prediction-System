import React, { useState, useEffect } from 'react';
import {
  BarChart, Bar, LineChart, Line, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import './AnalyticsPage.css';

function AnalyticsPage() {
  const [history, setHistory] = useState([]);
  const [stats, setStats] = useState({
    total: 0,
    mostCommon: 'N/A',
    peakHour: 'N/A'
  });

  useEffect(() => {
    loadAnalytics();
  }, []);

  const loadAnalytics = () => {
    const savedHistory = JSON.parse(localStorage.getItem('predictionHistory') || '[]');
    setHistory(savedHistory);
    calculateStats(savedHistory);
  };

  const calculateStats = (data) => {
    if (data.length === 0) return;

    // Most common result
    const resultCounts = data.reduce((acc, item) => {
      acc[item.result] = (acc[item.result] || 0) + 1;
      return acc;
    }, {});
    const mostCommon = Object.keys(resultCounts).reduce((a, b) =>
      resultCounts[a] > resultCounts[b] ? a : b
    );

    // Peak hour
    const hourCounts = data.reduce((acc, item) => {
      const hour = item.inputs.hour;
      acc[hour] = (acc[hour] || 0) + 1;
      return acc;
    }, {});
    const peakHour = Object.keys(hourCounts).reduce((a, b) =>
      hourCounts[a] > hourCounts[b] ? a : b
    );

    setStats({
      total: data.length,
      mostCommon,
      peakHour: `${peakHour}:00`
    });
  };

  // Congestion Distribution Data
  const getDistributionData = () => {
    const counts = { Low: 0, Medium: 0, High: 0 };
    history.forEach(item => {
      counts[item.result]++;
    });
    return [
      { name: 'Low', value: counts.Low, color: '#2ea043' },
      { name: 'Medium', value: counts.Medium, color: '#d29922' },
      { name: 'High', value: counts.High, color: '#f85149' }
    ];
  };

  // Predictions Over Time Data
  const getTimelineData = () => {
    const hourCounts = {};
    for (let i = 0; i < 24; i++) {
      hourCounts[i] = 0;
    }
    history.forEach(item => {
      const hour = parseInt(item.inputs.hour);
      hourCounts[hour]++;
    });
    return Object.keys(hourCounts).map(hour => ({
      hour: `${hour}:00`,
      predictions: hourCounts[hour]
    }));
  };

  // Road Type Distribution Data
  const getRoadTypeData = () => {
    const roadCounts = {};
    history.forEach(item => {
      const road = item.inputs.roadType;
      roadCounts[road] = (roadCounts[road] || 0) + 1;
    });
    return Object.keys(roadCounts).map(road => ({
      name: road,
      value: roadCounts[road]
    }));
  };

  const COLORS = ['#58a6ff', '#1f6feb', '#388bfd', '#0969da'];

  return (
    <div className="analytics-page">
      <div className="page-header">
        <h1>Analytics Dashboard</h1>
        <p>Insights from your prediction history</p>
      </div>

      {history.length === 0 ? (
        <div className="empty-state card">
          <div className="empty-icon">📊</div>
          <h2>No Data Available</h2>
          <p>Make some predictions to see analytics and insights.</p>
          <a href="/predict" className="btn btn-primary">Make a Prediction</a>
        </div>
      ) : (
        <>
          {/* Summary Stats */}
          <div className="stats-cards">
            <div className="stat-card card">
              <div className="stat-icon">📈</div>
              <div className="stat-content">
                <div className="stat-value">{stats.total}</div>
                <div className="stat-label">Total Predictions</div>
              </div>
            </div>

            <div className="stat-card card">
              <div className="stat-icon">🎯</div>
              <div className="stat-content">
                <div className="stat-value">{stats.mostCommon}</div>
                <div className="stat-label">Most Common Result</div>
              </div>
            </div>

            <div className="stat-card card">
              <div className="stat-icon">⏰</div>
              <div className="stat-content">
                <div className="stat-value">{stats.peakHour}</div>
                <div className="stat-label">Peak Hour</div>
              </div>
            </div>
          </div>

          {/* Charts */}
          <div className="charts-grid">
            {/* Bar Chart - Congestion Distribution */}
            <div className="chart-card card">
              <h3>Congestion Distribution</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={getDistributionData()}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#30363d" />
                  <XAxis dataKey="name" stroke="#8b949e" />
                  <YAxis stroke="#8b949e" />
                  <Tooltip
                    contentStyle={{
                      background: '#161b22',
                      border: '1px solid #30363d',
                      borderRadius: '8px',
                      color: '#c9d1d9'
                    }}
                  />
                  <Bar dataKey="value" radius={[8, 8, 0, 0]}>
                    {getDistributionData().map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Line Chart - Predictions Over Time */}
            <div className="chart-card card">
              <h3>Predictions by Hour</h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={getTimelineData()}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#30363d" />
                  <XAxis dataKey="hour" stroke="#8b949e" />
                  <YAxis stroke="#8b949e" />
                  <Tooltip
                    contentStyle={{
                      background: '#161b22',
                      border: '1px solid #30363d',
                      borderRadius: '8px',
                      color: '#c9d1d9'
                    }}
                  />
                  <Line
                    type="monotone"
                    dataKey="predictions"
                    stroke="#58a6ff"
                    strokeWidth={2}
                    dot={{ fill: '#58a6ff', r: 4 }}
                    activeDot={{ r: 6 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>

            {/* Pie Chart - Road Types */}
            <div className="chart-card card">
              <h3>Road Type Distribution</h3>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={getRoadTypeData()}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                    outerRadius={100}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {getRoadTypeData().map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip
                    contentStyle={{
                      background: '#161b22',
                      border: '1px solid #30363d',
                      borderRadius: '8px',
                      color: '#c9d1d9'
                    }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default AnalyticsPage;

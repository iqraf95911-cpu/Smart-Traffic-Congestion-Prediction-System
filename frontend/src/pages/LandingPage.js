import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';

function LandingPage() {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate('/predict');
  };

  return (
    <div className="landing-page">
      <div className="animated-background">
        <div className="road-line"></div>
        <div className="road-line"></div>
        <div className="road-line"></div>
        <div className="road-line"></div>
      </div>
      
      <div className="landing-content">
        <div className="logo-container">
          <div className="logo">
            <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
              <circle cx="40" cy="40" r="35" stroke="url(#gradient)" strokeWidth="3" />
              <path d="M25 40 L35 30 L45 40 L55 25" stroke="url(#gradient)" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
              <circle cx="25" cy="40" r="3" fill="#58a6ff" />
              <circle cx="35" cy="30" r="3" fill="#58a6ff" />
              <circle cx="45" cy="40" r="3" fill="#58a6ff" />
              <circle cx="55" cy="25" r="3" fill="#58a6ff" />
              <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stopColor="#58a6ff" />
                  <stop offset="100%" stopColor="#1f6feb" />
                </linearGradient>
              </defs>
            </svg>
          </div>
          <h1 className="app-title">FlowSense AI</h1>
          <p className="app-tagline">Smart Traffic Congestion Prediction</p>
        </div>

        <button className="cta-button" onClick={handleGetStarted}>
          <span>Get Started</span>
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M7 3 L14 10 L7 17" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </button>

        <div className="features-preview">
          <div className="feature-item">
            <span className="feature-icon">🎯</span>
            <span>Accurate Predictions</span>
          </div>
          <div className="feature-item">
            <span className="feature-icon">📊</span>
            <span>Analytics Dashboard</span>
          </div>
          <div className="feature-item">
            <span className="feature-icon">📝</span>
            <span>History Tracking</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;

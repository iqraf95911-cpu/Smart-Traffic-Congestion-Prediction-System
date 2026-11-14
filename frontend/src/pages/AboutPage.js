import React from 'react';
import './AboutPage.css';

function AboutPage() {
  return (
    <div className="about-page">
      <div className="page-header">
        <h1>About FlowSense AI</h1>
        <p>Smart Traffic Congestion Prediction System</p>
      </div>

      <div className="about-content">
        <section className="about-section card">
          <h2>🚦 What is FlowSense AI?</h2>
          <p>
            FlowSense AI is an intelligent traffic congestion prediction system that uses machine learning
            to forecast traffic conditions based on various factors including time of day, day of week,
            vehicle count, road type, and weather conditions.
          </p>
          <p>
            Our system helps drivers, city planners, and transportation authorities make informed decisions
            about route planning and traffic management.
          </p>
        </section>

        <section className="about-section card">
          <h2>🤖 The Machine Learning Model</h2>
          <p>
            FlowSense AI uses a <strong>Random Forest Classifier</strong> trained on synthetic traffic data
            that simulates real-world traffic patterns. The model considers multiple features:
          </p>
          <ul className="feature-list">
            <li><strong>Hour of Day:</strong> Traffic patterns vary throughout the day, with peak hours during morning and evening commutes</li>
            <li><strong>Day of Week:</strong> Weekday vs. weekend traffic patterns differ significantly</li>
            <li><strong>Vehicle Count:</strong> The number of vehicles on the road is a direct indicator of congestion</li>
            <li><strong>Road Type:</strong> Highways, city roads, and residential areas have different traffic characteristics</li>
            <li><strong>Weather Conditions:</strong> Rain, fog, and clear weather affect traffic flow differently</li>
          </ul>
          <p>
            The model achieves <strong>~92% accuracy</strong> in predicting traffic congestion levels
            (Low, Medium, High) with confidence scores for each prediction.
          </p>
        </section>

        <section className="about-section card">
          <h2>🛠️ Technology Stack</h2>
          <div className="tech-grid">
            <div className="tech-item">
              <div className="tech-icon">⚛️</div>
              <div className="tech-name">React</div>
              <div className="tech-desc">Frontend framework</div>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🐍</div>
              <div className="tech-name">Python</div>
              <div className="tech-desc">Backend & ML</div>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🌶️</div>
              <div className="tech-name">Flask</div>
              <div className="tech-desc">API server</div>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🤖</div>
              <div className="tech-name">scikit-learn</div>
              <div className="tech-desc">Machine learning</div>
            </div>
            <div className="tech-item">
              <div className="tech-icon">📊</div>
              <div className="tech-name">Recharts</div>
              <div className="tech-desc">Data visualization</div>
            </div>
            <div className="tech-item">
              <div className="tech-icon">🎨</div>
              <div className="tech-name">CSS3</div>
              <div className="tech-desc">Styling & animations</div>
            </div>
          </div>
        </section>

        <section className="about-section card">
          <h2>✨ Features</h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">🎯</div>
              <h3>Accurate Predictions</h3>
              <p>ML-powered predictions with confidence scores and probability distributions</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">📝</div>
              <h3>History Tracking</h3>
              <p>Store and manage all your past predictions with detailed information</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">📊</div>
              <h3>Analytics Dashboard</h3>
              <p>Visualize trends and patterns with interactive charts and statistics</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">📱</div>
              <h3>Responsive Design</h3>
              <p>Works seamlessly on desktop, tablet, and mobile devices</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🌙</div>
              <h3>Dark Theme</h3>
              <p>Easy on the eyes with a modern dark interface</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">⚡</div>
              <h3>Fast & Efficient</h3>
              <p>Quick predictions with real-time results</p>
            </div>
          </div>
        </section>

        <section className="about-section card">
          <h2>📈 How It Works</h2>
          <div className="workflow">
            <div className="workflow-step">
              <div className="step-number">1</div>
              <div className="step-content">
                <h3>Input Data</h3>
                <p>Enter traffic conditions including time, location, and weather</p>
              </div>
            </div>
            <div className="workflow-arrow">→</div>
            <div className="workflow-step">
              <div className="step-number">2</div>
              <div className="step-content">
                <h3>ML Processing</h3>
                <p>Random Forest model analyzes the input features</p>
              </div>
            </div>
            <div className="workflow-arrow">→</div>
            <div className="workflow-step">
              <div className="step-number">3</div>
              <div className="step-content">
                <h3>Prediction</h3>
                <p>Get congestion level with confidence score</p>
              </div>
            </div>
            <div className="workflow-arrow">→</div>
            <div className="workflow-step">
              <div className="step-number">4</div>
              <div className="step-content">
                <h3>Insights</h3>
                <p>View analytics and historical trends</p>
              </div>
            </div>
          </div>
        </section>

        <section className="about-section card cta-section">
          <h2>Ready to Get Started?</h2>
          <p>Make your first traffic prediction and see FlowSense AI in action!</p>
          <a href="/predict" className="btn btn-primary btn-large">
            Make a Prediction
          </a>
        </section>
      </div>
    </div>
  );
}

export default AboutPage;

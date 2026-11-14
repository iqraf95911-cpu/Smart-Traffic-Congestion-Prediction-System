import React, { useState } from 'react';
import { Outlet, NavLink } from 'react-router-dom';
import './MainLayout.css';

function MainLayout() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  const closeMobileMenu = () => {
    setMobileMenuOpen(false);
  };

  return (
    <div className="main-layout">
      <nav className="navbar">
        <div className="navbar-container">
          <div className="navbar-brand">
            <svg width="32" height="32" viewBox="0 0 80 80" fill="none">
              <circle cx="40" cy="40" r="35" stroke="url(#gradient)" strokeWidth="3" />
              <path d="M25 40 L35 30 L45 40 L55 25" stroke="url(#gradient)" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
              <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stopColor="#58a6ff" />
                  <stop offset="100%" stopColor="#1f6feb" />
                </linearGradient>
              </defs>
            </svg>
            <span className="brand-name">FlowSense AI</span>
          </div>

          <button className="mobile-menu-toggle" onClick={toggleMobileMenu}>
            <span></span>
            <span></span>
            <span></span>
          </button>

          <div className={`navbar-links ${mobileMenuOpen ? 'mobile-open' : ''}`}>
            <NavLink to="/predict" className="nav-link" onClick={closeMobileMenu}>
              <span className="nav-icon">🎯</span>
              Predict
            </NavLink>
            <NavLink to="/history" className="nav-link" onClick={closeMobileMenu}>
              <span className="nav-icon">📝</span>
              History
            </NavLink>
            <NavLink to="/analytics" className="nav-link" onClick={closeMobileMenu}>
              <span className="nav-icon">📊</span>
              Analytics
            </NavLink>
            <NavLink to="/about" className="nav-link" onClick={closeMobileMenu}>
              <span className="nav-icon">ℹ️</span>
              About
            </NavLink>
          </div>
        </div>
      </nav>

      <main className="main-content">
        <Outlet />
      </main>

      <footer className="footer">
        <p>Built with ❤️ · FlowSense AI · 2025</p>
      </footer>
    </div>
  );
}

export default MainLayout;

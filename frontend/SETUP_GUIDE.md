# 🚀 FlowSense AI - Complete Setup Guide

## Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
cd frontend
npm install
```

### Step 2: Start Backend (Flask)
In a separate terminal:
```bash
cd ..
python app.py
```

### Step 3: Start Frontend (React)
```bash
npm start
```

### Step 4: Open Browser
Navigate to: **http://localhost:3000**

---

## Detailed Setup

### Prerequisites

✅ **Node.js 14+** - [Download](https://nodejs.org/)
✅ **npm** (comes with Node.js)
✅ **Python 3.8+** - [Download](https://python.org/)
✅ **Flask backend** - Already set up in parent directory

### Installation Steps

#### 1. Backend Setup (if not already done)

```bash
# From project root
cd Smart-Traffic-Congestion-Prediction-System

# Install Python dependencies
pip install -r requirements.txt

# Train model (if not already trained)
python src/train_model.py

# Start Flask server
python app.py
```

You should see:
```
✓ Model loaded
✓ Traffic predictor initialized successfully
🚀 Starting Smart Traffic Congestion Prediction API
* Running on http://127.0.0.1:5000
```

#### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

This will install:
- React 18.2.0
- React Router DOM 6.20.0
- Recharts 2.10.0
- React Scripts 5.0.1

#### 3. Start Development Server

```bash
npm start
```

The app will automatically open at **http://localhost:3000**

---

## Project Structure

```
Smart-Traffic-Congestion-Prediction-System/
│
├── frontend/                    # React application
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── MainLayout.js   # Navbar & Footer
│   │   │   └── MainLayout.css
│   │   ├── pages/
│   │   │   ├── LandingPage.js  # Entry page
│   │   │   ├── PredictPage.js  # Prediction form
│   │   │   ├── HistoryPage.js  # Past predictions
│   │   │   ├── AnalyticsPage.js # Charts & stats
│   │   │   └── AboutPage.js    # Info page
│   │   ├── App.js              # Main app with routing
│   │   ├── App.css             # Global styles
│   │   ├── index.js            # Entry point
│   │   └── index.css           # Base styles
│   ├── package.json
│   └── README.md
│
├── app.py                       # Flask API
├── config.py                    # Configuration
├── model.pkl                    # Trained ML model
└── requirements.txt             # Python dependencies
```

---

## Features Overview

### 🏠 Landing Page
- Animated traffic background
- Glowing "Get Started" button
- Feature preview cards
- Smooth transition to app

### 🎯 Predict Page
- Form with 5 input fields
- Real-time validation
- Loading spinner during prediction
- Color-coded results
- Probability distribution bars

### 📝 History Page
- Table of all past predictions
- Color-coded rows (green/amber/red)
- Delete individual entries
- Clear all history
- Quick stats summary

### 📊 Analytics Page
- Bar chart: Congestion distribution
- Line chart: Predictions by hour
- Pie chart: Road type distribution
- Summary stat cards

### ℹ️ About Page
- App description
- ML model explanation
- Technology stack
- Features showcase
- How it works

---

## Configuration

### API Endpoint

The frontend connects to the Flask backend at `http://localhost:5000`

To change this, edit `src/pages/PredictPage.js`:

```javascript
const response = await fetch('http://localhost:5000/predict', {
  // ... rest of the code
});
```

### Port Configuration

**Frontend (React):**
- Default: http://localhost:3000
- To change: Set `PORT` environment variable

**Backend (Flask):**
- Default: http://localhost:5000
- To change: Edit `config.py` → `FLASK_PORT`

---

## Troubleshooting

### Issue: "npm: command not found"
**Solution:** Install Node.js from https://nodejs.org/

### Issue: "Cannot connect to API"
**Solution:**
1. Check Flask is running: `python app.py`
2. Verify Flask is on port 5000
3. Check browser console for CORS errors

### Issue: CORS Error
**Solution:** Install flask-cors:
```bash
pip install flask-cors
```

Add to `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

### Issue: "Module not found: recharts"
**Solution:**
```bash
npm install recharts
```

### Issue: Charts not displaying
**Solution:**
1. Make some predictions first
2. Check browser console for errors
3. Verify localStorage has data:
   - Open DevTools → Application → Local Storage
   - Look for `predictionHistory`

### Issue: Port 3000 already in use
**Solution:**
```bash
# Kill process on port 3000
npx kill-port 3000

# Or use different port
PORT=3001 npm start
```

---

## Development Tips

### Hot Reload
React automatically reloads when you save files. No need to restart!

### Browser DevTools
- Press `F12` to open DevTools
- Check Console for errors
- Use React DevTools extension

### LocalStorage Inspection
1. Open DevTools
2. Go to Application tab
3. Click Local Storage → http://localhost:3000
4. View `predictionHistory`

### Clear LocalStorage
```javascript
// In browser console
localStorage.clear()
```

---

## Building for Production

### Create Production Build

```bash
npm run build
```

This creates an optimized build in `build/` folder.

### Test Production Build

```bash
# Install serve
npm install -g serve

# Serve production build
serve -s build
```

### Deploy to Netlify

1. Build the app: `npm run build`
2. Drag `build/` folder to Netlify
3. Update API URL to production backend

### Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

---

## Environment Variables

Create `.env` file in `frontend/`:

```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_NAME=FlowSense AI
```

Use in code:
```javascript
const API_URL = process.env.REACT_APP_API_URL;
```

---

## Testing

### Run Tests
```bash
npm test
```

### Run Tests with Coverage
```bash
npm test -- --coverage
```

---

## Scripts

```bash
# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Eject (not recommended)
npm run eject
```

---

## Next Steps

1. ✅ Complete setup
2. ✅ Start both backend and frontend
3. ✅ Open http://localhost:3000
4. ✅ Click "Get Started"
5. ✅ Make your first prediction!

---

## Need Help?

- Check `README.md` for detailed documentation
- Review `API_DOCUMENTATION.md` in parent directory
- Open an issue on GitHub
- Check browser console for errors

---

**Happy Coding! 🚀**

Built with React, Flask, and Machine Learning

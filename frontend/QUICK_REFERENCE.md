# ⚡ FlowSense AI - Quick Reference

## 🚀 Start the App

```bash
# Terminal 1: Backend
python app.py

# Terminal 2: Frontend
cd frontend
npm install  # First time only
npm start
```

**Open:** http://localhost:3000

---

## 📁 File Structure

```
frontend/src/
├── App.js                    # Main app + routing
├── components/
│   └── MainLayout.js        # Navbar + Footer
└── pages/
    ├── LandingPage.js       # Entry page
    ├── PredictPage.js       # Prediction form
    ├── HistoryPage.js       # Past predictions
    ├── AnalyticsPage.js     # Charts
    └── AboutPage.js         # Info
```

---

## 🎨 Key Components

### Landing Page
- Animated background
- Glowing CTA button
- Navigate to `/predict`

### Predict Page
- Form with validation
- API call to Flask
- Save to localStorage
- Display results

### History Page
- Load from localStorage
- Display table
- Delete entries
- Show stats

### Analytics Page
- Load from localStorage
- Generate chart data
- Display 3 charts
- Show summary cards

---

## 🔌 API Call

```javascript
const response = await fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    features: [hour, day, count, road, weather] 
  })
});

const data = await response.json();
// data.traffic_level
// data.confidence
// data.probabilities
```

---

## 💾 LocalStorage

```javascript
// Save
const history = JSON.parse(localStorage.getItem('predictionHistory') || '[]');
history.unshift(newPrediction);
localStorage.setItem('predictionHistory', JSON.stringify(history));

// Load
const history = JSON.parse(localStorage.getItem('predictionHistory') || '[]');

// Clear
localStorage.removeItem('predictionHistory');
```

---

## 🎨 Styling

### Colors
```css
--bg-dark: #0d1117
--bg-card: #161b22
--border: #30363d
--primary: #58a6ff
--secondary: #1f6feb
--text: #c9d1d9
--muted: #8b949e
```

### Classes
```css
.card              /* Card container */
.btn               /* Button base */
.btn-primary       /* Primary button */
.btn-secondary     /* Secondary button */
.badge             /* Badge base */
.badge-low         /* Green badge */
.badge-medium      /* Amber badge */
.badge-high        /* Red badge */
.spinner           /* Loading spinner */
```

---

## 📊 Charts (Recharts)

```javascript
import { BarChart, LineChart, PieChart } from 'recharts';

// Bar Chart
<BarChart data={data}>
  <Bar dataKey="value" />
</BarChart>

// Line Chart
<LineChart data={data}>
  <Line dataKey="predictions" />
</LineChart>

// Pie Chart
<PieChart>
  <Pie data={data} dataKey="value" />
</PieChart>
```

---

## 🔄 Routing

```javascript
// Navigate programmatically
import { useNavigate } from 'react-router-dom';
const navigate = useNavigate();
navigate('/predict');

// Link component
import { NavLink } from 'react-router-dom';
<NavLink to="/predict">Predict</NavLink>
```

---

## 🐛 Common Issues

### API not connecting
```bash
# Check Flask is running
python app.py

# Check port
http://localhost:5000/health
```

### CORS error
```python
# Add to app.py
from flask_cors import CORS
CORS(app)
```

### Charts not showing
```bash
# Install recharts
npm install recharts

# Make predictions first
# Check localStorage has data
```

### Port in use
```bash
# Kill port 3000
npx kill-port 3000

# Or use different port
PORT=3001 npm start
```

---

## 📦 Scripts

```bash
npm start          # Start dev server
npm run build      # Build for production
npm test           # Run tests
```

---

## 🔧 Quick Edits

### Change API URL
`src/pages/PredictPage.js` line ~60

### Change colors
`src/App.css` and `src/index.css`

### Add nav link
`src/components/MainLayout.js`

### Add route
`src/App.js`

---

## 📱 Responsive

```css
/* Desktop */
@media (min-width: 969px) { }

/* Tablet */
@media (max-width: 968px) { }

/* Mobile */
@media (max-width: 768px) { }
```

---

## ✅ Checklist

- [ ] Backend running on :5000
- [ ] Frontend running on :3000
- [ ] npm install completed
- [ ] Browser opened
- [ ] First prediction made
- [ ] History showing
- [ ] Analytics displaying

---

## 🆘 Help

- Check browser console (F12)
- Check terminal for errors
- Read `SETUP_GUIDE.md`
- Read `README.md`

---

**Quick Start:** `npm install && npm start`

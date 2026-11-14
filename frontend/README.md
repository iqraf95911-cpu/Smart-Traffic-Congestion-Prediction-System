# FlowSense AI - React Frontend

A modern, responsive React application for traffic congestion prediction with analytics and history tracking.

## 🚀 Features

### 1. Landing Page
- Full-screen animated landing page
- Glowing CTA button with smooth animations
- CSS-only animated traffic background
- Smooth transition to main app

### 2. Navigation
- Sticky navbar with logo and app name
- Active route highlighting
- Mobile-responsive hamburger menu
- Links to: Predict, History, Analytics, About

### 3. Prediction Form
- Enhanced form with validation
- Animated loading spinner
- Color-coded results (green/amber/red)
- Confidence scores and probability distribution
- Reset form button
- Inline error messages

### 4. History Page
- LocalStorage-based prediction history
- Sortable table with all past predictions
- Color-coded rows by congestion level
- Delete individual entries or clear all
- Quick stats summary

### 5. Analytics Dashboard
- **Bar Chart**: Congestion distribution (Low/Medium/High)
- **Line Chart**: Predictions over time by hour
- **Pie Chart**: Road type distribution
- Summary stat cards:
  - Total Predictions
  - Most Common Result
  - Peak Hour

### 6. About Page
- App description and features
- ML model explanation
- Technology stack showcase
- How it works workflow
- CTA to make predictions

### 7. General Polish
- Dark theme (#0d1117 background, cyan/blue accents)
- Smooth hover animations
- Fully mobile responsive
- Footer with branding

## 📦 Installation

### Prerequisites
- Node.js 14+ and npm
- Python Flask backend running on http://localhost:5000

### Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm start
   ```

4. **Open browser:**
   Navigate to http://localhost:3000

## 🏗️ Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── MainLayout.js
│   │   └── MainLayout.css
│   ├── pages/
│   │   ├── LandingPage.js
│   │   ├── LandingPage.css
│   │   ├── PredictPage.js
│   │   ├── PredictPage.css
│   │   ├── HistoryPage.js
│   │   ├── HistoryPage.css
│   │   ├── AnalyticsPage.js
│   │   ├── AnalyticsPage.css
│   │   ├── AboutPage.js
│   │   └── AboutPage.css
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## 🔌 API Integration

The app connects to the Flask backend API at `http://localhost:5000/predict`

**Request Format:**
```json
{
  "features": [hour, day, vehicleCount, roadType, weather]
}
```

**Response Format:**
```json
{
  "traffic_level": "High",
  "traffic_level_code": 2,
  "confidence": 60.0,
  "probabilities": {
    "Low": 40.0,
    "Medium": 0.0,
    "High": 60.0
  }
}
```

## 🎨 Customization

### Colors
Edit `src/App.css` and `src/index.css` to change the color scheme:
- Primary: `#58a6ff` (cyan blue)
- Secondary: `#1f6feb` (darker blue)
- Background: `#0d1117` (dark)
- Cards: `#161b22` (slightly lighter)

### Animations
All animations are CSS-based and can be modified in individual component CSS files.

## 📱 Responsive Breakpoints

- Desktop: > 968px
- Tablet: 768px - 968px
- Mobile: < 768px

## 🧪 Testing

```bash
npm test
```

## 🏗️ Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## 📊 LocalStorage Structure

**Prediction History:**
```json
[
  {
    "id": 1234567890,
    "timestamp": "2025-05-18T12:00:00.000Z",
    "inputs": {
      "hour": "8",
      "day": "Monday",
      "vehicleCount": "120",
      "roadType": "Highway",
      "weather": "Clear"
    },
    "result": "High",
    "confidence": 60.0,
    "probabilities": {
      "Low": 40.0,
      "Medium": 0.0,
      "High": 60.0
    }
  }
]
```

## 🔧 Troubleshooting

### CORS Issues
If you encounter CORS errors, make sure the Flask backend has CORS enabled:

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

### API Connection Failed
1. Ensure Flask backend is running on port 5000
2. Check the API URL in `PredictPage.js`
3. Verify network connectivity

### Charts Not Displaying
1. Ensure Recharts is installed: `npm install recharts`
2. Check browser console for errors
3. Verify data format matches chart requirements

## 🚀 Deployment

### Deploy to Netlify/Vercel

1. Build the app:
   ```bash
   npm run build
   ```

2. Deploy the `build/` folder to your hosting service

3. Update API URL in `PredictPage.js` to your production backend URL

### Environment Variables

Create `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
```

Update API calls to use:
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
```

## 📝 License

MIT License - Built with ❤️ for FlowSense AI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Built with React, Recharts, and modern CSS animations**

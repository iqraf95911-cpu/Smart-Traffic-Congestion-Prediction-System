# 🚦 Smart Traffic Congestion Prediction System

An AI-powered web application that predicts traffic congestion levels using machine learning. Built with Flask, scikit-learn, and a modern glassmorphic UI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Real-time Traffic Prediction**: Predict traffic congestion levels (Low, Medium, High) based on multiple factors
- **Confidence Scores**: Get probability distributions for all traffic levels
- **Modern UI**: Beautiful glassmorphic design with smooth animations
- **RESTful API**: Well-documented API endpoints for integration
- **Batch Predictions**: Support for predicting multiple scenarios at once
- **Model Metrics**: Comprehensive evaluation metrics and visualizations
- **Input Validation**: Robust validation for all input parameters
- **Error Handling**: Graceful error handling with informative messages

## 📊 Model Features

The prediction model considers the following factors:

1. **Hour of Day** (0-23): Time of day in 24-hour format
2. **Day of Week** (0-6): Monday=0, Sunday=6
3. **Vehicle Count** (0-500): Number of vehicles on the road
4. **Road Type**: City, Highway, or Residential
5. **Weather Condition**: Clear, Fog, or Rain

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Smart-Traffic-Congestion-Prediction-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate training data** (if needed)
   ```bash
   cd data
   python generate_data.py
   cd ..
   ```

4. **Train the model**
   ```bash
   cd src
   python train_model.py
   cd ..
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Smart-Traffic-Congestion-Prediction-System/
│
├── app.py                      # Flask application with API endpoints
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── data/
│   ├── generate_data.py       # Script to generate synthetic traffic data
│   └── traffic_data.csv       # Training dataset
│
├── src/
│   ├── preprocess.py          # Data preprocessing module
│   ├── train_model.py         # Model training script
│   └── predict.py             # Prediction module
│
├── templates/
│   └── index.html             # Web interface
│
├── notebook/
│   └── exploration.ipynb      # Jupyter notebook for data exploration
│
├── model.pkl                   # Trained model (generated)
├── encoders.pkl               # Label encoders (generated)
├── model_metrics.pkl          # Model performance metrics (generated)
├── confusion_matrix.png       # Confusion matrix visualization (generated)
└── feature_importance.png     # Feature importance plot (generated)
```

## 🔌 API Endpoints

### 1. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Service is running",
  "model_path": "path/to/model.pkl"
}
```

### 2. Single Prediction
```http
POST /predict
Content-Type: application/json

{
  "features": [8, 1, 120, 1, 0]
}
```

**Response:**
```json
{
  "traffic_level": "Medium",
  "traffic_level_code": 1,
  "confidence": 85.5,
  "probabilities": {
    "Low": 5.2,
    "Medium": 85.5,
    "High": 9.3
  }
}
```

### 3. Batch Prediction
```http
POST /predict/batch
Content-Type: application/json

{
  "features_list": [
    [8, 1, 120, 1, 0],
    [14, 3, 50, 2, 0],
    [18, 4, 180, 0, 2]
  ]
}
```

### 4. Model Information
```http
GET /info
```

**Response:**
```json
{
  "model_type": "Random Forest Classifier",
  "features": [...],
  "output_classes": ["Low", "Medium", "High"]
}
```

## 📈 Model Performance

After training, the model generates:

- **Accuracy Score**: Overall prediction accuracy
- **Precision, Recall, F1-Score**: Detailed metrics per class
- **Confusion Matrix**: Visual representation of predictions vs actual
- **Feature Importance**: Which features contribute most to predictions

Example output:
```
============================================================
📊 MODEL PERFORMANCE METRICS
============================================================
Accuracy:  0.9250 (92.50%)
Precision: 0.9245
Recall:    0.9250
F1-Score:  0.9247
============================================================
```

## 🎨 User Interface

The web interface features:

- **Glassmorphic Design**: Modern, translucent UI elements
- **Responsive Layout**: Works on desktop and mobile devices
- **Real-time Validation**: Instant feedback on input values
- **Animated Results**: Smooth transitions and loading states
- **Color-coded Predictions**: Visual indicators for traffic levels
  - 🟢 Green: Low traffic
  - 🟡 Yellow: Medium traffic
  - 🔴 Red: High traffic

## 🛠️ Configuration

Edit `config.py` to customize:

- Model parameters (n_estimators, max_depth)
- File paths
- Feature ranges
- Flask settings (host, port, debug mode)

## 📊 Data Generation

The `generate_data.py` script creates synthetic traffic data with realistic patterns:

- **Peak hours**: Increased traffic during morning (8-9 AM) and evening (5-7 PM)
- **Weekend effect**: Reduced traffic on weekends
- **Weather impact**: Higher congestion during rain and fog
- **Road type variations**: Different patterns for highways, city roads, and residential areas

## 🧪 Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:5000/health

# Make a prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [8, 1, 120, 1, 0]}'

# Get model info
curl http://localhost:5000/info
```

### Using Python

```python
import requests

# Make a prediction
response = requests.post(
    'http://localhost:5000/predict',
    json={'features': [8, 1, 120, 1, 0]}
)

result = response.json()
print(f"Traffic Level: {result['traffic_level']}")
print(f"Confidence: {result['confidence']}%")
```

## 🔧 Troubleshooting

### Model not found error
```bash
# Train the model first
cd src
python train_model.py
cd ..
```

### Port already in use
Edit `config.py` and change `FLASK_PORT` to a different port.

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📝 Future Enhancements

- [ ] Real-time traffic data integration
- [ ] Historical trend analysis
- [ ] Route optimization suggestions
- [ ] Mobile application
- [ ] Integration with mapping services
- [ ] Multi-city support
- [ ] Advanced weather integration
- [ ] Traffic incident detection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Built with ❤️ by Ayush

## 🙏 Acknowledgments

- Flask framework for the web application
- scikit-learn for machine learning capabilities
- The open-source community for inspiration and tools

---

**Note**: This is a demonstration project using synthetic data. For production use, integrate with real traffic data sources and perform thorough validation.

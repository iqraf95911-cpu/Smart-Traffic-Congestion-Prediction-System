# 📡 API Documentation

Complete API reference for the Smart Traffic Congestion Prediction System.

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, no authentication is required. For production deployment, implement proper authentication mechanisms.

---

## Endpoints

### 1. Health Check

Check if the API service is running and the model is loaded.

**Endpoint:** `GET /health`

**Response:**

```json
{
  "status": "healthy",
  "message": "Service is running",
  "model_path": "/path/to/model.pkl"
}
```

**Status Codes:**
- `200 OK`: Service is healthy
- `503 Service Unavailable`: Model not loaded

**Example:**

```bash
curl http://localhost:5000/health
```

---

### 2. Single Prediction

Predict traffic congestion level for a single scenario.

**Endpoint:** `POST /predict`

**Request Body:**

```json
{
  "features": [hour, day, vehicle_count, road_type, weather]
}
```

**Parameters:**

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| hour | int | 0-23 | Hour of the day (24-hour format) |
| day | int | 0-6 | Day of the week (0=Monday, 6=Sunday) |
| vehicle_count | int | 0-500 | Number of vehicles |
| road_type | int | 0-2 | 0=City, 1=Highway, 2=Residential |
| weather | int | 0-2 | 0=Clear, 1=Fog, 2=Rain |

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

**Status Codes:**
- `200 OK`: Prediction successful
- `400 Bad Request`: Invalid input
- `503 Service Unavailable`: Model not loaded

**Example:**

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "features": [8, 1, 150, 1, 0]
  }'
```

**Python Example:**

```python
import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={'features': [8, 1, 150, 1, 0]}
)

result = response.json()
print(f"Traffic Level: {result['traffic_level']}")
print(f"Confidence: {result['confidence']}%")
```

---

### 3. Batch Prediction

Predict traffic congestion for multiple scenarios at once.

**Endpoint:** `POST /predict/batch`

**Request Body:**

```json
{
  "features_list": [
    [8, 1, 150, 1, 0],
    [14, 3, 50, 2, 0],
    [18, 4, 180, 0, 2]
  ]
}
```

**Response:**

```json
{
  "predictions": [
    {
      "traffic_level": "High",
      "traffic_level_code": 2,
      "confidence": 92.3,
      "probabilities": {
        "Low": 2.1,
        "Medium": 5.6,
        "High": 92.3
      }
    },
    {
      "traffic_level": "Low",
      "traffic_level_code": 0,
      "confidence": 88.7,
      "probabilities": {
        "Low": 88.7,
        "Medium": 9.2,
        "High": 2.1
      }
    },
    {
      "traffic_level": "High",
      "traffic_level_code": 2,
      "confidence": 95.1,
      "probabilities": {
        "Low": 1.2,
        "Medium": 3.7,
        "High": 95.1
      }
    }
  ],
  "count": 3
}
```

**Status Codes:**
- `200 OK`: Predictions successful
- `400 Bad Request`: Invalid input format
- `503 Service Unavailable`: Model not loaded

**Example:**

```bash
curl -X POST http://localhost:5000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{
    "features_list": [
      [8, 1, 150, 1, 0],
      [14, 3, 50, 2, 0],
      [18, 4, 180, 0, 2]
    ]
  }'
```

**Python Example:**

```python
import requests

scenarios = [
    [8, 1, 150, 1, 0],   # Morning rush
    [14, 3, 50, 2, 0],   # Afternoon
    [18, 4, 180, 0, 2]   # Evening rain
]

response = requests.post(
    'http://localhost:5000/predict/batch',
    json={'features_list': scenarios}
)

results = response.json()
for i, pred in enumerate(results['predictions']):
    print(f"Scenario {i+1}: {pred['traffic_level']} ({pred['confidence']}%)")
```

---

### 4. Model Information

Get information about the model and its features.

**Endpoint:** `GET /info`

**Response:**

```json
{
  "model_type": "Random Forest Classifier",
  "features": [
    {
      "name": "hour",
      "range": "0-23",
      "description": "Hour of the day"
    },
    {
      "name": "day",
      "range": "0-6",
      "description": "Day of the week (0=Monday)"
    },
    {
      "name": "vehicle_count",
      "range": "0-500",
      "description": "Number of vehicles"
    },
    {
      "name": "road_type",
      "range": "0-2",
      "description": "Type of road (0=city, 1=highway, 2=residential)"
    },
    {
      "name": "weather",
      "range": "0-2",
      "description": "Weather condition (0=clear, 1=fog, 2=rain)"
    }
  ],
  "output_classes": ["Low", "Medium", "High"]
}
```

**Status Codes:**
- `200 OK`: Information retrieved successfully
- `503 Service Unavailable`: Model not loaded

**Example:**

```bash
curl http://localhost:5000/info
```

---

## Error Responses

### 400 Bad Request

```json
{
  "error": "Invalid input: hour must be between 0 and 23, got 25"
}
```

### 404 Not Found

```json
{
  "error": "Endpoint not found"
}
```

### 500 Internal Server Error

```json
{
  "error": "An error occurred during prediction. Please try again."
}
```

### 503 Service Unavailable

```json
{
  "error": "Model not loaded. Please train the model first."
}
```

---

## Rate Limiting

Currently, no rate limiting is implemented. For production use, consider implementing rate limiting to prevent abuse.

---

## CORS

CORS is not configured by default. To enable CORS for cross-origin requests, install `flask-cors`:

```bash
pip install flask-cors
```

Then add to `app.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

---

## Best Practices

### 1. Input Validation

Always validate inputs on the client side before sending requests:

```javascript
function validateFeatures(features) {
  const [hour, day, count, road, weather] = features;
  
  if (hour < 0 || hour > 23) return false;
  if (day < 0 || day > 6) return false;
  if (count < 0 || count > 500) return false;
  if (road < 0 || road > 2) return false;
  if (weather < 0 || weather > 2) return false;
  
  return true;
}
```

### 2. Error Handling

Always handle errors gracefully:

```python
try:
    response = requests.post(url, json=data, timeout=5)
    response.raise_for_status()
    result = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

### 3. Batch Processing

For multiple predictions, use the batch endpoint instead of multiple single requests:

```python
# ❌ Bad: Multiple requests
for features in features_list:
    response = requests.post('/predict', json={'features': features})

# ✅ Good: Single batch request
response = requests.post('/predict/batch', json={'features_list': features_list})
```

---

## Testing

Use the provided test script:

```bash
python test_api.py
```

Or test individual endpoints:

```python
import requests

# Test health
response = requests.get('http://localhost:5000/health')
print(response.json())

# Test prediction
response = requests.post(
    'http://localhost:5000/predict',
    json={'features': [8, 1, 150, 1, 0]}
)
print(response.json())
```

---

## Deployment Considerations

### Production Checklist

- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Implement authentication and authorization
- [ ] Add rate limiting
- [ ] Enable HTTPS
- [ ] Set up logging and monitoring
- [ ] Configure CORS properly
- [ ] Add request validation middleware
- [ ] Implement caching for frequent requests
- [ ] Set up health checks and alerts
- [ ] Use environment variables for configuration

### Example Production Setup

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Support

For issues or questions:
- Open an issue on GitHub
- Check the [README](README.md) for general information
- See [QUICKSTART](QUICKSTART.md) for setup help

---

**Last Updated:** May 18, 2026

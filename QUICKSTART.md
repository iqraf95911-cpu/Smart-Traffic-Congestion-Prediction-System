# 🚀 Quick Start Guide

Get up and running with the Smart Traffic Congestion Prediction System in 5 minutes!

## ⚡ Super Quick Start (One Command)

```bash
python setup.py && python run.py
```

That's it! The application will be available at `http://localhost:5000`

## 📋 Step-by-Step Guide

### 1. Install Dependencies (30 seconds)

```bash
pip install -r requirements.txt
```

### 2. Setup and Train (2-3 minutes)

```bash
python setup.py
```

This will:
- ✅ Check Python version
- ✅ Install dependencies
- ✅ Generate training data
- ✅ Train the ML model

### 3. Run the Application (5 seconds)

```bash
python app.py
```

### 4. Open Your Browser

Navigate to: `http://localhost:5000`

## 🎮 Try It Out

### Using the Web Interface

1. **Fill in the form:**
   - Hour: `8` (morning rush hour)
   - Day: `Monday`
   - Vehicle Count: `150`
   - Road Type: `Highway`
   - Weather: `Clear`

2. **Click "Predict Traffic"**

3. **See the results:**
   - Traffic level prediction
   - Confidence score
   - Probability distribution

### Using the API

```bash
# Test the API
python test_api.py
```

Or use cURL:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [8, 1, 150, 1, 0]}'
```

## 🎯 Common Use Cases

### Scenario 1: Morning Rush Hour
```json
{
  "features": [8, 1, 150, 1, 0]
}
```
- Hour: 8 AM
- Day: Monday
- Vehicles: 150
- Road: Highway
- Weather: Clear

**Expected Result:** High traffic congestion

### Scenario 2: Late Night
```json
{
  "features": [2, 6, 20, 2, 0]
}
```
- Hour: 2 AM
- Day: Sunday
- Vehicles: 20
- Road: Residential
- Weather: Clear

**Expected Result:** Low traffic congestion

### Scenario 3: Rainy Evening
```json
{
  "features": [18, 4, 180, 0, 2]
}
```
- Hour: 6 PM
- Day: Friday
- Vehicles: 180
- Road: City
- Weather: Rain

**Expected Result:** High traffic congestion

## 🔧 Troubleshooting

### "Model not found" error
```bash
cd src
python train_model.py
cd ..
```

### Port 5000 already in use
Edit `config.py` and change `FLASK_PORT` to `5001` (or any available port)

### Import errors
```bash
pip install -r requirements.txt --force-reinstall
```

### Can't connect to server
Make sure the Flask app is running:
```bash
python app.py
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Explore the [API endpoints](README.md#-api-endpoints)
- Customize the model in `config.py`

## 💡 Pro Tips

1. **Quick restart:** Use `python run.py` - it checks if model exists and starts the server
2. **API testing:** Use `test_api.py` to test all endpoints at once
3. **Custom data:** Edit `data/generate_data.py` to create custom training scenarios
4. **Model tuning:** Adjust parameters in `config.py` and retrain

## 🎉 You're All Set!

Start predicting traffic congestion and explore the features. Happy coding! 🚦

---

**Need help?** Open an issue on GitHub or check the documentation.

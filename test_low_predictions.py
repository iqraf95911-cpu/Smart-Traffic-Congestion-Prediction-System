"""
Test script to verify the model can predict Low traffic levels
"""
import pickle
import pandas as pd

# Load model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

# Test cases that should predict Low traffic
test_cases = [
    {'hour': 2, 'day': 5, 'vehicle_count': 25, 'road_type': 'residential', 'weather': 'clear'},
    {'hour': 14, 'day': 6, 'vehicle_count': 30, 'road_type': 'city', 'weather': 'clear'},
    {'hour': 23, 'day': 0, 'vehicle_count': 40, 'road_type': 'highway', 'weather': 'clear'},
    {'hour': 3, 'day': 3, 'vehicle_count': 20, 'road_type': 'residential', 'weather': 'clear'},
    {'hour': 11, 'day': 6, 'vehicle_count': 35, 'road_type': 'highway', 'weather': 'clear'},
]

print('Testing Low Traffic Predictions:')
print('=' * 80)

for i, test in enumerate(test_cases, 1):
    # Encode categorical features
    test_encoded = test.copy()
    test_encoded['road_type'] = encoders['road_type'].transform([test['road_type']])[0]
    test_encoded['weather'] = encoders['weather'].transform([test['weather']])[0]
    
    # Create DataFrame
    X = pd.DataFrame([test_encoded])
    
    # Predict
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = max(probabilities) * 100
    
    # Get class names
    traffic_levels = encoders['traffic_level'].classes_
    predicted_level = traffic_levels[prediction]
    
    # Get probabilities for each class
    low_idx = list(traffic_levels).index('Low')
    medium_idx = list(traffic_levels).index('Medium')
    high_idx = list(traffic_levels).index('High')
    
    print(f'Test {i}:')
    print(f'  Input: Hour={test["hour"]}, Day={test["day"]}, Vehicles={test["vehicle_count"]}, Road={test["road_type"]}, Weather={test["weather"]}')
    print(f'  Prediction: {predicted_level} (Confidence: {confidence:.1f}%)')
    print(f'  Probabilities: Low={probabilities[low_idx]*100:.1f}%, Medium={probabilities[medium_idx]*100:.1f}%, High={probabilities[high_idx]*100:.1f}%')
    print()

print('=' * 80)
print('Summary: All test cases should predict "Low" traffic level')

"""
API testing script for the Smart Traffic Congestion Prediction System
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:5000"

def print_response(title: str, response: requests.Response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"📡 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2))

def test_health_check():
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print_response("Health Check", response)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server.")
        print("   Make sure the Flask app is running (python app.py)")
        return False

def test_single_prediction():
    """Test single prediction endpoint"""
    # Test case: Morning rush hour, weekday, high vehicle count, highway, clear weather
    data = {
        "features": [8, 1, 150, 1, 0]
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print_response("Single Prediction (Rush Hour)", response)
    return response.status_code == 200

def test_batch_prediction():
    """Test batch prediction endpoint"""
    data = {
        "features_list": [
            [8, 1, 150, 1, 0],   # Morning rush hour
            [14, 3, 50, 2, 0],   # Afternoon, residential
            [18, 4, 180, 0, 2],  # Evening rush, city, rain
            [2, 6, 20, 2, 0]     # Late night, weekend, residential
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/predict/batch",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print_response("Batch Prediction", response)
    return response.status_code == 200

def test_model_info():
    """Test model info endpoint"""
    response = requests.get(f"{BASE_URL}/info")
    print_response("Model Information", response)
    return response.status_code == 200

def test_invalid_input():
    """Test error handling with invalid input"""
    # Test with invalid hour value
    data = {
        "features": [25, 1, 150, 1, 0]  # Hour > 23
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print_response("Invalid Input Test (Expected Error)", response)
    return response.status_code == 400

def test_missing_data():
    """Test error handling with missing data"""
    data = {}  # Empty data
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print_response("Missing Data Test (Expected Error)", response)
    return response.status_code == 400

def run_all_tests():
    """Run all API tests"""
    print("=" * 60)
    print("🧪 Starting API Tests")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health_check),
        ("Single Prediction", test_single_prediction),
        ("Batch Prediction", test_batch_prediction),
        ("Model Information", test_model_info),
        ("Invalid Input Handling", test_invalid_input),
        ("Missing Data Handling", test_missing_data)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ Error in {test_name}: {str(e)}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    print("=" * 60)
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)

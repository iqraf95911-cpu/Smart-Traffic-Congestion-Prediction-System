"""
Quick test to verify the API is working
Run this while the Flask app is running
"""
import requests
import json

BASE_URL = "http://localhost:5000"

print("=" * 60)
print("🧪 Quick API Test")
print("=" * 60)

# Test 1: Health Check
print("\n1. Testing Health Check...")
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   Make sure Flask app is running: python app.py")
    exit(1)

# Test 2: Single Prediction
print("\n2. Testing Prediction...")
try:
    data = {"features": [8, 1, 120, 1, 0]}
    response = requests.post(
        f"{BASE_URL}/predict",
        json=data,
        headers={"Content-Type": "application/json"},
        timeout=5
    )
    print(f"   Status: {response.status_code}")
    result = response.json()
    print(f"   Traffic Level: {result.get('traffic_level', 'N/A')}")
    print(f"   Confidence: {result.get('confidence', 'N/A')}%")
    print(f"   Response: {json.dumps(result, indent=2)}")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 60)
print("✅ Test Complete!")
print("=" * 60)
print("\nNow open your browser: http://localhost:5000")

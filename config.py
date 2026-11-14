"""
Configuration file for the Smart Traffic Congestion Prediction System
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Data paths
DATA_DIR = BASE_DIR / "data"
TRAFFIC_DATA_PATH = DATA_DIR / "traffic_data.csv"

# Model paths
MODEL_DIR = BASE_DIR
MODEL_PATH = MODEL_DIR / "model.pkl"
ENCODERS_PATH = MODEL_DIR / "encoders.pkl"
METRICS_PATH = MODEL_DIR / "model_metrics.pkl"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 100
MAX_DEPTH = 10

# Traffic level mappings
TRAFFIC_LEVELS = {
    0: "Low",
    1: "Medium",
    2: "High"
}

# Feature ranges for validation
FEATURE_RANGES = {
    "hour": (0, 23),
    "day": (0, 6),
    "vehicle_count": (0, 500),
    "road_type": (0, 2),
    "weather": (0, 2)
}

# Flask configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

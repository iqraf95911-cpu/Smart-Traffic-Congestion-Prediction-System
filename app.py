"""
Flask API for Smart Traffic Congestion Prediction System
"""
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import logging
from pathlib import Path
import sys
import json
from datetime import datetime

# Add src directory to path
sys.path.append(str(Path(__file__).parent / 'src'))
from predict import TrafficPredictor
from config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG, MODEL_PATH

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for React frontend
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

# Stats file path
STATS_FILE = Path(__file__).parent / 'data' / 'stats.json'
STATS_FILE.parent.mkdir(exist_ok=True)

# Initialize predictor
try:
    predictor = TrafficPredictor()
    logger.info("✓ Traffic predictor initialized successfully")
except Exception as e:
    logger.error(f"❌ Failed to initialize predictor: {str(e)}")
    predictor = None


@app.route("/")
def home():
    """Render the home page"""
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    if predictor is None:
        return jsonify({
            "status": "unhealthy",
            "message": "Model not loaded"
        }), 503
    
    return jsonify({
        "status": "healthy",
        "message": "Service is running",
        "model_path": str(MODEL_PATH)
    }), 200


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict traffic congestion level
    
    Expected JSON format:
    {
        "features": [hour, day, vehicle_count, road_type, weather]
    }
    """
    try:
        # Check if predictor is initialized
        if predictor is None:
            return jsonify({
                "error": "Model not loaded. Please train the model first."
            }), 503
        
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "No data provided. Please send JSON data."
            }), 400
        
        if "features" not in data:
            return jsonify({
                "error": "Missing 'features' key in request data."
            }), 400
        
        features = data["features"]
        
        # Make prediction
        result = predictor.predict(features)
        
        # Log prediction with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f"[{timestamp}] Prediction: {result['traffic_level']} (confidence: {result['confidence']}%) | Input: {features}")
        
        # Save to stats
        save_prediction_stats(result, features)
        
        return jsonify(result), 200
        
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        return jsonify({
            "error": f"Invalid input: {str(e)}"
        }), 400
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({
            "error": "An error occurred during prediction. Please try again."
        }), 500


@app.route("/predict/batch", methods=["POST"])
def predict_batch():
    """
    Predict traffic congestion for multiple inputs
    
    Expected JSON format:
    {
        "features_list": [
            [hour, day, vehicle_count, road_type, weather],
            [hour, day, vehicle_count, road_type, weather],
            ...
        ]
    }
    """
    try:
        if predictor is None:
            return jsonify({
                "error": "Model not loaded. Please train the model first."
            }), 503
        
        data = request.get_json()
        
        if not data or "features_list" not in data:
            return jsonify({
                "error": "Missing 'features_list' key in request data."
            }), 400
        
        features_list = data["features_list"]
        
        if not isinstance(features_list, list):
            return jsonify({
                "error": "'features_list' must be a list of feature arrays."
            }), 400
        
        results = predictor.predict_batch(features_list)
        
        logger.info(f"Batch prediction completed for {len(features_list)} samples")
        
        return jsonify({
            "predictions": results,
            "count": len(results)
        }), 200
        
    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        return jsonify({
            "error": "An error occurred during batch prediction."
        }), 500


@app.route("/info", methods=["GET"])
def model_info():
    """Get model information"""
    try:
        if predictor is None:
            return jsonify({
                "error": "Model not loaded"
            }), 503
        
        return jsonify({
            "model_type": "Random Forest Classifier",
            "features": [
                {"name": "hour", "range": "0-23", "description": "Hour of the day"},
                {"name": "day", "range": "0-6", "description": "Day of the week (0=Monday)"},
                {"name": "vehicle_count", "range": "0-500", "description": "Number of vehicles"},
                {"name": "road_type", "range": "0-2", "description": "Type of road (0=city, 1=highway, 2=residential)"},
                {"name": "weather", "range": "0-2", "description": "Weather condition (0=clear, 1=fog, 2=rain)"}
            ],
            "output_classes": ["Low", "Medium", "High"]
        }), 200
        
    except Exception as e:
        logger.error(f"Info error: {str(e)}")
        return jsonify({
            "error": "Failed to retrieve model information"
        }), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Get aggregate prediction statistics"""
    try:
        if not STATS_FILE.exists():
            return jsonify({
                "total_predictions": 0,
                "predictions_by_level": {"Low": 0, "Medium": 0, "High": 0},
                "recent_predictions": [],
                "average_confidence": 0
            }), 200
        
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
        
        return jsonify(stats), 200
        
    except Exception as e:
        logger.error(f"Stats error: {str(e)}")
        return jsonify({
            "error": "Failed to retrieve stats"
        }), 500


def save_prediction_stats(result, features):
    """Save prediction statistics to JSON file"""
    try:
        # Load existing stats
        if STATS_FILE.exists():
            with open(STATS_FILE, 'r') as f:
                stats = json.load(f)
        else:
            stats = {
                "total_predictions": 0,
                "predictions_by_level": {"Low": 0, "Medium": 0, "High": 0},
                "recent_predictions": [],
                "average_confidence": 0
            }
        
        # Update stats
        stats["total_predictions"] += 1
        level = result["traffic_level"]
        stats["predictions_by_level"][level] = stats["predictions_by_level"].get(level, 0) + 1
        
        # Add to recent predictions (keep last 100)
        recent_pred = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "confidence": result["confidence"],
            "features": features
        }
        stats["recent_predictions"].insert(0, recent_pred)
        stats["recent_predictions"] = stats["recent_predictions"][:100]
        
        # Update average confidence
        total_confidence = sum(p["confidence"] for p in stats["recent_predictions"])
        stats["average_confidence"] = round(total_confidence / len(stats["recent_predictions"]), 2)
        
        # Save stats
        with open(STATS_FILE, 'w') as f:
            json.dump(stats, f, indent=2)
            
    except Exception as e:
        logger.error(f"Error saving stats: {str(e)}")


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("🚀 Starting Smart Traffic Congestion Prediction API")
    logger.info("=" * 60)
    logger.info(f"Host: {FLASK_HOST}")
    logger.info(f"Port: {FLASK_PORT}")
    logger.info(f"Debug: {FLASK_DEBUG}")
    logger.info("=" * 60)
    
    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
        use_reloader=False
    )

"""
Prediction module for traffic congestion
"""
import pickle
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from config import MODEL_PATH, TRAFFIC_LEVELS, FEATURE_RANGES


class TrafficPredictor:
    """Traffic congestion predictor class"""
    
    def __init__(self):
        """Initialize the predictor by loading the trained model"""
        try:
            with open(MODEL_PATH, 'rb') as f:
                self.model = pickle.load(f)
            print(f"✓ Model loaded from {MODEL_PATH}")
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. "
                "Please train the model first using: python src/train_model.py"
            )
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def validate_input(self, features):
        """
        Validate input features
        
        Args:
            features (list): List of feature values [hour, day, vehicle_count, road_type, weather]
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if len(features) != 5:
            return False, f"Expected 5 features, got {len(features)}"
        
        feature_names = ["hour", "day", "vehicle_count", "road_type", "weather"]
        
        for i, (name, value) in enumerate(zip(feature_names, features)):
            try:
                value = float(value)
                min_val, max_val = FEATURE_RANGES[name]
                
                if not (min_val <= value <= max_val):
                    return False, f"{name} must be between {min_val} and {max_val}, got {value}"
            except (ValueError, TypeError):
                return False, f"{name} must be a number, got {value}"
        
        return True, None
    
    def predict(self, features):
        """
        Predict traffic congestion level
        
        Args:
            features (list): List of feature values [hour, day, vehicle_count, road_type, weather]
            
        Returns:
            dict: Prediction result with level and confidence
        """
        # Validate input
        is_valid, error_msg = self.validate_input(features)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Prepare data with feature names to avoid sklearn warning
        import pandas as pd
        feature_names = ['hour', 'day', 'vehicle_count', 'road_type', 'weather']
        data = pd.DataFrame([features], columns=feature_names)
        
        # Make prediction
        prediction = self.model.predict(data)[0]
        probabilities = self.model.predict_proba(data)[0]
        
        # Get confidence
        confidence = float(probabilities[prediction])
        
        result = {
            'traffic_level': TRAFFIC_LEVELS[prediction],
            'traffic_level_code': int(prediction),
            'confidence': round(confidence * 100, 2),
            'probabilities': {
                TRAFFIC_LEVELS[i]: round(float(prob) * 100, 2) 
                for i, prob in enumerate(probabilities)
            }
        }
        
        return result
    
    def predict_batch(self, features_list):
        """
        Predict traffic congestion for multiple inputs
        
        Args:
            features_list (list): List of feature arrays
            
        Returns:
            list: List of prediction results
        """
        results = []
        for features in features_list:
            try:
                result = self.predict(features)
                results.append(result)
            except ValueError as e:
                results.append({'error': str(e)})
        
        return results


def main():
    """Example usage of the predictor"""
    predictor = TrafficPredictor()
    
    # Example prediction
    example_features = [8, 1, 120, 1, 0]  # hour, day, vehicle_count, road_type, weather
    
    print("\n" + "=" * 60)
    print("🔮 Traffic Prediction Example")
    print("=" * 60)
    print(f"Input features: {example_features}")
    print(f"  - Hour: {example_features[0]}")
    print(f"  - Day: {example_features[1]}")
    print(f"  - Vehicle Count: {example_features[2]}")
    print(f"  - Road Type: {example_features[3]}")
    print(f"  - Weather: {example_features[4]}")
    
    result = predictor.predict(example_features)
    
    print("\n📊 Prediction Result:")
    print(f"  - Traffic Level: {result['traffic_level']}")
    print(f"  - Confidence: {result['confidence']}%")
    print(f"\n  Probabilities:")
    for level, prob in result['probabilities'].items():
        print(f"    - {level}: {prob}%")
    print("=" * 60)


if __name__ == "__main__":
    main()

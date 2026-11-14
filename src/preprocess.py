"""
Data preprocessing module for traffic prediction
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from config import TRAFFIC_DATA_PATH, ENCODERS_PATH, RANDOM_STATE, TEST_SIZE


def preprocess(save_encoders=True):
    """
    Preprocess traffic data for model training
    
    Args:
        save_encoders (bool): Whether to save the label encoders
        
    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    try:
        # Load data
        df = pd.read_csv(TRAFFIC_DATA_PATH)
        print(f"✓ Loaded {len(df)} records from {TRAFFIC_DATA_PATH}")
        
        # Check for missing values
        if df.isnull().any().any():
            print("⚠ Warning: Missing values detected. Dropping rows with missing values.")
            df = df.dropna()
        
        # Encode categorical columns
        le_road = LabelEncoder()
        le_weather = LabelEncoder()
        le_target = LabelEncoder()

        df['road_type'] = le_road.fit_transform(df['road_type'])
        df['weather'] = le_weather.fit_transform(df['weather'])
        df['traffic_level'] = le_target.fit_transform(df['traffic_level'])
        
        print(f"✓ Encoded categorical features")
        print(f"  - Road types: {list(le_road.classes_)}")
        print(f"  - Weather conditions: {list(le_weather.classes_)}")
        print(f"  - Traffic levels: {list(le_target.classes_)}")

        # Save encoders for later use in prediction
        if save_encoders:
            encoders = {
                'road_type': le_road,
                'weather': le_weather,
                'traffic_level': le_target
            }
            with open(ENCODERS_PATH, 'wb') as f:
                pickle.dump(encoders, f)
            print(f"✓ Saved encoders to {ENCODERS_PATH}")

        # Split features and target
        X = df.drop("traffic_level", axis=1)
        y = df["traffic_level"]
        
        # Display feature statistics
        print(f"\n📊 Feature Statistics:")
        print(X.describe())

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
        )
        
        print(f"\n✓ Split data: {len(X_train)} training, {len(X_test)} testing samples")
        
        return X_train, X_test, y_train, y_test
        
    except FileNotFoundError:
        print(f"❌ Error: Data file not found at {TRAFFIC_DATA_PATH}")
        raise
    except Exception as e:
        print(f"❌ Error during preprocessing: {str(e)}")
        raise


def load_encoders():
    """Load saved label encoders"""
    try:
        with open(ENCODERS_PATH, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Encoders file not found at {ENCODERS_PATH}")
        raise

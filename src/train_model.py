"""
Model training module for traffic congestion prediction
"""
from preprocess import preprocess
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score
)
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from pathlib import Path
import numpy as np

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from config import (
    MODEL_PATH, 
    METRICS_PATH, 
    N_ESTIMATORS, 
    MAX_DEPTH, 
    RANDOM_STATE,
    TRAFFIC_LEVELS
)


def plot_confusion_matrix(y_test, y_pred, save_path='confusion_matrix.png'):
    """Plot and save confusion matrix"""
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm, 
        annot=True, 
        fmt='d', 
        cmap='Blues',
        xticklabels=TRAFFIC_LEVELS.values(),
        yticklabels=TRAFFIC_LEVELS.values()
    )
    plt.title('Confusion Matrix - Traffic Prediction')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✓ Confusion matrix saved to {save_path}")
    plt.close()


def plot_feature_importance(model, feature_names, save_path='feature_importance.png'):
    """Plot and save feature importance"""
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    plt.title('Feature Importance')
    plt.bar(range(len(importances)), importances[indices])
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
    plt.ylabel('Importance')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✓ Feature importance plot saved to {save_path}")
    plt.close()


def train_model():
    """Train the traffic prediction model"""
    print("=" * 60)
    print("🚀 Starting Model Training")
    print("=" * 60)
    
    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess()
    
    # Initialize model with class balancing
    print(f"\n🤖 Training Random Forest Classifier...")
    print(f"   - n_estimators: {N_ESTIMATORS}")
    print(f"   - max_depth: {MAX_DEPTH}")
    print(f"   - random_state: {RANDOM_STATE}")
    print(f"   - class_weight: balanced (to handle class imbalance)")
    
    model = RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        max_depth=MAX_DEPTH,
        random_state=RANDOM_STATE,
        class_weight='balanced',  # Handle class imbalance
        n_jobs=-1
    )
    
    # Train model
    model.fit(X_train, y_train)
    print("✓ Model training completed")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 MODEL PERFORMANCE METRICS")
    print("=" * 60)
    print(f"Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print("=" * 60)
    
    # Classification report
    print("\n📋 Detailed Classification Report:")
    print("-" * 60)
    print(classification_report(
        y_test, 
        y_pred, 
        target_names=TRAFFIC_LEVELS.values()
    ))
    
    # Save model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print(f"✓ Model saved to {MODEL_PATH}")
    
    # Save metrics
    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'classification_report': classification_report(
            y_test, 
            y_pred, 
            target_names=TRAFFIC_LEVELS.values(),
            output_dict=True
        )
    }
    with open(METRICS_PATH, 'wb') as f:
        pickle.dump(metrics, f)
    print(f"✓ Metrics saved to {METRICS_PATH}")
    
    # Generate visualizations
    print("\n📈 Generating visualizations...")
    plot_confusion_matrix(y_test, y_pred)
    plot_feature_importance(model, X_train.columns)
    
    print("\n" + "=" * 60)
    print("✅ Training pipeline completed successfully!")
    print("=" * 60)
    
    return model, metrics


if __name__ == "__main__":
    train_model()

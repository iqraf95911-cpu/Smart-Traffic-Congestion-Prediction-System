"""
Convenience script to run the complete pipeline
"""
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=False,
            text=True
        )
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}")
        print(f"Error: {e}")
        return False

def main():
    """Main execution function"""
    print("=" * 60)
    print("🚀 Smart Traffic Congestion Prediction System")
    print("=" * 60)
    
    # Check if model exists
    model_path = Path("model.pkl")
    
    if not model_path.exists():
        print("\n⚠️  Model not found. Training new model...")
        
        # Train model
        if not run_command(
            "python src/train_model.py",
            "Training model"
        ):
            print("\n❌ Failed to train model. Exiting.")
            sys.exit(1)
    else:
        print("\n✓ Model found. Skipping training.")
        print("  (Delete model.pkl to retrain)")
    
    # Run the Flask app
    print("\n" + "=" * 60)
    print("🌐 Starting Flask application...")
    print("=" * 60)
    print("\n📍 Application will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run(
            "python app.py",
            shell=True,
            check=True
        )
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running Flask app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
Setup script for Smart Traffic Congestion Prediction System
"""
import subprocess
import sys
from pathlib import Path

def print_step(step_num, total_steps, message):
    """Print formatted step message"""
    print(f"\n[{step_num}/{total_steps}] {message}")
    print("-" * 60)

def run_command(command, error_message):
    """Run a command and handle errors"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {error_message}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("🚀 Smart Traffic Congestion Prediction System - Setup")
    print("=" * 60)
    
    total_steps = 4
    
    # Step 1: Check Python version
    print_step(1, total_steps, "Checking Python version")
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print("✅ Python version is compatible")
    
    # Step 2: Install dependencies
    print_step(2, total_steps, "Installing dependencies")
    if not run_command(
        "pip install -r requirements.txt",
        "Failed to install dependencies"
    ):
        sys.exit(1)
    print("✅ Dependencies installed successfully")
    
    # Step 3: Generate data
    print_step(3, total_steps, "Generating training data")
    data_file = Path("data/traffic_data.csv")
    
    if data_file.exists():
        print("⚠️  Data file already exists. Skipping generation.")
        print(f"   Delete {data_file} to regenerate")
    else:
        if not run_command(
            "python data/generate_data.py",
            "Failed to generate training data"
        ):
            sys.exit(1)
        print("✅ Training data generated successfully")
    
    # Step 4: Train model
    print_step(4, total_steps, "Training machine learning model")
    model_file = Path("model.pkl")
    
    if model_file.exists():
        print("⚠️  Model file already exists. Skipping training.")
        print(f"   Delete {model_file} to retrain")
    else:
        if not run_command(
            "python src/train_model.py",
            "Failed to train model"
        ):
            sys.exit(1)
        print("✅ Model trained successfully")
    
    # Setup complete
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("=" * 60)
    print("\n📝 Next steps:")
    print("   1. Run the application: python app.py")
    print("   2. Open your browser: http://localhost:5000")
    print("   3. Test the API: python test_api.py")
    print("\n💡 Quick start: python run.py")
    print("=" * 60)

if __name__ == "__main__":
    main()

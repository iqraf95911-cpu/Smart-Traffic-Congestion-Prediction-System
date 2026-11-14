"""
Script to restart Flask application
Kills any existing Flask process on port 5000 and starts a new one
"""
import subprocess
import sys
import time
import os

def find_process_on_port(port=5000):
    """Find process ID running on specified port"""
    try:
        result = subprocess.run(
            f'netstat -ano | findstr :{port}',
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if 'LISTENING' in line:
                    parts = line.split()
                    pid = parts[-1]
                    return pid
        return None
    except Exception as e:
        print(f"Error finding process: {e}")
        return None

def kill_process(pid):
    """Kill process by PID"""
    try:
        subprocess.run(
            f'taskkill /PID {pid} /F',
            shell=True,
            capture_output=True
        )
        return True
    except Exception as e:
        print(f"Error killing process: {e}")
        return False

def main():
    print("=" * 60)
    print("🔄 Flask Application Restart Script")
    print("=" * 60)
    
    # Check if Flask is running
    print("\n1. Checking for existing Flask process...")
    pid = find_process_on_port(5000)
    
    if pid:
        print(f"   Found Flask running on port 5000 (PID: {pid})")
        print("   Stopping Flask...")
        if kill_process(pid):
            print("   ✅ Flask stopped successfully")
            time.sleep(1)
        else:
            print("   ❌ Failed to stop Flask")
            print("   Please stop it manually with Ctrl+C")
            sys.exit(1)
    else:
        print("   No Flask process found on port 5000")
    
    # Start Flask
    print("\n2. Starting Flask application...")
    print("   Running: python app.py")
    print("\n" + "=" * 60)
    print("Flask is starting...")
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
        print("\n\n👋 Flask stopped. Goodbye!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting Flask: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

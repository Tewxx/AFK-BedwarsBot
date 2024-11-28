import subprocess
import time
import os
import sys

def run_bedwars():
    """
    Run the Bedwars.py script and handle any potential errors.
    """
    try:
        # Determine the full path to Bedwars.py
        bedwars_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Bedwars.py')
        
        # Run the script
        print(f"Running Bedwars.py at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        result = subprocess.run([sys.executable, bedwars_path], 
                                capture_output=True, 
                                text=True, 
                                check=True)
        
        # Print output if any
        if result.stdout:
            print("Bedwars.py Output:")
            print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Handle script execution errors
        print(f"Error running Bedwars.py: {e}")
        print("Error output:")
        print(e.stderr)
    except FileNotFoundError:
        print(f"Error: Bedwars.py not found in the current directory.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to continuously run Bedwars.py every 30 minutes.
    """
    print("Bedwars Auto-Rerun Script Started")
    print("Press Ctrl+C to stop the script")
    
    try:
        while True:
            # Run Bedwars.py
            run_bedwars()
            
            # Wait for 30 minutes before next run
            print("Waiting 30 minutes before next run...")
            time.sleep(1300)  # 1800 seconds = 30 minutes
    
    except KeyboardInterrupt:
        print("\nScript stopped by user.")

if __name__ == "__main__":
    main()
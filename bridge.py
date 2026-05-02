import os
import time
import subprocess
from datetime import datetime

WATCH_FILE =" certified_targets.json"
def push_to_web():
    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Change detected. Syncing to HVL-Web...")
        subprocess.run(["git", "add", "-f", WATCH_FILE], check=True)
        subprocess.run(["git", "commit", "-m", "Veritas_Live_Update", "--no-edit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Sync Successful.\n")
    except Exception as e:
        print(f"BRIDGE_ERROR: {e}")

def main():
    print("="*40)
    print("BRIDGE ORCHESTRATOR: ACTIVE (FORCE-SYNC)")
    print(f"Monitoring: {WATCH_FILE}")
    print("Waiting for Veritas V2.2 broadcast...")
    print("="*40)

    last_mtime = os.path.getmtime(WATCH_FILE) if os.path.exists(WATCH_FILE) else 0

    while True:
        if os.path.exists(WATCH_FILE):
            current_mtime = os.path.getmtime(WATCH_FILE)
            if current_mtime > last_mtime:
                push_to_web()
                last_mtime = current_mtime
        time.sleep(5) 

if __name__ == "__main__":
    main()


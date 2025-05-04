import sqlite3
import datetime
import os
import shutil

def quarantine_folder(folder_path, quarantine_path):
    print(f"\n⚠️ Moving {folder_path} to quarantine area {quarantine_path}...")
    if not os.path.exists(quarantine_path):
        os.makedirs(quarantine_path)
    try:
        shutil.move(folder_path, quarantine_path)
        print(f"Folder successfully moved to {quarantine_path}.")
    except Exception as e:
        print(f"Error moving folder: {e}")

def detect_ransomware(db_path="monitor.db", threshold=100, window_sec=10):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        now = datetime.datetime.now()
        window_start = now - datetime.timedelta(seconds=window_sec)

        cursor.execute("""
            SELECT COUNT(*) FROM file_events
            WHERE timestamp >= ?
            AND file_path NOT LIKE '%.db%'
            AND file_path NOT LIKE '%.db-journal%'
        """, (window_start.strftime("%Y-%m-%d %H:%M:%S"),))

        event_count = cursor.fetchone()[0]
        conn.close()

        if event_count > threshold:
            print("\n RANSOMWARE DETECTED ")
            print(f"Triggered at: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Events in {window_sec} seconds: {event_count}")
            
            # 🛡️ Mitigation Step: quarantine the critical folder
            quarantine_folder("/home/nikitha/critical", "/home/nikitha/quarantine")

        else:
            print("\n No ransomware detected.")
            print(f"Events in {window_sec} seconds: {event_count}")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    detect_ransomware()

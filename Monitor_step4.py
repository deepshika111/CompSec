import os
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# SQLite database setup
def init_db():
    conn = sqlite3.connect("monitor.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_events (
        timestamp TEXT,
        event_type TEXT,
        file_path TEXT
    )
    """)
    conn.commit()
    return conn

# Function to log events
def log_event(conn, event_type, file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO file_events (timestamp, event_type, file_path) VALUES (?, ?, ?)", 
                   (timestamp, event_type, file_path))
    conn.commit()
    print(f"[{timestamp}] {event_type}: {file_path}")

# Event handler class
class RansomwareMonitorHandler(FileSystemEventHandler):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def on_created(self, event):
        log_event(self.conn, "Created", event.src_path)

    def on_modified(self, event):
        log_event(self.conn, "Modified", event.src_path)

    def on_deleted(self, event):
        log_event(self.conn, "Deleted", event.src_path)

# Start monitoring function
def start_monitoring(path):
    conn = init_db()
    event_handler = RansomwareMonitorHandler(conn)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"[*] Monitoring started on: {path}")
    try:
        while True:
            pass  # Keeps the script running
    except KeyboardInterrupt:
        observer.stop()
        print("[!] Monitoring stopped.")
    observer.join()
    conn.close()

# Main function
if __name__ == "__main__":
    directory_to_monitor = "/home/nikitha/critical"
    start_monitoring(directory_to_monitor)

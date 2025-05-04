import sqlite3
from datetime import datetime, timedelta

# Connect to the monitor database
conn = sqlite3.connect('monitor.db')
cursor = conn.cursor()

# Load all modification and deletion events
cursor.execute("""
    SELECT timestamp, event_type, file_path FROM file_events
    WHERE event_type IN ('Modified', 'Deleted')
    ORDER BY timestamp ASC
""")

rows = cursor.fetchall()
conn.close()

# Convert timestamps to datetime objects
events = [(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"), etype, fpath) for ts, etype, fpath in rows]

# Detection rule: >5 mod/del events in any 10-second window
window_size = timedelta(seconds=10)
threshold = 5
suspicious_found = False

for i in range(len(events)):
    count = 1
    start_time = events[i][0]

    for j in range(i + 1, len(events)):
        if events[j][0] - start_time <= window_size:
            count += 1
        else:
            break

    if count > threshold:
        print("RANSOMWARE DETECTED!")
        print(f"Triggered at: {events[i][0].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Events in 10 seconds: {count}")
        suspicious_found = True
        break

if not suspicious_found:
    print("No ransomware activity detected.")

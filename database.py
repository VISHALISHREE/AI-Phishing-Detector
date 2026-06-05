import sqlite3

conn = sqlite3.connect("history.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scans(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    prediction TEXT,
    scan_time TEXT
)
""")

conn.commit()

conn.close()

print("Database created successfully!")

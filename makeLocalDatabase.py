import sqlite3
import os


# Check if the database file exists
db_file = 'mydatabase.db'
if not os.path.exists(db_file):
    # If it doesn't exist, create a new database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Create a table
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            data TEXT
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

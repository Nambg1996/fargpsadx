import os

# Path to your SQLite database file
database_path = 'mydatabase.db'

# Define the maximum size in bytes (5 GB)
max_size_bytes = 5 * 1024 * 1024 * 1024

def bytes_to_mb(bytes_value):
    """Convert bytes to megabytes (MB)."""
    return bytes_value / (1024 * 1024)

def check_database_size():
    # Get the size of the database file
    size_bytes = os.path.getsize(database_path)

    # Check if the size exceeds the threshold
    if size_bytes > max_size_bytes:
        print("Error: Database size exceeds 5 GB")
        
        #print(size_bytes)
        print(bytes_to_mb(size_bytes))
    else:
        print("Database size is within the limit")
        print(bytes_to_mb(size_bytes))

if __name__ == "__main__":
    check_database_size()

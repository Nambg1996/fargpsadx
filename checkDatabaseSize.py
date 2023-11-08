import os

# Path to your SQLite database file
database_path = 'mydatabase.db'

# Define the maximum size in bytes (5 GB)
max_size_bytes = 5 * 1024 * 1024 * 1024

def bytes_to_mb(bytes_value):
    """Convert bytes to megabytes (MB)."""
    return float(bytes_value / (1024 * 1024))

def toGb():
    # Get the size of the database file
    size_bytes = os.path.getsize(database_path)
    gbSize=bytes_to_mb(size_bytes)/1024

    # Check if the size exceeds the threshold byte to mb-gb
    return float(gbSize)
       

   
        



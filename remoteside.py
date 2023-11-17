import psycopg2
import socket


def conectToDatabaseAndMakeTable(tableName):
    # Establish a connection to the database
    remote_conn = psycopg2.connect(
        host='192.168.161.127',
        port=5432,
        dbname='fadb',
        user='tyk_user',
        password='1998'
    )

    # Create a cursor
    cursor = remote_conn.cursor()
    # Check if the table already exists
    table_exists_sql = f"""
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name ='{tableName}'
    );
    """
    
   

    cursor.execute(table_exists_sql)
    table_exists = cursor.fetchone()[0]
    
   

    if not table_exists:
        # Define the SQL statement to create the table
        create_table_sql = f"""
        CREATE TABLE gpsadx.{tableName} (
            time_update timestamp,
            data json
        );
        """
       

        # Execute the SQL statement to create the table
        cursor.execute(create_table_sql)

        # Commit the changes to the database
        remote_conn.commit()
        
    # alertmess.Success("Table on the remote database is created successfully")
        print("Table on the remote database is created successfully")
    else:
        print("Table on remote Database already exists, no action taken.")
 
    # Close the cursor and the database connection
    cursor.close()
    remote_conn.close()
    
def get_local_ip_address():
    try:
        # Use a dummy socket to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))  # Connect to a known external server
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None


   
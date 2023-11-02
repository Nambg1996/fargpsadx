
import subprocess
import sqlite3
import psycopg2
import time
import requests
#import alertmess

import networks


def conectToDatabaseAndMakeTable():
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
    table_exists_sql = """
    SELECT EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = 'gpsadxnewdata'
    );
    """

    cursor.execute(table_exists_sql)
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        # Define the SQL statement to create the table
        create_table_sql = """
        CREATE TABLE gpsadx.gpsadxnewdata (
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
    

""" while networks.is_wifi_available():
    #print("wifi is ok")
    conectToDatabaseAndMakeTable()
else:
    print("Waiting for Wi-Fi to be available...")
    networks.connect_to_wifi()
    time.sleep(3)  # Adjust the sleep duration as needed    """   
    
    
while not networks.is_wifi_available():
    print("Waiting for Wi-Fi to be available...")
    networks.connect_to_wifi()
    time.sleep(3)  # Adjust the sleep duration as needed

# Wi-Fi is available, so connect to the database and make the table
conectToDatabaseAndMakeTable()    

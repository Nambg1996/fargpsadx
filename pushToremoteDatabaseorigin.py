import subprocess
import sqlite3
import psycopg2
import time
import requests
import networks

""" every update data to remote Database. it will automaticlly delete record by time """


def insert_and_delete_records():
    
    # Connect to the local SQLite database
    local_conn = sqlite3.connect('mydatabase.db')
    local_cursor = local_conn.cursor()

    # Connect to the remote PostgreSQL database
    #print("the records is inserting to database")
    try:
        remote_conn = psycopg2.connect(
        host='192.168.161.127',
        port='5432',
        dbname='fadb',
        user='tyk_user',
        password='1998'
        )
        remote_cursor = remote_conn.cursor()
        # Execute the query to retrieve the oldest 100 records from the local database
        select_query = "SELECT * FROM sensor_data ORDER BY timestamp ASC LIMIT 100"
        local_cursor.execute(select_query)
        # Fetch the oldest 100 records
        records = local_cursor.fetchall()

        # Process each record
        for record in records:
            # Extract the relevant data from the record
            time_update = record[1]
            datasensor = record[2]
            # Prepare the insert query for the remote database
            insert_query = "INSERT INTO gpsadx.gpsadxnewdata (time_update, data) VALUES (%s, %s::json)"
            insert_values = (time_update, datasensor)
            # Execute the insert query on the remote database
            remote_cursor.execute(insert_query, insert_values)

            # Delete the record from the local database using a placeholder
            delete_query = "DELETE FROM sensor_data WHERE timestamp = ?"
            local_cursor.execute(delete_query, (time_update,))
            time.sleep(0.008)

        # Commit the changes to the remote database
        remote_conn.commit()
        # Commit the changes to the local database
        local_conn.commit()

    except Exception as e:
        # Handle the exception (e.g., log an error, rollback transactions, etc.)
        #print(f"Error: {e}")
        try:
            remote_conn.rollback()
            local_conn.rollback()
        except Exception as e:
            current_time=time.time()
            formatted_time= time.ctime(current_time)
            #print(f"{formatted_time} Error is catching: {e}")



# Continuously check Wi-Fi availability and execute the function when Wi-Fi is available
while True:
    if networks.is_wifi_available():
        #print("wifi is ok")
        insert_and_delete_records()

    else:
        #print("Waiting for Wi-Fi to be available...")
        #networks.connect_to_wifi()
        time.sleep(5)  # Adjust the sleep duration as needed  
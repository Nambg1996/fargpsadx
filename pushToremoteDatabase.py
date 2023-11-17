import subprocess
import sqlite3
import psycopg2
import time
import requests
import networks






def deleteRecord():
    pass
    

            
""" every update data to remote Database. it will automaticlly delete record by time """
 

def insert_and_delete_records():
    
    # Connect to the local SQLite database
    local_conn = sqlite3.connect('mydatabase.db')
    local_cursor = local_conn.cursor()
    
    

    try:
        
        # Connect to the remote PostgreSQL database

        print("s1")
        
        # Execute the query to retrieve the oldest 100 records from the local database
        select_query = "SELECT * FROM sensor_data ORDER BY timestamp ASC LIMIT 100"
        local_cursor.execute(select_query)
        # Fetch the oldest 100 records
        records = local_cursor.fetchall()
        print("s2")

        # Process each record
        for record in records:
            # Extract the relevant data from the record
            time_update = record[1]
            datasensor = record[2]
            print("s3")

            # Prepare the insert query for the remote database
            insert_query = "INSERT INTO gpsadx.gpsadxnewdata (time_update, data) VALUES (%s, %s::json)"
            insert_values = (time_update, datasensor)
            checkDatabase=1
            while checkDatabase:
                try:
                 print("s4")
                 remote_conn = psycopg2.connect(
                 host='192.168.161.127',
                 port='5432',
                 dbname='fadb',
                 user='tyk_user',
                 password='1998'
                 )
                 remote_cursor = remote_conn.cursor()
                 remote_cursor.execute(insert_query, insert_values)
                 checkDatabase=0
                 
                 print("s5")
                 
                 #time.sleep(0.15)
                 print("insert ok to remoteDatabase")
                except Exception as e:
                    # Handle the exception (e.g., log an error, rollback transactions, etc.)
                    error_message = f"Error during insert to Remote database: {e}"
                    print(error_message)
                    script_name = "./restart_remotes.sh"
                    # Run the shell script with sudo
                    print("restart this script")
                    #subprocess.run(["sudo", script_name], check=True) 

            # Execute the insert query on the remote database
            checkDele=1
            while checkDele:
                try:
                    
                    # Delete the record from the local database using a placeholder
                    delete_query = "DELETE FROM sensor_data WHERE timestamp = ?"
                    local_cursor.execute(delete_query, (time_update,))
                    checkDele=0
                    print("delete ok")
                    
                except Exception as e:
                    # Handle the exception (e.g., log an error, rollback transactions, etc.)
                    
                   
                    error_message = f"Error during delete local database: {e}"
                    print(error_message)
                    time.sleep(0.005)
                    checkDele=1
                

                
                # Log the error to a file (append to an error log file)
                
                #with open('error_log.txt', 'a') as error_log_file:
                 #error_log_file.write(error_message + '\n')
                 # Replace "restart_remote.sh" with the actual script name and path

                

        # Commit the changes to the remote database
        
        remote_conn.commit()
        
        # Commit the changes to the local database
        local_conn.commit()
    
    except Exception as e:
        # Handle the exception (e.g., log an error, rollback transactions, etc.)
        print(f"Error: {e}")
        remote_conn.rollback()
        local_conn.rollback()

    finally:
        # Close the cursors and database connections
        print("vao day")
        local_cursor.close()
        local_conn.close()
        remote_cursor.close()
        remote_conn.close()
        

# Continuously check Wi-Fi availability and execute the function when Wi-Fi is available
while True:
    if networks.is_wifi_available():
        print("wifi is ok")
        insert_and_delete_records()
        
    else:
        print("Waiting for Wi-Fi to be available...")
        #networks.connect_to_wifi()
        time.sleep(3)  # Adjust the sleep duration as needed  
      
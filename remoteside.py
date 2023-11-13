import psycopg2



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
   
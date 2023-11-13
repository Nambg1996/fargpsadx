#!/bin/bash

# Change to the directory where your Python scripts are located
cd /home/pi/nam_test/fargpsadx
# Run makeLocalDatabase.py
/usr/bin/python3 makeLocalDatabase.py&

# Run getdataUartToLocalDatabase.py
/usr/bin/python3 getdataUartToLocalDatabase.py&

# Run createListTableOnRemoteServer.py make ip tracking Raspberry table and table data 
/usr/bin/python3 createListTableOnRemoteServer.py& 


# Run pushToremoteDatabase.py
/usr/bin/python3 pushToremoteDatabase.py&


import subprocess
import sqlite3
import psycopg2
import time
import requests
import networks
import threading
import remoteside


""" make table on remote server. 
the first table --> tracking ip address for Raspberry Pi, 
the second table --> table store data 
"""

tableIpAdress="trackingraspid"
tableData="gpsadxnewdata"

def wifi_check_thread(createtableDatabase):
    while not networks.is_wifi_available():
        print("Waiting for Wi-Fi to be available...")
        networks.connect_to_wifi()
        time.sleep(3)
    createtableDatabase
        

# Create a thread to run the Wi-Fi check
wifi_thread = threading.Thread(target=wifi_check_thread(remoteside.conectToDatabaseAndMakeTable(tableIpAdress)))
# Start the thread
wifi_thread.start()

# Create a thread to run the Wi-Fi check
wifi_thread = threading.Thread(target=wifi_check_thread(remoteside.conectToDatabaseAndMakeTable(tableData)))
# Start the thread
wifi_thread.start()




   

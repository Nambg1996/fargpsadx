import serial
import json
import datetime
import sqlite3
import os
import math
import time

import checkDatabaseSize

#import alertmess




""" this code program is get data via Uart and then put data to mydatabase.db """

ser = serial.Serial('/dev/ttyS0', 9600,timeout=0.5) 
def InsertDataToLocalDatabase(data):
        split_data = data.split('--')
       
        if len(split_data) == 2:
                lat = split_data[0].split(":")[0]
                lon = split_data[0].split(":")[1]
                adxData = split_data[1]
                axayazDatas = json.loads(adxData)["data"]

                for axayazData in axayazDatas:
                      if axayazData is not None:  
                                adx=axayazData.split(":")
                                ax=float(adx[0])
                                ay=float(adx[1])
                                az=float(adx[2])
                                asum=math.sqrt(ax*ax+ay*ay+az*az)
                                current_time = datetime.datetime.now()
                                data = {"ax": ax,"ay": ay,"az": az,"asum": asum,"lat": lat,"lon": lon}
                                datajson = json.dumps(data)
                                conn = sqlite3.connect('mydatabase.db')
                                c = conn.cursor()
                                # Insert data into the table
                                c.execute('INSERT INTO sensor_data (timestamp, data) VALUES (?, ?)', (current_time, datajson))
                                # Commit changes and close connection
                                conn.commit()
                                conn.close()
                                time.sleep(0.008)  
 
   


def getdata():
        try:
                data = ser.readline().decode('utf-8').strip()
                if data:
                        #print("Data received:")
                   InsertDataToLocalDatabase(data)
                   print("data >>>> LocalDatabase")   
   
                else:
                  print(" Connect with ATOM LITE ESP32 Via UART have a proplem")
                  
 
        except serial.SerialException as e:
         print(f"Serial error: {e}")
        except UnicodeDecodeError as e:
         print(f"Data decoding error: {e}")
        except Exception as e:
         print(f"An unexpected error occurred: {e}")
        

while True:
        if checkDatabaseSize.toGb()<5:
          getdata()
        else:
          pass        
  
        

 

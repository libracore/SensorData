#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Application to write Raspberry PI sensor value to ERP
#
# Created by Lars, 2016-04-25
# 

# imports
from frappeclient import FrappeClient
from sense_hat import SenseHat
from time import gmtime, strftime

# variable definition
server = "http://hseerp01.intra.hse-ag.com"
user = "sensor@hseag.com"
password = "sensor"
sensor_name = "Server room"
temperature_unit = "°C"
humidity_unit = "%rH"

# sync function
def sync():
   # read temperature
   print("Reading sensor data...")
   sense = SenseHat()
   sense.clear()
   temperature = sense.get_temperature()
   temperature = round(temperature , 1)
   # temperature offset correction
   temperature = temperature - 5
   print("{} {}".format(temperature, temperature_unit))
   # read humidity
   humidity = sense.get_humidity()
   humidity = round(humidity, 1)
   if humidity > 100:
      humidity = 100.0
   print("{} {}".format(humidity, humidity_unit))
   # write data to ERP
   print("Logging into ERP {}...".format(server))
   client = FrappeClient(server, user, password)  
   print("Creating sensor data...")
   doc = {"doctype":"Sensor data"}
   doc["date"] = strftime("%Y-%m-%d") 
   doc["time"] = strftime("%H:%M")
   doc["sensor_name"] = sensor_name
   doc["value"] = temperature
   doc["unit"] = temperature_unit
   client.insert(doc)
   print("Inserted " + doc["sensor_name"])

# constructor
if __name__=="__main__":
	sync()

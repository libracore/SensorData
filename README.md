# SensorData
Monitor application for ERPNext to include Raspberry PI Sense Hat for sensor data and room surveillance

== Description ==
The Monitor app is an app for ERPNext. It contains the DocType "Sensor data", which allows storing sensor readings.

The SensorData script runs on a Raspberry PI with Sense Hat. When set up with a cron job, it reports the sensor data to ERPNext.

== Requirements ==
* ERPNext server
* Raspberry PI with Sense Hat

== Installation ==
* Install Monitor app in your ERPNext
* Create a new user "sensor" and a new role sensor (that can create new sensor data items)
* Copy the server scripts to the Raspberry PI
* Adjust the script file to match your server and sensor account
* Test if the script works
* Create cron job to execute the readout

# sensor_data_iot
Example of different ways to collect data from sensor and analyse that data

## Scenario 1
In this scenerio we will use an SQLite based web application (on glitch) to store and display the data and then use a python script to send data to this database

Remix the following glitch project:
https://glitch.com/edit/#!/sensor-data-example

Then modify the following python script to send data to this sql based webapp:
https://github.com/oidebrett/sensor_data_iot/blob/main/pythonToHttpPost.py

## Scenario 2
In the second scenerio we will use an online cloud service called ThingSpeak to store and display the data and then use a python script to send data to this database

Sign up to Thingspeak
https://thingspeak.com/

Then modify the following python script to send data to this online cloud service:
https://github.com/oidebrett/sensor_data_iot/blob/main/pythonToThingSpeakChannel.py



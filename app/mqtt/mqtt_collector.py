import paho.mqtt.client as mqtt
import json
import time
import xml.etree.ElementTree as et

from threading import Thread

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(0,"..")

from database import Database
from db_manager import dbManager
from coap.remote_controller import coapActuatorHandler

def change_cons_sensing_freq(wagon,freq):
    client = mqtt.Client()
    client.connect("fd00::1", 1883, 60)
    msg = "<frequency> " + str(freq) + " </frequency>"
    client.publish(wagon+"/consumption/frequency",msg)


def on_connect_consumption(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("consumption")

def on_message_consumption(client, userdata, msg):
    db = dbManager()
    print(msg.topic + " " + str(msg.payload) + str(userdata))
    myxml = et.fromstring(msg.payload)
    node = myxml[0].text
    wagon = myxml[1].text
    cons = int(myxml[2].text)
    timestamp = int(myxml[3].text)

    #this could be optimized caching the values in some structure like a list or a dictionary
    result = db.get_actuator_ip(wagon,"energy")
    thresholds = db.get_wagon_thresholds(wagon)
    coap_handler = coapActuatorHandler("energy")
    if (cons > thresholds["max_consumption"] and result["state"] != "backup"):
        command = "open"
        new_state="backup"
    elif(cons < thresholds["max_consumption"] and result["state"] != "standard"):
        command = "shutdown"
        new_state = "standard"
    else:
        return  
    # Send command to actuator
    cmdstring = "<?xml version='1.0' encoding='UTF-8'?><cmd> " + command + " </cmd>" 
    response = coap_handler.cooling_actuator_send(result["ip_address"],cmdstring)
    db.set_actuator_state(result["ip_address"],new_state)
    db.store_sensor_data(node,"consumption",cons,timestamp)


# The callback for when the client receives a CONNACK response from the server.
def on_connect_temp(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("brake_temp")

# The callback for when a PUBLISH message is received from the server.
def on_message_temp(client, userdata, msg):
    db = dbManager()
    print(msg.topic + " " + str(msg.payload) + str(userdata))
    myxml = et.fromstring(msg.payload)
    node = myxml[0].text
    wagon = myxml[1].text
    temp = int(myxml[2].text)
    timestamp = int(myxml[3].text)
    #Store in database
    #Retrieve Actuator address and current state

    #this could be optimized caching the values in some structure like a list or a dictionary
    result = db.get_actuator_ip(wagon,"brakes")
    thresholds = db.get_wagon_thresholds(wagon)
    print("mqttOnMessage - ip address of actuator is:" + str(result))
    coap_handler = coapActuatorHandler("cooling")
    if (temp > thresholds["max_br_temp"] and result["state"] != "cooling"):
        command = "activate"
        new_state="cooling"
    elif(temp < thresholds["max_br_temp"] and result["state"] != "idle"):
        command = "deactivate"
        new_state = "idle"
    else:
        # Do nothing 
        return 
    
    # Send command to actuator    
    cmdstring = "<?xml version='1.0' encoding='UTF-8' ?><cmd> "+command+" </cmd>"
    response = coap_handler.cooling_actuator_send(result["ip_address"],cmdstring)
    db.set_actuator_state(result["ip_address"],new_state)
    db.store_sensor_data(node,"brake_temperature",temp,timestamp)

def mqtt_client_co():
    client_co = mqtt.Client()
    client_co.on_connect = on_connect_consumption
    client_co.on_message = on_message_consumption
    client_co.connect("fd00::1", 1883, 60)
    client_co.loop_forever()

def mqtt_client_temp():
    client_temp = mqtt.Client()
    client_temp.on_connect = on_connect_temp
    client_temp.on_message = on_message_temp
    client_temp.connect("fd00::1", 1883, 60)
    client_temp.loop_forever()

if __name__ == "__main__":
    
    #Run threads
    thread_temp = Thread(target = mqtt_client_temp)
    thread_temp.start()
    thread_co = Thread(target = mqtt_client_co)
    thread_co.start()



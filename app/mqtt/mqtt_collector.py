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


def on_connect_consumption(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("consumption")

def on_message_consumption(client, userdata, msg):
    db = dbManager()
    print(msg.topic + " " + str(msg.payload) + str(userdata))
    
    myxml = et.fromstring(msg.pyaload)
    node = myxml[0].text
    wagon = myxml[1].text
    cons = myxml[2].text
    
    result = db.get_actuator_ip(node)
    thresholds = db.get_wagon_thresholds(wagon)

    print("mqttOnMessage - ip address of actuator is:" + str(result))

    coap_handler = coapActuatorHandler()
    if (cons > thresholds["max_consumption"] and result["state"] != "backup"):
        command = "on"
        new_state="backup"
    elif(cons < thresholds["max_consumption"] and result["state"] != "standard"):
        command = "off"
        new_state = "standard"
    else:
        return  

    # Send command to actuator    
    response = coap_handler.cooling_actuator_send(result["ip_address"],command,"o")
    db.set_actuator_state(result["ip_address"],new_state)


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
    
    myxml = et.fromstring(msg.pyaload)
    
    node = myxml[0].text
    wagon = myxml[1].text
    temp = myxml[2].text
    
    #Store in database
    db.store_sensor_data(node,"brake_temperature",temp,time.time())
    
    #Retrieve Actuator address and current state
    result = db.get_actuator_ip(node)
    thresholds = db.get_wagon_thresholds(node)
    
    print("mqttOnMessage - ip address of actuator is:" + str(result))

    coap_handler = coapActuatorHandler()
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
    response = coap_handler.cooling_actuator_send(result["ip_address"],command,"o")
    db.set_actuator_state(result["ip_address"],new_state)

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
        



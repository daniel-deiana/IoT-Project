import paho.mqtt.client as mqtt
import json
import time
from threading import Thread

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(0,"..")

from database import Database
from db_manager import dbManager
from coap.remote_controller import coapActuatorHandler

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
    
    #Handle sensor data
    data = json.loads(msg.payload)
    
    #Store in database
    db.store_sensor_data(data["node_id"],"brake_temperature",data["temperature"],time.time())
    
    #Retrieve Actuator address and current state
    result = db.get_actuator_ip(data["node_id"])
    
    print("mqttOnMessage - ip address of actuator is:" + str(result))

    coap_handler = coapActuatorHandler();
    if (data["temperature"] > 50 and result["state"] == "cooling"):
        response = coap_handler.cooling_actuator_send(result["ip_address"],"activate","o")
        #Update the actuator state
        state="cooling"
        db.set_actuator_state(result["ip_address"],state)


def mqtt_client_temp():
    client_temp = mqtt.Client()
    client_temp.on_connect = on_connect_temp
    client_temp.on_message = on_message_temp
    client_temp.connect("fd00::1", 1883, 60)
    client_temp.loop_forever()

if __name__ == "__main__":
    
    #Run threads
    thread_temp = Thread(target=mqtt_client_temp)
    thread_temp.start()
    


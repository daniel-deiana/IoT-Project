import paho.mqtt.client as mqtt
import json
import time

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(0,"..")

from database import Database
from coap.remote_controller import coapActuatorHandler

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("brake_temp")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    
    print(msg.topic + " " + str(msg.payload) + str(userdata))
    
    #Handle sensor data
    data = json.loads(msg.payload)
    
    #Store in database
    db = Database()
    db.connect_db()
    
    querystring = " INSERT INTO sensor_data(`sensor_id`, `type`, `value`, `timestamp`,`wagon`) VALUES (%s,%s,%s,%s,%s);"
    parameters = (data["node_id"], "brake_temperature", data["temperature"], int(time.time()), 1)
    db.execute_query(querystring,parameters)
   
    #Retrieve Actuator address and current state
    db = Database()
    db.connect_db()
    querystring = " SELECT A.ip_address, A.state  FROM actuator A inner join wagon W on W.wagon_id = A.wagon INNER JOIN sensor_data D on D.wagon = W.wagon_id WHERE D.sensor_id = %s;"
    result = db.execute_query(querystring,(data["node_id"]))
    print("mqttOnMessage - ip address of actuator is:" + str(result)) 
    
    coap_handler = coapActuatorHandler();
    if (data["temperature"] > 50 and result["state"] != "cooling"):
        response = coap_handler.cooling_actuator_send(result["ip_address"],"o","o")
        #Update the actuator state
         

def mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("fd00::1", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

if __name__ == "__main__":
    mqtt_client()

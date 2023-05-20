import paho.mqtt.client as mqtt

# import sys module
import sys
# tell interpreter where to look
sys.path.insert(0,"..")

from database import Database

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
    




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("fd00::1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()



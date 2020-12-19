import paho.mqtt.client as mqtt
import os
import multiprocessing as mp
import logging

## possibilité de lancer un brooker shell par python
#os.system("mosquitto -v")

def on_connect(client, userdata, flags, rc, properties=None):
        print("Connection au brooker\n")
        print(client)
        print(userdata)
        print(flags)
        print(rc)
        client.subscribe("Test/+")
        
def on_message(client, userdata, message):
        print(client)
        print(userdata)
        print(message)
        print(message.topic+""+str(message.payload))

def on_disconnect(client, userdata,rc=0):
    logging.debug("DisConnected result code "+str(rc))
    client.loop_stop()
# creation d'un client et parametrage d'un client

client = mqtt.Client()                          
client._client_id = "11"
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
   
client.connect(host="127.0.0.1", port=1883, keepalive=60, bind_address='', bind_port=0,  properties=None,)
#client.loop_start()               cree un thread pour la comm
#client.loop_stop() 
client.loop_forever()

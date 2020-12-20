import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import logging
import random
## possibilité de lancer un brooker shell par python
#os.system("mosquitto -v")
INFLUXDB_ADDRESS = "127.0.0.1"
INFLUXDB_USER = "Enagnon"
INFLUXDB_MDP = "mmsldonrm"
INFLUXDB_DATABASE = "Feux"

MQTT_ADDRESS = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "Test/+"
MQTT_ID = "MqttToInfl"


def on_connect(client, userdata, flags, rc, properties=None):
        print("Connection au brooker\n")
        client.subscribe(MQTT_TOPIC)
        
def on_message(client, userdata, message):
        print(message.topic+""+str(message.payload))

def on_disconnect(client, userdata,rc=0):
    logging.debug("DisConnected result code "+str(rc))
    client.loop_stop()


if __name__=="__main__":
        # creation client mqtt et parametrage 
        client_mqtt = mqtt.Client()                          
        client_mqtt._client_id = MQTT_ID
        client_mqtt.on_connect = on_connect
        client_mqtt.on_message = on_message
        client_mqtt.on_disconnect = on_disconnect

        # instanciation connection avec InfluxDB
        in
        
        client_mqtt.connect(host=MQTT_ADDRESS, port=MQTT_PORT, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        #client_mqtt.connect_srv(......)
        #client_mqtt.loop_start()               cree un thread pour la comm
        #client_mqtt.loop_stop() 
        client_mqtt.loop_forever()

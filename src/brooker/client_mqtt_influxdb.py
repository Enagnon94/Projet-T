import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient,Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import logging
import json
## possibilité de lancer un brooker shell par python
#os.system("mosquitto -v")
INFLUXDB_ADDRESS = "127.0.0.1:8086"
INFLUXDB_USER = "Enagnon"
INFLUXDB_MDP = "mmsldonrm"
INFLUXDB_DATABASE = "Feux"

MQTT_ADDRESS = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "Test/+"
MQTT_ID = "MqttToInfl"

TOKEN = "Y_3M2ARgt4jeADhSE8pzWnKhGDksp8005FCMkJKCh6SxiRvs5Z28vtMuUIyW7nG6PwOx4c-bnjP-QZJtQab2TQ=="
ORG = "ProjetT"
BUCKET = "Feux"


def on_connect(client, userdata, flags, rc, properties=None):
        print("Connection au brooker\n")
        client.subscribe(MQTT_TOPIC)        
        
def on_message(client, userdata, message):
        data = "test"
        data = data.encode('utf-8')
        print(message.topic+""+str(message.payload))
        client_influxDB = InfluxDBClient(url=INFLUXDB_ADDRESS,token=TOKEN)
        write_api = client_influxDB.write_api(write_options=SYNCHRONOUS)
        data = InfluxDBClient
        #influxdb_client.Point("Capteur").tag("ID","c1").field("temperature",25)
        write_api.write(bucket=BUCKET, org=ORG, record=data)

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
        
        # client_influxDB.switch_database(INFLUXDB_DATABASE)
      
        client_mqtt.connect(host=MQTT_ADDRESS, port=MQTT_PORT, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        #client_mqtt.connect_srv(......)
        #client_mqtt.loop_start()               cree un thread pour la comm
        #client_mqtt.loop_stop() 
        client_mqtt.loop_forever()

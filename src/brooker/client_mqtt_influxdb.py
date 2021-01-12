import paho.mqtt.client as mqtt
from influxdb_client import Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
import influxdb_client
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
        print("Client InfluxDB connecté au brooker\n")
        client.subscribe(MQTT_TOPIC)        
        
def on_message(client, userdata, message):
        
        client_influxDB = influxdb_client.InfluxDBClient(url=INFLUXDB_ADDRESS,token=TOKEN, org=ORG)
        write_api = client_influxDB.write_api(write_options=SYNCHRONOUS)
        
        donnee = ExtractionBDD(str(message.payload,'utf-8'))
        print(message.topic+""+str(message.payload))
        
        for i in range (6):
                requete = "temperature,X="+str(donnee[3*i])+",Y="+str(donnee[3*i+1])+" value="+str(donnee[3*i+2])
                print(requete)
                write_api.write(bucket=BUCKET, org=ORG,record=[requete])
               
                # write_api.write(bucket=BUCKET, org=ORG,record=["Capteur,Id=11 20"])
        # write_api.write(bucket=BUCKET, org=ORG, record=Point("Capteur").tag("Id","1").field("Temp",25).field("Lum",20).time(1))
        # write_api.write(bucket=BUCKET, org=ORG,record=[{"measurement": "Capteur", "tags": {"location": "C1"}, "fields": {"Temp": 25, "lum":30}, "time": 1}])

def ExtractionBDD(data):
        donnee =[]
        for i in range(len(data)):          # mise sous forme de liste
                if data[i].isdigit():
                        donnee.append(data[i])
        if len(donnee) == 24:            # cas où X = 10, retraitement du string
                donnee.pop(0)
                donnee.pop(3)
                donnee.pop(6)
                donnee.pop(9)                 
                donnee.pop(12)
                donnee.pop(15) 
                donnee[0] = 10
                donnee[3] = 10
                donnee[6] = 10
                donnee[9] = 10
                donnee[12] = 10
                donnee[15] = 10   
        return donnee


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

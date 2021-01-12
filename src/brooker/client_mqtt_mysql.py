import paho.mqtt.client as mqtt
import mysql.connector
import logging

import json
## possibilité de lancer un brooker shell par python
#os.system("mosquitto -v")

MQTT_ADDRESS = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "Test/+"
MQTT_ID = "MqttToMySql"



def on_connect(client, userdata, flags, rc, properties=None):
        print("Client MySql connecté au brooker\n")
        client.subscribe(MQTT_TOPIC)        

def on_disconnect(client, userdata,rc=0):
        logging.debug("DisConnected result code "+str(rc))
        client.loop_stop()
     
def on_message(client, userdata, message):
        # print("message")
        # if message:
             #   print(str(message.payload,'utf-8'))
                EnregistrementBdd(str(message.payload,'utf-8'))
    
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
                       
    
def EnregistrementBdd(data):
        donnee = ExtractionBDD(data)
        if (len(donnee) == 18 ):
                for i in range(6):       
                        sqlInsert = "Update Feux set Intensité="+str(donnee[3*i+2])+" where X="+str(donnee[3*i])+" and Y="+str(donnee[3*i+1])+";" 
                        mycursor.execute(sqlInsert)
                        print(sqlInsert)
                mycursor.execute("COMMIT;")    
                print("\n")

if __name__=="__main__":
        # creation client mqtt et parametrage 
        client_mqtt = mqtt.Client()                          
        client_mqtt._client_id = MQTT_ID
        client_mqtt.on_connect = on_connect
        client_mqtt.on_message = on_message
        client_mqtt.on_disconnect = on_disconnect

        mydb = mysql.connector.connect(host="localhost", user="Enagnon", passwd="bdd", database="ProjetTEmergency",)
        print("Connected to BDD")
        mycursor = mydb.cursor()

        # instanciation connection avec InfluxDB     
        client_mqtt.connect(host=MQTT_ADDRESS, port=MQTT_PORT, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        client_mqtt.loop_forever()
        #client_mqtt.connect_srv(......)
        #client_mqtt.loop_start()               cree un thread pour la comm
        #client_mqtt.loop_stop() 
       

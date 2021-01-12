## Emergency Web Server##
## En écoute, s'il recoit un message par UART du dataCollector, il le traite et le publie en MQTT ##

import paho.mqtt.client as mqtt
import serial
import mysql.connector
from time import sleep
import re


def initUART():
                   # ser = serial.Serial(SERIALPORT, BAUDRATE)
    ser.port = SERIALPORT
    ser.baudrate = BAUDRATE
    ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
    ser.parity = serial.PARITY_NONE  # set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
    ser.timeout = None  # block read

    # ser.timeout = 0             #non-block read
    # ser.timeout = 2              #timeout block read
    ser.xonxoff = False  # disable software flow control
    ser.rtscts = False  # disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
    # ser.writeTimeout = 0     #timeout for write
    print("Starting Up Serial Monitor")
    try:
        ser.open()
    except serial.SerialException:
        print("Serial {} port not available".format(SERIALPORT))
        exit()

def ecouteUART():
    data=ser.readline()
    return str(data,'UTF-8')

def remplirBDD():
    nb=1
    for m in range(10):
        for i in range(6):
            r = 0 # random.randint(0,9)
            sqlReq="INSERT INTO Feux (IdCapteur, X, Y, Intensité) VALUES("+str(nb)+","+str(m+1)+", "+str(i+1)+", "+str(r)+");"
            print(sqlReq)
            nb+=1
            mycursor.execute(sqlReq)      
    mycursor.execute("COMMIT;")              
    

def EnregistrementBdd(data):
    print(len(data))
    if (len(data) == 18 ):
        for i in range(6):       
            sqlInsert = "Update Feux set Intensité="+str(data[3*i+2])+" where X="+str(data[3*i])+" and Y="+str(data[3*i+1])+";"
            print(sqlInsert)
            mycursor.execute(sqlInsert)
        mycursor.execute("COMMIT;")    
    
def TraitementDonnee(data):
    liste.clear()
    for a in data:              
        if a.isdigit():
            liste.append(a)         # cree un string avec les donnees     
        
    if len(liste) == 24:            # cas où X = 10, retraitement du string
        liste.pop(0)
        liste.pop(3)
        liste.pop(6)
        liste.pop(9)                 
        liste.pop(12)
        liste.pop(15) 
        liste[0] = 10
        liste[3] = 10
        liste[6] = 10
        liste[9] = 10
        liste[12] = 10
        liste[15] = 10   
    return liste

if __name__ == '__main__':
        SERIALPORT = "/dev/ttyACM0"                             # port pour comm. UART
        BAUDRATE = 115200
        ser = serial.Serial()
        initUART()
        liste = []

        mydb = mysql.connector.connect(host="localhost", user="Enagnon", passwd="bdd", database="ProjetTEmergency",)
        print("Connected to BDD")
        mycursor = mydb.cursor()
    #    remplirBDD()

        client = mqtt.Client()
        client._client_id = "EmerWebServ"

        client.connect(host="127.0.0.1", port=1883, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        client.loop_start() 

        while True:                         
            data = ecouteUART()   # ecoute UART
        
            if data:     
                donnee = TraitementDonnee(data)  # traitement des donnees recues, mise au format            
                if len(donnee) == 18:            # enregistrement en bdd si string de bonne longueur
               #     EnregistrementBdd(donnee)
                    mm = client.publish(topic="Test/Capteur", payload="".join(str(donnee)), qos=1,retain=False)
   
                print(liste)
                
             
                    

        # client = mqtt.Client()
        # client._client_id = "EmerWebServ"

        # client.connect(host="127.0.0.1", port=1883, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        # #client.loop_start()              # cree un thread pour la comm

        # mm = client.publish(topic="Test/Capteur", payload="Kwabo, ceci est un test", qos=1,retain=False)

        # print(str(mm.is_published()))

        #client.loop_stop() 
        #client.loop_forever()


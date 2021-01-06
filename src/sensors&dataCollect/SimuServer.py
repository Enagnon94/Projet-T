# coding: utf-8
import serial
import time
import mysql.connector
import sys
from time import sleep


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


def sendUARTMessage(msg):
    if isinstance(msg,str):
        message_bytes = bytes(msg, 'utf-8')
        ser.write(message_bytes)
        print("Message <" + msg + "> sent to micro-controller.")
    else:    
        ser.write(msg)
        print("Message <" + (msg, 'utf-8') + "> sent to micro-controller.")


def EnregistrementBdd(nom,id_,temp,lum,ordre):    # Enregistrement et suppression donnees en bdd
    sqlInsertInto = "INSERT INTO Data VALUES (%s, %s, %s, %s, %s);"         # requete permettant d'enregistre une donnee
    sqlCountRows = "SELECT COUNT(*) FROM Data"                              # requete pour compter le nombre de ligne dans la table
    sqlDelete = "DELETE FROM Data LIMIT 1"                                  # requete de suppression d'une ligne

    mycursor.execute(sqlCountRows)                                          # compte le nb de ligne dans la table
    nbligne = mycursor.fetchall()
    nb = str(nbligne[0]).split(",")
    nb = str(nb[0]).split("(")
    nb = int(nb[1])   
    if nb >= 20:                                   # si la table a plus de 20 lignes supprime la premiere 
        mycursor.execute(sqlDelete)
        mydb.commit()                              # valide la requete

    val = (nom, id_, temp, lum, ordre)              
    mycursor.execute(sqlInsertInto, val)           # enregistre les donnnees en base
    mydb.commit()                                  # valide la requete


def recuperationDonneeBDD():
    sqlSelectAll = "SELECT X, Y, Intensité FROM Capteur"         # requete permettant de recuperer les donnees
    mycursor.execute(sqlSelectAll)                                          # compte le nb de ligne dans la table
    resultat = mycursor.fetchall()
    
    if resultat :      
        print("Transmission BDD to MicroBit...")
        # sendUARTMessage("Debut")
        # sleep(15)
        for val in list(resultat):
            if val:
                val = str(val)
                sendUARTMessage(val)
        print("Fin")
        
    
    
if __name__ == '__main__':

    SERIALPORT = "/dev/ttyACM0"
    BAUDRATE = 115200
    ser = serial.Serial()
    initUART()

    mydb = mysql.connector.connect(host="localhost", user="Enagnon", passwd="bdd", database="ProjetT",)
    print("Connected to BDD")
    mycursor = mydb.cursor()
    
    while 1:
        
    
        recuperationDonneeBDD()
        sleep(10)
        # lecture donnee en BDD     
        # if data_str:
        #     data = ExtractData(data_str)
        #     nomCapteur = data[0]
        #     id_ = data[1]
        #     temp = data[2]
        #     lum = data[3]
        #     EnregistrementBdd(nomCapteur,id_,temp,lum,"TL")                
        #     LAST_VALUE = data_str

 
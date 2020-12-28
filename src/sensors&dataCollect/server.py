# coding: utf-8
import serial
import time
import mysql.connector
import argparse
import signal
import sys
import socket
import socketserver
import threading

HOST = "192.168.1.89"
UDP_PORT = 9000

MICRO_COMMANDS = ["TL", "LT"]

LAST_VALUE = ""


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
    message_bytes = bytes(msg, 'utf-8')
    ser.write(message_bytes)
    print("Message <" + msg + "> sent to micro-controller.")


def ecoute():                                    # ecoute les échanges UART et renvoi les donnees recues
    data = ser.readline()
    data = data[0:len(data)-2]
    data = data[1:len(data)-2]
    data = str(data).replace("\"","")
    data = str(data).replace("\'","")
    data = str(data).replace("b","",1)
   # print(data)
    return str(data)                          


def ExtractData(data_str):                       # extrait les donnees recu par UART 
    data_str = data_str.split(',') 
    print(data_str)
    nomCapteur = "."
    id_= temp = lum = 0
    if len(data_str) > 3 :
        nomCapteur = data_str[0]
        id_ = int(data_str[2])
        mesure = data_str[3]
        mesure = mesure.split("-")
        temp = int(mesure[0])
        lum = int(mesure[1])
    data = [nomCapteur,id_,temp, lum]           # renvoi un tableau contenant les donnees extraites 
    return data

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




if __name__ == '__main__':

    SERIALPORT = "/dev/ttyACM0"
    BAUDRATE = 115200
    ser = serial.Serial()
    initUART()
    mydb = mysql.connector.connect(
        host="localhost", user="Enagnon", passwd="bdd", database="IoT",)
    print("Connected to BDD")
    mycursor = mydb.cursor()
    server = ThreadedUDPServer((HOST, UDP_PORT), ThreadedUDPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, UDP_PORT))

        while 1:
            data_str = ecoute()   # ecoute UART
            
            if data_str:
                data = ExtractData(data_str)
                nomCapteur = data[0]
                id_ = data[1]
                temp = data[2]
                lum = data[3]
                EnregistrementBdd(nomCapteur,id_,temp,lum,"TL")                
                LAST_VALUE = data_str

    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        ser.close()
        print("Fin\n")
        exit()
 
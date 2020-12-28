# Add your Python code here. E.g.
#### Code source dataCollect #####
## Le capteur est en écoute, s'il recoit un message, il le transmet par Uart à Emergency Web Server ##
from microbit import *
import radio
import random
import os
radio.config(group=23)
radio.on()
uart.init(baudrate=115200, bits=8, parity=None, stop=1)

id_passerelle = 11

def BuildMessage(typeM,id_dest,id_emet,contenu):
    message = typeM+":"+str(id_dest)+":"+str(id_emet)+":"+contenu
    return message

def ReadMessage(donnee):
    donneeRecu = str(donnee).split(":") 
    return donneeRecu

def AnimationDisplay():
    display.show(Image("00000:""00500:""05550:""00500:""00000"))
    sleep(1000)
    display.clear()
    sleep(1000)

def EnCours():
    display.show(Image("00000:""00000:""00400:""00000:""00000"))
    sleep(300)
    display.clear()
    display.show(Image("00000:""00400:""04040:""00400:""00000"))
    sleep(300)
    display.clear()
    display.show(Image("00400:""04040:""40004:""04040:""00400"))
    sleep(300)
    display.clear()
    display.show(Image("40004:""00000:""00000:""00000:""40004"))
    sleep(200)
    display.clear()
    sleep(900)
    
def EnvoiUART(messsage):
    print(message)
                
   
display.show("Init")
display.clear()

while True:
    message = radio.receive()               # le dataCollector est en écoute
   
    if message:                             # si on recoit un message non vide
        message = ReadMessage(message)      # on decompose le message pour connaitre son type
        if ( (message[0] == "DATA" ) and (message[1] == str(id_passerelle)) ):  # si type message = data et si id_dest = id_passerelle
            emetteur = message[2]           # on recupère l'identifiant de l'emettteur
            donnee = message[3]             # on recupère le contenu du message
            # decryptage message
            EnvoiUART(message)              # envoi des donnees recu au serveur
            EnCours()                       # animation led
            radio.send(BuildMessage("ACK",emetteur,id_passerelle,""))     # envoi d'un message de confirmation au capteur
                
    else:
        AnimationDisplay()                  # animation 
        
        
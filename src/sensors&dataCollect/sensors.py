# Add your Python code here. E.g.
from microbit import *
import radio
import os

radio.config(group=23)
radio.on()
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
CLE = 10
ID_CAPTEUR = 11
ID_PASSERELLE = 1111

def EnCours():
    display.show(Image("00000:""00000:""00400:""00000:""00000"))
    sleep(100)
    display.clear()
    display.show(Image("00000:""00400:""04040:""00400:""00000"))
    sleep(100)
    display.clear()
    display.show(Image("00400:""04040:""40004:""04040:""00400"))
    sleep(100)
    display.clear()
    display.show(Image("40004:""00000:""00000:""00000:""40004"))
    sleep(100)
    display.clear()
    sleep(100)
    
def Encrypt(msg,cle):
    crypt = ""
    for i in range(len(msg)):
        if (ord(msg[i])+cle)<127:
            crypt+=chr(ord(msg[i])+cle)
        else:
            crypt+=chr(ord(msg[i])+cle-95)
    return crypt
    
def BuildMessage(typeM,id_dest,id_emet,contenu):
    message = typeM+":"+str(id_dest)+":"+str(id_emet)+":"+contenu
    return message    

while True:
    
    if (uart.any()):                                # ecoute uart
        msg = uart.read()                     # recuperer donnees(bytes) uart 
        data=BuildMessage("DATA",ID_PASSERELLE,ID_CAPTEUR,msg)
        print(data)
        radio.send(data)   
        
   #     print(msg)
        
    #    data=Encrypt(str(msg,'utf-8'),CLE)    # encrypt les donnees
    #    tosend = BuildMessage("DATA",ID_PASSERELLE,ID_CAPTEUR,data)
    #    radio.send(tosend)                    #envoi les donnees encryptées(str) et formatées
        EnCours()
                
    display.scroll("...")
    

# Add your Python code here. E.g.
from microbit import *
import radio
import os
radio.on()
radio.config(group=23)
radio.config(length=80)
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
CLE = 1
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
        data = str(msg,'UTF-8')
        data=Encrypt(data,CLE) 
        radio.send(BuildMessage("DATA",ID_PASSERELLE,ID_CAPTEUR,data))  
        EnCours()
                
    display.scroll("...")
    

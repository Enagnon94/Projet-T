# Add your Python code here. E.g.
#### Code source dataCollect #####
## Le capteur est en écoute, s'il recoit un message, il le transmet par Uart à Emergency Web Server ##


# Add your Python code here. E.g.
from microbit import *
import radio
import os

radio.config(group=23)
radio.on()
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
CLE = 10
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
        

def Decrypt(msg,cle):
    decrypt = ""
    for i in range(len(msg)):
        if (ord(msg[i])-cle)>31:
            decrypt+=chr(ord(msg[i])-cle)
        else:
            decrypt+=chr(ord(msg[i])-cle+95)
    return decrypt
    
def ReadMessage(donnee):
    donneeRecu = str(donnee).split(":") 
    return donneeRecu

while True:
    
    msg = radio.receive()
    if msg:
        data = Decrypt(msg)
        data = ReadMessage(data)
        if data[0] == "DATA" and data[2] == ID_PASSERELLE:
            display.scroll(data[3])
            print(data[3])
            EnCours()
            
    


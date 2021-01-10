# Add your Python code here. E.g.
#### Code source dataCollect #####
## Le capteur est en écoute, s'il recoit un message, il le transmet par Uart à Emergency Web Server ##
# Add your Python code here. E.g.
from microbit import *
import radio
import os

radio.on()
radio.config(group=23,length=78)
uart.init(baudrate=115200, bits=8, parity=None, stop=1)
CLE = 10
ID_PASSERELLE = "1111"


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
        display.show(Image("00000:""00000:""00700:""00000:""00000"))
        data = ReadMessage(msg)
        if ((data[0] == "DATA") and (data[1] == ID_PASSERELLE)):
           #  contenu = Decrypt(data[3],CLE)
           contenu = data[3]
           print(contenu)
        #    display.scroll(contenu)
   #     EnCours()
        display.clear()
            
    



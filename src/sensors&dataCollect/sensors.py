
# Add your Python code here. E.g.
from microbit import *
import radio

radio.config(group=23)
radio.on()
initialize(pinReset=pin0)
id_passerelle = 11
id_capteur = "BRD-C-928"
i = 0

    
def BuildMessage(typeM,id_dest,id_emet,contenu):
    message = typeM+":"+str(id_dest)+":"+str(id_emet)+":"+str(contenu)
    return message

def ReadMessage(donnee):
    donneeRecu = str(donnee).split(":")
    return donneeRecu
    
def Mesure():                                                   # Prise des mesures 
    dataTemp = temperature()                                    # temperature
    dataLum = display.read_light_level()                        # luminosite ( entre 0 = sombre et 255 = clair )
    data = str(dataTemp) +":"+ str(dataLum)                     # concatenation donnees
    return data

def EnvoiDonneePasserelle(data):                    # Envoi un message a la passerelle
    data = data[0]+"-"+data[1]
    # encrypter donnees
    radio.send(BuildMessage("DATA",id_passerelle,id_capteur,data))



display.show("Capteur")
display.clear()
while True:
    display.show("Press B to start")
    if  button_b.was_pressed():                 # si on appuie sur le bouton b
        display.clear()
        while True:
            data = Mesure()                     # generation mesure capteur
            EnvoiDonneePasserelle(data)         # envoi les donnees a la passerelle
            sleep(50)   
            message = radio.receive()           # ecoute reponse
            reponse = ReadMessage(message)
            while ( (reponse[0] != "ACK") and (reponse[1] != id_capteur) ) :
                EnvoiDonneePasserelle(data)         # envoi les donnees a la passerelle
                reponse = ReadMessage(radio.receive())
                i += 1
                sleep(50)
                if (i == 5):
                        i = 0
                        break 
            i = 0
            sleep(1000)                                 # prise, affichage et envoi des mesures toutes les 200ms
   
         
     
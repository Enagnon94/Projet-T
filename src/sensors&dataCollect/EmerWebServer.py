## Emergency Web Server##
## En écoute, s'il recoit un message par UART du dataCollector, il le traite et le publie en MQTT ##

# import paho.mqtt.client as mqtt
import serial
import mysql.connector

def init_uart():
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

def ecoute():
    data=ser.readline()
    return str(data)



if __name__ == '__main__':
        SERIALPORT = "/dev/ttyACM0"                             # port pour comm. UART
        BAUDRATE = 115200
        ser = serial.Serial()
        init_uart()

    # mydb = mysql.connector.connect(host="localhost", user="Enagnon", passwd="bdd", database="ProjetT",)
    # print("Connected to BDD")
    # mycursor = mydb.cursor()

        while True:
                #
                data_str = ecoute()   # ecoute UART
                if data_str:
                    print(data_str)


        # client = mqtt.Client()
        # client._client_id = "EmerWebServ"

        # client.connect(host="127.0.0.1", port=1883, keepalive=60, bind_address='', bind_port=0,  properties=None,)
        # #client.loop_start()              # cree un thread pour la comm

        # mm = client.publish(topic="Test/Capteur", payload="Kwabo, ceci est un test", qos=1,retain=False)

        # print(str(mm.is_published()))

        #client.loop_stop() 
        #client.loop_forever()


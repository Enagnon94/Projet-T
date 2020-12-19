import paho.mqtt.client as mqtt

client = mqtt.Client()
client._client_id = "0"

client.connect(host="127.0.0.1", port=1883, keepalive=60, bind_address='', bind_port=0,  properties=None,)
#client.loop_start()              # cree un thread pour la comm

mm = client.publish(topic="Test/Capteur", payload="Kwabo, ceci est un test", qos=1,retain=False)

print(str(mm.is_published()))
#client.loop_stop() 
#client.loop_forever()

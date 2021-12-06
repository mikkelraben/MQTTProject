#Backend
import paho
import paho.mqtt.client as mqtt

ip = "85.184.168.11"
port = 1883

Username = "19xvz"
Password = "msg007"
Client_id = f"MikkelMarkus"

def on_connect(client,obj,flags,rc):
    print(f"Oprettede forbindelse {str(rc)}")


client = mqtt.Client()
client.username_pw_set(Username,Password)
client.on_connect = on_connect
client.connect(ip,port,60)

client.loop_forever()



#Backend
from ctypes import c_longdouble
import paho
import paho.mqtt.client as mqtt

ip = "85.184.168.11"
port = 1883

Username = "19xvz"
Password = "msg007"
Client_id = f"MikkelMarkus"

def on_connect(client,obj,flags,rc):
    print(f"Oprettede forbindelse {str(rc)}")

def on_sub(client,userdata,mid):
    print()

def on_publish(client, userdata, mid):
    print()

def on_message(client, userdata, msg):
    print()


client = mqtt.Client()
client.username_pw_set(Username,Password)
client.on_connect = on_connect
client.on_subscribe = on_sub
client.on_publish = on_publish
client.on_message = on_message
client.connect(ip,port,60)


rc = 0
while rc == 0:
    rc = client.loop()





#Backend
import paho
import paho.mqtt.client as mqtt

ip = "85.184.168.11"
port = 1883

Username = "19xvz"
Password = "msg007"
Client_id = f"Mikkel&Markus"

#Event functions

def on_connect(client,obj,flags,rc):
    print(f"Oprettede forbindelse med koden: {str(rc)}")

def on_subscribe(client,userdata,mid,qos):
    print(f"You have subscribed to {str(mid)}")

def on_unsubscribe(client,userdata,mid):
    print(f"You have unsubscribed to {str(mid)}")

def on_publish(client, userdata, mid):
    print(f"Your message has been published to {str(mid)}")

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {str(msg.payload)}")


#Functions
def subscribe():
    pass

def unsubscribe():
    pass

def publish():
    pass


client = mqtt.Client()

client.username_pw_set(Username,Password)

#Assign the events to our event functions
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_publish = on_publish
client.on_message = on_message


client.connect(ip,port,60)



rc = 0
while rc == 0:
    rc = client.loop()





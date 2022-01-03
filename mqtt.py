#Backend
import paho
import paho.mqtt.client as mqtt

ip = "85.184.168.11"
port = 1883

Username = "19xvz"
Password = "msg007"
Client_id = f"Markus"

subs_dict = {}
pub_dict = {}

#Event functions

def on_connect(client,obj,flags,rc):
    print(f"Oprettede forbindelse med koden: {str(rc)}")

def on_subscribe(client,userdata,mid,qos):
    print(f"You have subscribed to {subs_dict[mid]}")

def on_unsubscribe(client,userdata,mid):
    print(f"You have unsubscribed to {subs_dict(mid)}")

def on_publish(client, userdata, mid):
    print(f"Your message has been published to {str(mid)}")

def on_message(client, userdata, msg):
    msg.payload.decode()
    text = f"{msg.topic}, {userdata}: {str(msg.payload)[2:-1]}"
    print(text)


#Functions
def subscribe(topic):
    r = client.subscribe(f"M&M/{topic}",0)
    print(r)
    subs_dict[r[1]] = topic
    print(subs_dict)
    pass

def unsubscribe(topic):
    client.unsubscribe(topic)
    pass

def publish(topic, msg):
    client.publish(f"M&M/{topic}", msg)
    pass

def disconnet():
    client.disconnect()


client = mqtt.Client()
client.username_pw_set(Username,Password)

client.user_data_set(Client_id)

#Assign the events to our event functions
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_publish = on_publish
client.on_message = on_message


client.connect(ip,port,60)

subscribe("test")
publish("test","Test upload")


rc = 0
while rc == 0:
    rc = client.loop()





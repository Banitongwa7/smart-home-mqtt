import paho.mqtt.client as mqtt
from devices import LightBulb

# The callback for when the client receives a CONNACK response from the server.

def on_lightbulb_setstate(client, userdata, msg):
    # This callback will only be called for messages with topics that match the device topic
    print(msg.topic+" "+str(msg.payload))
    state = int(msg.payload)
    lightbulb.set_state(state)

def on_lightbulb_setcolor(client, userdata, msg):
    # This callback will only be called for messages with topics that match the device topic
    print(msg.topic+" "+str(msg.payload))
    color = msg.payload
    lightbulb.set_color(color)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    lightbulb.register_setstate(on_lightbulb_setstate)
    lightbulb.register_setcolor(on_lightbulb_setcolor)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

lightbulb = LightBulb(client, "lightbulb")

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
import random

APPLICATION_KEY = "0000"

class SmartDevice:
    def __init__(self, mqtt_client, name):
        self.client = mqtt_client
        self.name = name

    def notify(self, publish_topic, data_to_publish):
        print("Publish {} on topic {}".format(data_to_publish,publish_topic))
        self.client.publish(publish_topic, data_to_publish)

    def simulate_measurment(self, values_list):
        return random.choice(values_list)

class LightBulb(SmartDevice):
    def __init__(self, mqtt_client, name):
        SmartDevice.__init__(self, mqtt_client, name)
        self.color = '#000000'
        self.state = False
        self.setstate_topic ="home/{}/{}/setstate".format(APPLICATION_KEY, self.name)
        self.state_topic = "home/{}/{}/state".format(APPLICATION_KEY,self.name)
        self.setcolor_topic ="home/{}/{}/setcolor".format(APPLICATION_KEY, self.name)
        self.color_topic = "home/{}/{}/color".format(APPLICATION_KEY,self.name)

    def register_setstate(self, on_setstate):
        self.client.subscribe(self.setstate_topic)
        self.client.message_callback_add(self.setstate_topic,on_setstate)

    def register_setcolor(self, on_setcolor):
        self.client.subscribe(self.setcolor_topic)
        self.client.message_callback_add(self.setcolor_topic,on_setcolor)

    def set_state(self, state):
        self.state = state
        self.notify(self.state_topic, state)

    def set_color(self, color):
        self.color = color
        self.notify(self.color_topic, color)


class RollerBlind(SmartDevice):
    def __init__(self, mqtt_client, name):
        SmartDevice.__init__(self, mqtt_client, name)
        self.color = '#000000'
        self.state = False
        self.setstate_topic ="home/{}/{}/setstate".format(APPLICATION_KEY, self.name)
        self.state_topic = "home/{}/{}/state".format(APPLICATION_KEY,self.name)
        self.setcolor_topic ="home/{}/{}/setcolor".format(APPLICATION_KEY, self.name)
        self.color_topic = "home/{}/{}/color".format(APPLICATION_KEY,self.name)

    def register_setstate(self, on_setstate):
        self.client.subscribe(self.setstate_topic)
        self.client.message_callback_add(self.setstate_topic,on_setstate)

    def register_setcolor(self, on_setcolor):
        self.client.subscribe(self.setcolor_topic)
        self.client.message_callback_add(self.setcolor_topic,on_setcolor)
    
    def set_state(self, state):
        self.state = state
        self.notify(self.state_topic, state)
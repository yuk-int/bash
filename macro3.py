#macro3.py to receive mqtt data from macro4.py
#macro4.py
#breadbaord with LED light and button
#use button to toggle LED light

import paho.mqtt.client as mqtt
#from paho.mqtt import client as client
import redis

redis_conn = redis.Redis(host='localhost', port=6379, password='redispass')

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    print (f"topic={topic}, message={message}")

if __name__ == '__main__':
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect('127.0.0.1')
    client.subscribe('btn/func1', qos=2)
    client.loop_forever()
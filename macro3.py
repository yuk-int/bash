#macro3.py to receive mqtt data from macro4.py
#macro4.py
#breadbaord with LED light and button
#use button to toggle LED light

import paho.mqtt.client as mqtt
#from paho.mqtt import client as client
import redis
from dotenv import load_dotenv
import os
import json
from datetime  import datetime
import macro1_1

load_dotenv()

#redis_conn = redis.Redis(host='localhost', port=6379, password='redispass')
redis_conn = redis.Redis(host='localhost', port=6379)
render_redis_conn=redis.Redis.from_url(os.environ['render_redis'])


def on_message(mosq, obj, msg):
    print (msg)
    topic = msg.topic
    print (topic)
    message = msg.payload.decode('utf-8')
    print (message)
    redis_conn.rpush(topic,message)
    render_redis_conn.rpush(topic,message)
    print (f"topic={topic}, message={message}")
    #文字轉為dictionary
    message_dict = json.loads(s=message)
    print (message_dict)
    now = datetime.now()
    new_log_file = now.strftime('%Y_%m_%d.log')
    log_path = macro1_1.create_log_file(new_log_file)
    macro1_1.record_info(log_path=log_path, topic=message_dict['topic'], date=message_dict['date'], status=message_dict['status'])

if __name__ == '__main__':
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(username=os.environ['mqtt_username'], password=os.environ['mqtt_password'])
    client.on_message = on_message
    client.connect('127.0.0.1')
    client.subscribe('btn/func1', qos=2)
    client.loop_forever()
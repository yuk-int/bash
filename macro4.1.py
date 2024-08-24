#breadbaord with LED light and button
#use button to toggle LED light

import signal
import RPi.GPIO as GPIO
from gpiozero import Button
from gpiozero import LED
from datetime import datetime
from time import sleep
import paho.mqtt.publish as publish

def initialization():
    button = Button(pin=18)
    red = LED(pin=25)
    print ("initialization is done!")
    return button, red

def twinkle():
    #red.blink()
    print("hello")

def action():
    red.toggle()
    print("botton is toggled")
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    if red.is_lit:
        print(f"light is ON_{now_str}")
        message=f"light is ON_{now_str}"
        publish.single(topic="btn/func1", payload=message, hostname="localhost", qos=2)
        #print ("mqtt-publish1")
    else:
        print(f"light is OFF_{now_str}")
        message=f"light is OFF_{now_str}"
        publish.single(topic="btn/func2", payload=message, hostname="localhost", qos=2)
        #print ("mqtt-publish2")


'''
while True:
    if button.is_pressed:
        print("Button is pressed")
        red.on()
    else:
        print("Button is not pressed")
'''

if __name__ == '__main__':
    button, red = initialization()
    button.when_released = action
    #button.when_released = twinkle
    #red.on()
    signal.pause()

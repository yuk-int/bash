import signal
import RPi.GPIO as GPIO
from gpiozero import Button
from gpiozero import LED
from time import sleep

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
    print("button is pressed")

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
    red.on()
    signal.pause()
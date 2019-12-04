from gpiozero import LED
import RPi.GPIO as GPIO
from random import random
from time import sleep

nG = LED(17)
nY = LED(27)
nR = LED(22)

sG = LED(25)
sY = LED(24)
sR = LED(5)

vG = LED(26)
vY = LED(19)
vR = LED(13)

eG = LED(16)
eY = LED(20)
eR = LED(21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN) #vCar
GPIO.setup(23,GPIO.IN) #nCar
GPIO.setup(4,GPIO.IN) #sCar
GPIO.setup(18,GPIO.IN) #eCar

nR.on()
sR.on()
vR.on()
eR.on()

def state0():
    sR.on()
    vR.on()
    eR.on()
    nY.on()
    sleep(1)
    nR.off()
    nY.off()
    nG.on()
    sleep(5.5)
    if (GPIO.input(4)):
        return state1
    if (GPIO.input(12)):
        return state2
    if (GPIO.input(18)):
        return state3

def state1():
    nR.on()
    vR.on()
    eR.on()
    nY.on()
    sleep(1)
    sR.off()
    sY.off()
    sG.on()
    sleep(5.5)
    if (GPIO.input(23)):
        return state0
    if (GPIO.input(12)):
        return state2
    if (GPIO.input(18)):
        return state3

def state2():
    sR.on()
    nR.on()
    eR.on()
    vY.on()
    sleep(1)
    vR.off()
    vY.off()
    vG.on()
    sleep(5.5)
    if (GPIO.input(4)):
        return state1
    if (GPIO.input(23)):
        return state0
    if (GPIO.input(18)):
        return state3

def state3():
    sR.on()
    vR.on()
    nR.on()
    eY.on()
    sleep(1)
    eR.off()
    eY.off()
    eG.on()
    sleep(5.5)
    if (GPIO.input(4)):
        return state1
    if (GPIO.input(12)):
        return state2
    if (GPIO.input(23)):
        return state0
    
state=state0
while state: state=state()

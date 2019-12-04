from gpiozero import LED, Button
from signal import pause
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
ledr = LED(13)
ledy = LED(19)
ledg = LED(26)
camera = PiCamera()
button = Button(2)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
sekvens = 0
overgang = False
while True:
    if (GPIO.input(17)):
        sekvens = 1
            
    if overgang == True:
        sekvens = 2
    
    
    
    
    
    if sekvens == 0:
        ledr.on()
        ledg.off()
        ledy.off()
        overgang = False
    
    if sekvens == 1 and not overgang:
        ledy.on()
        sleep(.5)
        kodeord = str(input("Indtast password"))
        if kodeord == "Fortnite":
            overgang = True
        else:
            ledr.on()
            ledy.off
            camera.start_preview()
            sleep(.2)
            ledr.off()
            camera.capture('/home/pi/Desktop/image1.jpg')
            camera.stop_preview()
        
    if sekvens == 2:
        ledy.off()
        ledr.off()
        ledg.on()
        sleep(0.2)
        ledg.off()
        sleep(0.2)
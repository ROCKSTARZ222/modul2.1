from gpiozero import LED, Button
from time import sleep

ledgreen1 = LED(17)
ledyellow1 = LED(27)
ledred1 = LED(22)
ledgreen2 = LED(26)
ledyellow2 = LED(19)
ledred2 = LED(13)
button = Button(2)

while True:

    if button.when_pressed == True:
        ledgreen1.off()
        ledyellow1.off()
        ledred1.on()
        ledgreen2.on()
        ledyellow2.off()
        ledred2.off()

        sleep(2)

        ledgreen1.off()
        ledyellow1.on()
        ledred1.on()

        ledyellow2.on()
        ledred2.off()

        sleep(2)
    
        ledgreen1.on()
        ledyellow1.off()
        ledred1.off()
        ledgreen2.off()
        ledyellow2.off()
        ledred2.on()
    
        sleep(2)
    

        ledyellow1.on()
        ledred1.off()
        ledgreen2.off()
        ledyellow2.on()
        ledred2.on()
    
        sleep(2)
    else:
        ledgreen1.on()
        ledgreen2.off()
        sleep(0.2)
        ledgreen1.off()
        ledgreen2.on()
        sleep(0.2)
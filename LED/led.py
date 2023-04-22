import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)

greenled = 27
redled = 17

rg.setup(greenled, rg.OUT)
rg.setup(redled, rg.OUT)

try:
    while True:
        rg.output(greenled, rg.LOW)
        rg.output(redled, rg.HIGH)
        time.sleep(1)
        
        rg.output(greenled, rg.HIGH)
        rg.output(redled, rg.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    rg.cleanup()

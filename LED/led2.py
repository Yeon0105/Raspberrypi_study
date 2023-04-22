import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BCM)

LED0 = 5
LED1 = 6
LED2 = 27
LED3 = 17
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

try:
    while True:
        sec = datetime.now().second % 16
        print(f"current second: {sec}")
        GPIO.output(LED0, (sec>>3)&1)
        GPIO.output(LED1, (sec>>2)&1)
        GPIO.output(LED2, (sec>>1)&1)
        GPIO.output(LED3, (sec>>0)&1)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

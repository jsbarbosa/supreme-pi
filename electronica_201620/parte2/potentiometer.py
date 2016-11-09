import RPi.GPIO as GPIO
from digiPi import potentiometer
import time


p1 = potentiometer(16, 20, 21, 10e3)

time.sleep(1)
for i in range(1,20):
    p1.set_to_digital(5*i)
    time.sleep(1)
    print(i)
time.sleep(2)

GPIO.cleanup()

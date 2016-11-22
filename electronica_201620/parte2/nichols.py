"""
    Potentiometer calibration
"""

import csv
import numpy as np
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from controller import potentiometer
from time import sleep

adc = Adafruit_ADS1x15.ADS1115()
pot = potentiometer((19, 20, 21), 100e3)

GAIN = 4
maximum = 32767.0
gain_voltage = 1.024

data = open('Nichols.csv', 'w')
writer = csv.writer(data)

init_text = ["Sensor", "Error"]
writer.writerow(init_text)

N = 10
format = "| {0:>10} | {1:>10}"

pot.change(100)

sensor = 0
ref = 1

while True:
    try:
        temp_sensor = 100*adc.read_adc(sensor, gain=GAIN)*gain_voltage/maximum
        temp_ref = 100*adc.read_adc(ref, gain=GAIN)*gain_voltage/maximum

        error = temp_ref - temp_sensor
        info = [temp_sensor, error]

        writer.writerow(info)
        print(format.format(*info))
        sleep(1)
        
    except KeyboardInterrupt:
        break
    
data.close()
GPIO.cleanup()

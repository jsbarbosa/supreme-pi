"""
    Potentiometer calibration
"""

import csv
import numpy as np
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from controller import potentiometer

adc = Adafruit_ADS1x15.ADS1115()
pot = potentiometer((19, 20, 21), 100e3)

GAIN = 4
maximum = 32767.0
gain_voltage = 1.024

data = open('potentiometer_cal2.csv', 'w')
writer = csv.writer(data)

init_text = ["Wiper", "Voltage (V)", "std (V)"]
writer.writerow(init_text)

N = 10

buffer = np.zeros(N)

for i in range(101):
    pot.change(i)
    j = 0
    while j < N:
        buffer[j] = adc.read_adc(1, gain=GAIN)*gain_voltage/maximum
        j += 1
    avg = np.mean(buffer)
    std = np.std(buffer)

    results = [i, avg, std]
    writer.writerow(results)

data.close()
GPIO.cleanup()

import matplotlib.pyplot as plt

data = np.genfromtxt('potentiometer_cal2.csv', delimiter = ",")
x = data[1:,0]
y = data[1:,1]
err = data[1:,2]
plt.plot(x, y, "-o", ms = 2)
plt.errorbar(x, y, xerr = err)
plt.xlabel('Wiper')
plt.ylabel('Voltage (V)')
plt.grid()
plt.xlim(0, 100)
plt.ylim(y[0], y[-1])
plt.savefig('potentiometer_cal2.pdf')
plt.close()

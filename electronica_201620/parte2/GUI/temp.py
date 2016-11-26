import Adafruit_ADS1x15
import numpy as np
from time import sleep

MAXIMUM = 32767.0

adc = Adafruit_ADS1x15.ADS1115()

values = np.zeros(4)
while True:
    try:
        for i in range(4):
            values[i] = adc.read_adc(i, gain = 4)

        values = 1.024*values/MAXIMUM
        print("\033c")
        print(values)
        sleep(0.1)        

    except KeyboardInterrupt:
        break

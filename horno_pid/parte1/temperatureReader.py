import time
import Adafruit_ADS1x15
import csv
#import RPi.GPIO as GPIO
from datetime import datetime

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(4, GPIO.OUT)
#GPIO.output(4, GPIO.HIGH)

maximum = 32767.0
gain_voltage = 1.024#4.096
GAIN = 4
adc = Adafruit_ADS1x15.ADS1115()

data = open('results.csv', 'a')
writer = csv.writer(data)

#on = True

init_text = ["Hora", "Temperatura (C)"]
print("| {0:>10} | {1:>15} |".format(*init_text))

writer.writerow(init_text)
while True:
    try:
        voltage = adc.read_adc(0, gain=GAIN)
        temperature = voltage/maximum*gain_voltage*100
        actual_time = datetime.now().strftime("%H:%M:%S")
        results = [actual_time, "%.2f"%temperature]
        
        writer.writerow(results)
        print('| {0:>10} | {1:>15} |'.format(*results))
        time.sleep(1)
    except KeyboardInterrupt:
        data.close()
        exit()

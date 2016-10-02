# based on https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py

import Adafruit_DHT
import time
from datetime import datetime
import csv

def dataUpdate(file, data):
    f = open(file, "a")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

# Sensor
sensor = Adafruit_DHT.DHT11

# GPIO4.
pin = 4

init_text = ["Time", "Temperature (C)", "Humidity (%)"]
format_text = "| {0:<10} | {1:<15} | {2:<13} |"
print(format_text.format(*init_text))

file = "DHT_results.csv"

dataUpdate(file, init_text)
while True:
    try:
        humidity, temperature = Adafruit_DHT.read(sensor, pin)

        if humidity is not None and temperature is not None:
            date = datetime.now().strftime("%H:%M:%S")
            res = [date, temperature, humidity]
            print(format_text.format(*res))

            dataUpdate(file, res)
            time.sleep(1)
    except KeyboardInterrupt:
        break

exit()

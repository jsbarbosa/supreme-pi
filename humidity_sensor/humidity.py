import Adafruit_DHT
import time
from datetime import datetime
import csv

def dataUpdate(file, data):
    f = open(file, "a")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

init_text = ["Time", "Temperature (C)", "Humidity (%)"]
format_text = "| {0:<10} | {1:<15} | {2:<13} |"
print(format_text.format(*init_text))

file = "DHT_results.csv"

dataUpdate(file, init_text)
while True:
    try:
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read(sensor, pin)

        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).
        # If this happens try again!
        if humidity is not None and temperature is not None:
            date = datetime.now().strftime("%H:%M:%S")
            res = [date, temperature, humidity]
            print(format_text.format(*res))

            dataUpdate(file, res)
            time.sleep(1)
    except KeyboardInterrupt:
        break

exit()

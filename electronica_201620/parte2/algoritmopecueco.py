from controller import potentiometer
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

pot = potentiometer((19, 20, 21))
adc = Adafruit_ADS1x15.ADS1115()

def printer(voltage):
    pot.set_to(voltage)
    var = 1.024*adc.read_adc(1, gain=4)/32767.0
    print(var)

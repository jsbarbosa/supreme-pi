# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:35:21 2016

@author: juan
"""

try:
    import RPi.GPIO as GPIO
    import Adafruit_ADS1x15
    GPIO.setmode(GPIO.BCM)
except Exception as e:
    print("Test ", e)

from time import sleep
import numpy as np

MAXIMUM = 32767.0

class tester:
    def __init__(self):
        pass
    
    def read_adc(self, channel, gain = 1):
        return np.random.rand()*MAXIMUM
        
    def change(self, value):
        self.value = value

class controller:
    def __init__(self, pot_pins):
        self.maximum = MAXIMUM
        self.gain_voltage = 1.024
        self.GAIN = 4
        
        try:
            self.pot = potentiometer(pot_pins)
        except:
            self.pot = tester()
                
        try:
            self.ADC = Adafruit_ADS1x15.ADS1115()
        except NameError:
            self.ADC = tester()

        self.temperature, self.reference = self.from_bits_to_value(0), self.from_bits_to_value(1)
        
        self.pot.change(0)
        self.pot.change(100)
        
        self.v_min = self.pot.change(0)
        self.v_max = self.pot.change(100)
        
        self.desired_temperature = 0
        
    def from_bits_to_value(self, channel):
        temp = self.ADC.read_adc(channel, gain=self.GAIN)
        return (temp*self.gain_voltage*100)/self.maximum
        
    def read(self):
        self.temperature = self.from_bits_to_value(0)
        self.reference = self.from_bits_to_value(1)
        return self.temperature, self.reference
        
    def change_pot(self, value):
        self.pot.change(value)
        
    def set_desired(self, value):
        self.desired_temperature = value
        m = 100*(self.desired_temperature-self.v_min)/(self.v_max-self.v_min)
        m = int(np.around(m))
        self.change_pot(m)
        
    def close(self):
        GPIO.cleanup()
        
class potentiometer:
    def __init__(self, pins):
        self.pins = {"IC": pins[0], "UD": pins[1], "CS": pins[2]}
        self.value = 0

        self.time = 0.001
        
        for pin in self.pins:
            GPIO.setup(self.pins[pin], GPIO.OUT)
            GPIO.output(self.pins[pin], GPIO.LOW)
            
        GPIO.output(self.pins["IC"], GPIO.HIGH)
            
    def increase(self, value):
        GPIO.output(self.pins["UD"], GPIO.HIGH)
        while self.value < value:
            GPIO.output(self.pins["IC"], GPIO.LOW)
            sleep(self.time)
            GPIO.output(self.pins["IC"], GPIO.HIGH)
            sleep(self.time)
            self.value += 1
            
    def decrease(self, value):
        GPIO.output(self.pins["UD"], GPIO.LOW)
        while self.value > value:
            GPIO.output(self.pins["IC"], GPIO.LOW)
            sleep(self.time)
            GPIO.output(self.pins["IC"], GPIO.HIGH)
            sleep(self.time)
            self.value -= 1
            
    def change(self, value):
        if self.value > value:
            self.decrease(value)
        else:
            self.increase(value)

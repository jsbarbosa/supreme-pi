# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:35:21 2016

@author: juan
"""

try:
    import RPi.GPIO as GPIO
    import Adafruit_ADS1x15
except:
    print("Test")

import numpy as np

MAXIMUM = 32767.0

class tester:
    def __init__(self):
        pass
    
    def read_adc(self, channel, gain = 1):
        return np.random.rand()*MAXIMUM
        

class controller:
    def __init__(self, kp_pins, ki_pins, kd_pins, k_values):
        self.maximum = MAXIMUM
        self.gain_voltage = 1.024
        self.GAIN = 4
        
        try:
            self.ADC = Adafruit_ADS1x15.ADS1115()
        except NameError:
            self.ADC = tester()
        self.temperature = self.from_bits_to_value()
        self.variables = {}
        
    def from_bits_to_value(self):
        voltage = self.ADC.read_adc(0, gain=self.GAIN)
        temperature = (voltage/self.maximum)*self.gain_voltage*100
        return temperature
        
    def read(self):
        self.temperature = self.from_bits_to_value()
        return self.temperature
        
class resistor:
    def __init__(self):
        pass
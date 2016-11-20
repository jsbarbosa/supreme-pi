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
    def __init__(self, kp_pins, ki_pins, kd_pins, k_values):
        self.maximum = MAXIMUM
        self.gain_voltage = 1.024
        self.GAIN = 4
        
        try:
            self.kp = potentiometer(kp_pins, k_values[0])
            self.ki = potentiometer(ki_pins, k_values[1])
            self.kd = potentiometer(kd_pins, k_values[2])
        except:
            self.kp = tester()
            self.ki = tester()
            self.kd = tester()
                
        try:
            self.ADC = Adafruit_ADS1x15.ADS1115()
        except NameError:
            self.ADC = tester()

        self.temperature = self.from_bits_to_value()
        self.desired_temperature = 0
        
    def from_bits_to_value(self):
        voltage = self.ADC.read_adc(0, gain=self.GAIN)
        temperature = (voltage/self.maximum)*self.gain_voltage*100
        return temperature
        
    def read(self):
        self.temperature = self.from_bits_to_value()
        return self.temperature
        
    def change_pid(self, values):
        self.kp.change(values[0])
        self.ki.change(values[1])
        self.kd.change(values[2])
        
    def close(self):
        GPIO.cleanup()
        
class potentiometer:
    def __init__(self, pins, resistor):
        self.pins = {"IC": pins[0], "UD": pins[1], "CS": pins[2]}
        self.resistor = resistor
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

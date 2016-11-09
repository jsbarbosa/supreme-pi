# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 06:11:23 2016

@author: juan
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

class potentiometer:
    def __init__(self, pINC_PIN, pUD_PIN, pCS_PIN, value):
        self.INC_PIN = pINC_PIN
        self.UD_PIN = pUD_PIN
        self.CS_PIN = pCS_PIN
        
        self.POS = 0
        self.VALUE = value
        
        GPIO.setup(self.INC_PIN, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.UD_PIN, GPIO.OUT)
        GPIO.setup(self.CS_PIN, GPIO.OUT)
        
    def increase(self, desired_pos):
        time = 1/(desired_pos - self.POS)
        
        GPIO.output(self.UD_PIN, GPIO.HIGH)
        while self.POS < desired_pos:
            GPIO.output(self.INC_PIN, GPIO.LOW)
            sleep(time)
            GPIO.output(self.INC_PIN, GPIO.HIGH)
            self.POS += 1
            
        GPIO.output(self.CS_PIN, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.CS_PIN, GPIO.LOW)
        
    def decrease(self, desired_pos):
        pos = self.POS
        time = 1/(desired_pos - self.POS)
        
        GPIO.output(self.UD_PIN, GPIO.LOW)
        while desired_pos < pos:
            GPIO.output(self.INC_PIN, GPIO.LOW)
            sleep(time)
            GPIO.output(self.INC_PIN, GPIO.HIGH)
            self.POS -= 1
        GPIO.output(self.CS_PIN, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.CS_PIN, GPIO.LOW)
            
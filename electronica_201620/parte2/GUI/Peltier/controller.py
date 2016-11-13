# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:35:21 2016

@author: juan
"""
try:
    import RPi.GPIO as GPIO
except:
    print("Test")

class controller:
    def __init__(self):
        self.temperature
        self.variables = {}
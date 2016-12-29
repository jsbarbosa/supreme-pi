#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  arpa_code.py
#  
#  Copyright 2016 Juan Barbosa <juan@Lenovo-U410>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # GPIO.BCM

channels_in = [12]
channels_out = [13]
PWMs = [None]*len(channels_in)
freqs = [250]


def init():
    for i in range(len(channels_in)):
        GPIO.setup(channels_in[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(channels_out[i], GPIO.OUT)
        GPIO.add_event_detect(channels_in[i], GPIO.BOTH, callback=status)
        
        PWMs[i] = GPIO.PWM(channels_out[i], freqs[i])

def status(channel):
    pos = channels_in.index(channel)
    if GPIO.input(channel):
        PWMs[pos].start(50.0) # duty cycle
        print('STARTED: %d Hz'%freqs[pos])
    else:
        PWMs[pos].stop()
        print('STOPED: %d Hz'%freqs[pos])

def main():
    init()
    while True:
		try:
			sleep(0.1)
		except KeyboardInterrupt:
			break

if __name__ == '__main__':
    main()

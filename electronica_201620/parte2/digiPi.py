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
        
        GPIO.setup(self.INC_PIN, GPIO.OUT, initial = GPIO.HIGH)
        GPIO.setup(self.UD_PIN, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.CS_PIN, GPIO.OUT, initial = GPIO.LOW)

        zero_pwm = GPIO.PWM(self.INC_PIN, 99)
        zero_pwm.start(90)
        sleep(1)
        zero_pwm.stop()

        print('Setting potentiometer')
        
    def increase(self, desired_pos):
        time = 0.01/(desired_pos - self.POS)
        self.POS = 0
        GPIO.output(self.UD_PIN, GPIO.HIGH)
        while self.POS < desired_pos:
            GPIO.output(self.INC_PIN, GPIO.HIGH)
            sleep(time/2)
            GPIO.output(self.INC_PIN, GPIO.LOW)
            sleep(time/2)
            self.POS += 1
        
    def decrease(self, desired_pos):
        time = 1/(desired_pos - self.POS)
        
        GPIO.output(self.UD_PIN, GPIO.LOW)
        while desired_pos < self.pos:
            GPIO.output(self.INC_PIN, GPIO.HIGH)
            sleep(time/2)
            GPIO.output(self.INC_PIN, GPIO.LOW)
            sleep(time/2)
            self.POS -= 1
            
    def set_to_digital(self, desired_pos):
        pwm = GPIO.PWM(self.INC_PIN, desired_pos)
        pwm.start(90)
        sleep(1)
        pwm.stop()
#        self.increase(desired_pos)
#        if desired_pos < self.POS:
#            self.decrease(desired_pos)
#        elif desired_pos > self.POS:
#            self.increase(desired_pos)

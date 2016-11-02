import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

freq = 100
my_pwm = GPIO.PWM(4, freq)

my_pwm.start(5)
while True:
    try:
        V = input('Please enter desired voltage: ')
        alpha = (V/3.15)*100
        if alpha > 100:
            alpha = 100
        my_pwm.ChangeDutyCycle(alpha)
    except KeyboardInterrupt:
        break
print('\n')
my_pwm.stop()

GPIO.cleanup()

import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def setup(pins):
    for item in pins:
        pin = pins[item]
        value = func[item]
        GPIO.setup(pin, value)
        

def chooser(pin, value):
    temp = GPIO.LOW
    if value:
        temp = GPIO.HIGH
    GPIO.output(pin, temp)
    

def primeraParte():
    potentiometer = 0#ADC.read_adc(0)/maximum*gain_voltage
    cell = 0#ADC.read_adc(3)/maximum*gain_voltage
    print('\033c')
    print('Cell: %.3fV, Potentiometer: %.3fV'%(cell, potentiometer))
    print('----------------------------------')
    if cell > potentiometer:
        GPIO.output(pins['LED'], GPIO.HIGH)
        print('         LED is ON')
    else:
        GPIO.output(pins['LED'], GPIO.LOW)
        print('         LED is OFF')


def segundaParte(A, B):        
    NOT = (not A)
    AND = A and B
    OR = A or B
    print('Entrada A:%r B:%r'%(A,B))
    print('Negado: %r'%NOT)
    print('AND: %r'%AND)
    print('OR: %r'%OR)

    values = {'NOT': NOT, 'AND': AND, 'OR': OR}
    for item in values:
        chooser(pins[item], values[item])

    
def terceraParte(A, B):
    C = (not A) and B
    D = (not B) and A
    Y = C or D
    values = {'C': C, 'D': D, 'Y': Y}
    for item in values:
        chooser(pins[item], values[item])

    print('C: %r, D: %r, V: %r'%(C,D,Y))
    
pins = {'LED': 17, 'LEFT': 27, 'RIGHT': 18, 'NOT': 5, 'AND': 6, 'OR': 12, 'C': 13,
        'D': 19, 'Y': 26}
func = {'LED': GPIO.OUT, 'LEFT': GPIO.IN, 'RIGHT': GPIO.IN, 'NOT': GPIO.OUT,
        'AND': GPIO.OUT, 'OR': GPIO.OUT, 'C': GPIO.OUT, 'D': GPIO.OUT, 'Y': GPIO.OUT}

setup(pins)

ADC = Adafruit_ADS1x15.ADS1115()

maximum = 32767.0
gain_voltage = 4.096


while True:
    try:
        A, B = GPIO.input(pins['LEFT']), GPIO.input(pins['RIGHT'])
        A, B = bool(A), bool(B)
        
        primeraParte()
        print('----------------------------------')
        segundaParte(A, B)
        print('----------------------------------')
        terceraParte(A, B)
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

GPIO.cleanup()

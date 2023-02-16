import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pin numbers for IR sensors
leftIR = 1
rightIR = 2

GPIO.setup(leftIR,GPIO.IN)
GPIO.setup(rightIR,GPIO.IN)

if():
    #stay forward

if():
    #turn right

if():
    #turn left

if():
    #stop

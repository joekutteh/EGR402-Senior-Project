import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pin numbers for IR sensors
leftIR = 1
rightIR = 2

GPIO.setup(leftIR,GPIO.IN)
GPIO.setup(rightIR,GPIO.IN)

#Both IR sensors see white surface
if(GPIO.input(leftIR)==True and GPIO.input(rightIR)==True):
    #stay forward

#Right IR sensor see black line, turn right
if(GPIO.input(leftIR)==True and GPIO.input(rightIR)==False):
    #turn right

#Left IR sensor see black line, turn left
if(GPIO.input(leftIR)==False and GPIO.input(rightIR)==True):
    #turn left

#Both IR sensors see black line
if(GPIO.input(leftIR)==False and GPIO.input(rightIR)==False):
    #stop



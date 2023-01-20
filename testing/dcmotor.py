import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
enable = 16
input1 = 20
input2 = 21
GPIO.setup(enable,GPIO.OUT)
GPIO.setup(input1,GPIO.OUT)
GPIO.setup(input2,GPIO.OUT)

# GPIO.output(enable,GPIO.HIGH)
enablePWM = GPIO.PWM(enable,50)
enablePWM.start(0)

GPIO.output(input1,GPIO.HIGH)
GPIO.output(input2,GPIO.LOW)

enablePWM.ChangeDutyCycle(50)

time.sleep(3)
enablePWM.ChangeDutyCycle(100)
time.sleep(3)
enablePWM.ChangeDutyCycle(0)

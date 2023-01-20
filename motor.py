import RPi.GPIO as GPIO
import time

motorPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPIN,GPIO.OUT)
motor = GPIO.PWM(motorPIN,50)
motor.start(0)
motor.ChangeDutyCycle(70)
time.sleep(2)
motor.stop()
GPIO.cleanup()
print('Done')
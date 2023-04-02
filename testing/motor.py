import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


motorPIN = 32
MOTOR3_input1 = 19
MOTOR3_input2 = 21

GPIO.setup(MOTOR3_input1,GPIO.OUT)
GPIO.setup(MOTOR3_input2,GPIO.OUT)
GPIO.setup(motorPIN,GPIO.OUT)


    
motor = GPIO.PWM(motorPIN,100)
motor.start(0)

GPIO.output(MOTOR3_input1,GPIO.HIGH)
GPIO.output(MOTOR3_input2,GPIO.LOW)


motor.ChangeDutyCycle(100)

GPIO.output(motorPIN,GPIO.HIGH)


time.sleep(2)

GPIO.output(motorPIN,GPIO.LOW)
motor.stop()
GPIO.cleanup()
print('Done')

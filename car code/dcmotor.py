#Imports
import RPi.GPIO as GPIO
import time
#import yolov5   

#Variables
#Enable pins can turn the motors on/off and control speed via PWM
enableFront = 7
enableRear = 11

#Input pins control direction of the motors
#If both inputs are LO the motor is off, both are HI and motor is off
#input1 is HI and input2 is LO motor is spinning forward
#input1 is LO and input2 is HI motor is spinning backward
MOTOR1_input1 = 13
MOTOR1_input2 = 15

MOTOR2_input1 = 29
MOTOR2_input2 = 31

MOTOR3_input1 = 19
MOTOR3_input2 = 21

MOTOR4_input1 = 33
MOTOR4_input2 = 35

#GPIO pin numbers for IR sensors
leftIR = 38
rightIR = 40

GPIO.setwarnings(False)

#This function control the speed of the DC motor. Speed must be between 0-100
def speed_control(targetPWM,speed):
    targetPWM.ChangeDutyCycle(speed)

#forward
def reverse(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.HIGH)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    
    GPIO.output(MOTOR2_input1,GPIO.HIGH)
    GPIO.output(MOTOR2_input2,GPIO.LOW)

    GPIO.output(MOTOR3_input1,GPIO.HIGH)
    GPIO.output(MOTOR3_input2,GPIO.LOW)

    GPIO.output(MOTOR4_input1,GPIO.HIGH)
    GPIO.output(MOTOR4_input2,GPIO.LOW)

#reverse 
def forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.HIGH)

    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.HIGH)

    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.HIGH)

#left
def left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR3_input1,GPIO.HIGH)
    GPIO.output(MOTOR3_input2,GPIO.LOW)
    
    GPIO.output(MOTOR4_input1,GPIO.HIGH)
    GPIO.output(MOTOR4_input2,GPIO.LOW)


#right
def right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):

    GPIO.output(MOTOR1_input1,GPIO.HIGH)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    
    GPIO.output(MOTOR2_input1,GPIO.HIGH)
    GPIO.output(MOTOR2_input2,GPIO.LOW)
    
    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.HIGH)
    

#stop
def off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.LOW)
    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.LOW)
    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.LOW)

#Setting how board GPIOs are numbered
GPIO.setmode(GPIO.BOARD)

#Setting GPIO to be input or output
GPIO.setup(enableFront,GPIO.OUT)
GPIO.setup(enableRear,GPIO.OUT)
GPIO.setup(MOTOR1_input1,GPIO.OUT)
GPIO.setup(MOTOR1_input2,GPIO.OUT)
GPIO.setup(MOTOR2_input1,GPIO.OUT)
GPIO.setup(MOTOR2_input2,GPIO.OUT)
GPIO.setup(MOTOR3_input1,GPIO.OUT)
GPIO.setup(MOTOR3_input2,GPIO.OUT)
GPIO.setup(MOTOR4_input1,GPIO.OUT)
GPIO.setup(MOTOR4_input2,GPIO.OUT)
GPIO.setup(leftIR,GPIO.IN)
GPIO.setup(rightIR,GPIO.IN)

#Initial State
off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

#Create PWM instance with frequency of 50 Hz
#Start PWM with a duty cycle of 0
#PWM_enableFront = GPIO.PWM(enableFront,50)
#PWM_enableRear = GPIO.PWM(enableRear,50)
#PWM_enableFront.start(0)
#PWM_enableRear.start(0)
GPIO.output(enableFront, GPIO.HIGH)
GPIO.output(enableRear, GPIO.HIGH)


#Both IR sensors see white surface
#if(GPIO.input(leftIR)==True and GPIO.input(rightIR)==True):
    #stay forward

#Right IR sensor see black line, turn right
#if(GPIO.input(leftIR)==True and GPIO.input(rightIR)==False):
    #turn right

#Left IR sensor see black line, turn left
#if(GPIO.input(leftIR)==False and GPIO.input(rightIR)==True):
    #turn left

#Both IR sensors see black line
#if(GPIO.input(leftIR)==False and GPIO.input(rightIR)==False):
    #stop

#if GPIO.input(leftIR) == 1:
#	print("left - black")
#else:
	#print("left - white")
	
#if GPIO.input(rightIR) == 1:
#	print("right - black")
#else:
#	print("right - white")
off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
time.sleep(30)
while(1):
	#both on white
	if GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 0:
		print("both white")
		forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
	elif GPIO.input(leftIR) == 1 and GPIO.input(rightIR) == 0:
		print("left black")
		left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(0.2)
	elif GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 1:
		right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(0.2)
		print("right black")
	#both on black
	elif GPIO.input(leftIR) == 1 and GPIO.input(rightIR) == 1:
		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		print("both black")

GPIO.cleanup()
print('Done')



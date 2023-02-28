#Imports
import RPi.GPIO as GPIO
import time

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

#GPIO pin for button
button = 32

#GPIO pin for status LED
led = 36

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

#Button pressed
def button_pressed(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
    GPIO.cleanup()
    exit

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
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

#Creating interrupt for button, when button is pressed car will shutdown
GPIO.add_event_detect(button,GPIO.FALLING,callback=button_pressed(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2),bouncetime=50)

#Initial State
#off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

#Create PWM instance with frequency of 50 Hz
#Start PWM with a duty cycle of 0
#PWM_enableFront = GPIO.PWM(enableFront,50)
#PWM_enableRear = GPIO.PWM(enableRear,50)
#PWM_enableFront.start(0)
#PWM_enableRear.start(0)

#Enabling motor controllers
GPIO.output(enableFront, GPIO.HIGH)
GPIO.output(enableRear, GPIO.HIGH)

#Initial state
off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
GPIO.output(led, GPIO.LOW)

#30 second delay to allow us to unplug ketboard, mouse, and display and put the car on the track
time.sleep(30)

#Turning on status led to let us know the program is about run
GPIO.output(led, GPIO.HIGH)

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



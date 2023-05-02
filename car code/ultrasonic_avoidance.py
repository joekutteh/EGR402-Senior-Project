#Imports
import RPi.GPIO as GPIO
import time
import serial

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

#GPIO pin for status LED
led = 36

#Disabiling warnings
GPIO.setwarnings(False)

#Reverse function for motors
def reverse(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.HIGH)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    
    GPIO.output(MOTOR2_input1,GPIO.HIGH)
    GPIO.output(MOTOR2_input2,GPIO.LOW)

    GPIO.output(MOTOR3_input1,GPIO.HIGH)
    GPIO.output(MOTOR3_input2,GPIO.LOW)

    GPIO.output(MOTOR4_input1,GPIO.HIGH)
    GPIO.output(MOTOR4_input2,GPIO.LOW)

#Forward function for motors
def forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.HIGH)

    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.HIGH)

    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.HIGH)

#Left function for motors
def left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR3_input1,GPIO.HIGH)
    GPIO.output(MOTOR3_input2,GPIO.LOW)
    
    GPIO.output(MOTOR4_input1,GPIO.HIGH)
    GPIO.output(MOTOR4_input2,GPIO.LOW)
    time.sleep(0.3)

#Right function for motors
def right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):

    GPIO.output(MOTOR1_input1,GPIO.HIGH)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    
    GPIO.output(MOTOR2_input1,GPIO.HIGH)
    GPIO.output(MOTOR2_input2,GPIO.LOW)
    
    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.HIGH)
    time.sleep(0.3)

#Off function for motors
def off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.LOW)
    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.LOW)
    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.LOW)
 
#This function reads UART data containing the 4 ultrasonic sensor distances
def readUS():
    while True:
        #If there is data to read, read it in
        if arduino.in_waiting > 0:

            #Reading in line of data
            data = arduino.readline().strip()
            try:
                #Return read in data
                return data                
            #When anything else is transfered besides a number	
            except ValueError:
                return -1

#Setting how board GPIOs are numbered
GPIO.setmode(GPIO.BOARD)

#Creating serial object
arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

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
GPIO.setup(led,GPIO.OUT)

#Enabling motor controllers
GPIO.output(enableFront, GPIO.HIGH)
GPIO.output(enableRear, GPIO.HIGH)

#Initial state - motors off and status LED off
off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
GPIO.output(led, GPIO.LOW)

#30 second delay to allow us to unplug ketboard, mouse, and display and put the car on the track
time.sleep(30)


#Main loop
while True:
	
	#Get ultrasonic data
	sensorData = readUS()
	
	#Parsing read in string
	frontSen = int(sensorData[0:2])
	leftSen = int(sensorData[2:4])
	rightSen = int(sensorData[4:6])
	backSen = int(sensorData[6:8])
	
    #If an object is present
	if(frontSen > 0):

		right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(0.6)
		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

		time.sleep(2)

		forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(1.2)
		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

		time.sleep(2)

		left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(1.1)
		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

		time.sleep(2)

        #Driving until a black line is detected
		while GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 0:
			print("white")
			forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
			
		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(2)

		reverse(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
		time.sleep(0.1)
        
        #Turning back on track
		while GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 0:
			right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

		off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

GPIO.cleanup()
print('Done')



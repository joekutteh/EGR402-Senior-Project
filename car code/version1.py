#Imports
import RPi.GPIO as GPIO
import time
import serial

#Creating serial object
arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

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

#GPIO pin for status LED
led = 36

#Disabiling warnings
GPIO.setwarnings(False)

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

def reverse(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.HIGH)
    GPIO.output(MOTOR1_input2,GPIO.LOW)
    
    GPIO.output(MOTOR2_input1,GPIO.HIGH)
    GPIO.output(MOTOR2_input2,GPIO.LOW)

    GPIO.output(MOTOR3_input1,GPIO.HIGH)
    GPIO.output(MOTOR3_input2,GPIO.LOW)

    GPIO.output(MOTOR4_input1,GPIO.HIGH)
    GPIO.output(MOTOR4_input2,GPIO.LOW)

def forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2):
    GPIO.output(MOTOR1_input1,GPIO.LOW)
    GPIO.output(MOTOR1_input2,GPIO.HIGH)
    
    GPIO.output(MOTOR2_input1,GPIO.LOW)
    GPIO.output(MOTOR2_input2,GPIO.HIGH)

    GPIO.output(MOTOR3_input1,GPIO.LOW)
    GPIO.output(MOTOR3_input2,GPIO.HIGH)

    GPIO.output(MOTOR4_input1,GPIO.LOW)
    GPIO.output(MOTOR4_input2,GPIO.HIGH)

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
GPIO.setup(led,GPIO.OUT)

#Enabling motor controllers
GPIO.output(enableFront, GPIO.HIGH)
GPIO.output(enableRear, GPIO.HIGH)

#Initial state - motors off and status LED off
off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
GPIO.output(led, GPIO.LOW)

#30 second delay to allow us to unplug ketboard, mouse, and display and put the car on the track
time.sleep(30)

#Turning on status led to let us know the program is about run
GPIO.output(led, GPIO.HIGH)

#Main loop
while(True):

    #Get ultrasonic data
    sensorData = readUS()

    #Just in case the read failed we'll do it again
    while(int(sensorData) < 0):
        printf("failed")
        sensorData = readUS()

    #Parsing read in string
    front = int(sensorData[0:2])
    left = int(sensorData[2:4])
    right = int(sensorData[4:6])
    back = int(sensorData[6:8])

    #Debuging
    print(sensorData)
    print(front)
    print(left)
    print(right)
    print(back)

    #This code navigates when there is an object in front of the car
    #If object is within 20 cm
    if(front > 0):
        off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
        print("OBJECT WITHIN 20 CM TESTING")
        #Now check is we should turn left or right
        if(left == 0):
            print("TURNING LEFT")
            #No object on left, clear to turn left x seconds to make 90 degree turn
            left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            time.sleep(0.2)
            off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            while(True):
                #move foward
                forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                #Get new data
                sensorData = readUS()
                right = int(sensorData[4:6])
                if(right == 0):
                    break

            #No object on right, clear to turn right x seconds to make 90 degree turn
            right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            time.sleep(0.2)
            off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            while(True):
                #move foward
                forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                #Get new data
                sensorData = readUS()
                right = int(sensorData[4:6])
                if(right == 0):
                    break
            
            #No object on right, clear to turn right x seconds to make 90 degree turn
            right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            time.sleep(0.2)
            off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            while(True):
                #move foward
                forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                #Get new data
                sensorData = readUS()
                right = int(sensorData[4:6])
                if(right != 0):
                    #Back on track, clear to turn left x seconds to make 90 degree turn and continue tracking line
                    left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                    time.sleep(0.2)
                    off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                    break

        elif(right == 0):
            off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
            print("OBJECT WITHIN 20 CM TESTING")
            #Now check is we should turn left or right
            if(right == 0):
                print("TURNING RIGHT")
                #No object on right, clear to turn right x seconds to make 90 degree turn
                right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                time.sleep(0.2)
                off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                while(True):
                    #move foward
                    forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                    #Get new data
                    sensorData = readUS()
                    left = int(sensorData[2:4])
                    if(left == 0):
                        break

                #No object on left, clear to turn left x seconds to make 90 degree turn
                left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                time.sleep(0.2)
                off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                while(True):
                    #move foward
                    forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                    #Get new data
                    sensorData = readUS()
                    left = int(sensorData[2:4])
                    if(left == 0):
                        break
                
                #No object on left, clear to turn left x seconds to make 90 degree turn
                left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                time.sleep(0.2)
                off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                while(True):
                    #move foward
                    forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                    #Get new data
                    sensorData = readUS()
                    left = int(sensorData[2:4])
                    if(left != 0):
                        #Back on track, clear to turn right x seconds to make 90 degree turn and continue tracking line
                        right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                        time.sleep(0.2)
                        off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
                        break

        else:
            #Objects on both sides so STOP, this wont happen 
            print("blocked")
            
    else:
        #Nothing in the way so continue to track line
        print("nothing in the way")
        if GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 0:
            forward(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
        elif GPIO.input(leftIR) == 1 and GPIO.input(rightIR) == 0:
            left(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
        elif GPIO.input(leftIR) == 0 and GPIO.input(rightIR) == 1:
            right(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)
        elif GPIO.input(leftIR) == 1 and GPIO.input(rightIR) == 1:
            off(MOTOR1_input1,MOTOR1_input2,MOTOR2_input1,MOTOR2_input2,MOTOR3_input1,MOTOR3_input2,MOTOR4_input1,MOTOR4_input2)

    GPIO.cleanup()
    print('Done')
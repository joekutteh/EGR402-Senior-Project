import serial
import time

#Creates serial object for Arduino at a baud rate of 9600
#It is imortant that baud rates are equal or data transmission cannot occur
arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

def readUSsensor():
    #Loop to poll recieved data
    while True:
        if arduino.in_waiting > 0:

            #Reading in line of datas
            data = arduino.readline().strip()
            try:
                #Casting it to an integer and printing
                
                num = int(data)
                print(num) #this is 3 digit
                #print("Sensor #" + str(num)[0] + " distance")
                print(num % (int(str(num)[0])*100)) #this is distance
                
            #When anything else is transfered besides a number	
            except ValueError:
                print("error")

	
				
while True:

    #check for obstacle
    readUSsensor() 
    if()

    #Yolo stuff

    #IR sensor code, done

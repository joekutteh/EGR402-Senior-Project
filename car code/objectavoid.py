import serial
import time

arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

def readUS():
    while True:
        if arduino.in_waiting > 0:

            #Reading in line of datas
            data = arduino.readline().strip()
            try:
                return data                
            #When anything else is transfered besides a number	
            except ValueError:
                return -1

sensorData = readUS()

#Just in case the read failed we'll do it again
while(int(sensorData) < 0):
    printf("failed")
    sensorData = readUS()

front = int(sensorData[0:2])
left = int(sensorData[2:4])
right = int(sensorData[4:6])
back = int(sensorData[6:8])

print(sensorData)
print(front)
print(left)
print(right)
print(back)

#If object is within 20 cm
if(front > 0):
    print("OBJECT WITHIN 20 CM TESTING")
    #Now check is we should turn left or right
    if(left == 0):
        print("TURNING LEFT")
        #No object on left, clear to turn left x seconds to make 90 degree turn
        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            right = int(sensorData[4:6])
            if(right == 0):
                break

        #No object on right, clear to turn right x seconds to make 90 degree turn
        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            right = int(sensorData[4:6])
            if(right == 0):
                break
        

        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            right = int(sensorData[4:6])
            if(right == 0):
                #Back on track, clear to turn left x seconds to make 90 degree turn and continue tracking line
                break

    elif(right == 0):
        print("TURNING RIGHT")
        #Object on left but no object on right, clear to turn right
        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            left = int(sensorData[4:6])
            if(left == 0):
                break

        #No object on right, clear to turn right x seconds to make 90 degree turn
        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            left = int(sensorData[4:6])
            if(left == 0):
                break
            

        while(True):
            #move foward
            #Get new data
            sensorData = readUS()
            left = int(sensorData[4:6])
            if(left == 0):
                #Back on track, clear to turn left x seconds to make 90 degree turn and continue tracking line
                break

    else:
        #Objects on both sides so STOP, this wont happen 
        print("blocked")
        
else:
    print("nothing in the way")



import serial
import time

#Creates serial object for Arduino at a baud rate of 9600 
arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

#Loop to read in data whenever it is avaliable
while True:
	if arduino.in_waiting > 0:

		#Reading in line of data
		data = arduino.readline().strip()
		try:
			#Casting it to an integer and printing
			num = int(data)
			print(num)
			
		#When anything else is transfered besides a number	
		except ValueError:
			print("error")

	
	
				

		

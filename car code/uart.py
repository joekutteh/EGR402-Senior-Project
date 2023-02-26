import serial
import time


arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)



while True:
	if arduino.in_waiting > 0:
		data = arduino.readline().strip()
		try:
			num = int(data)
			print(num)
			
		except ValueError:
			print("error")


	#print("no data yet")
	
	
				

		

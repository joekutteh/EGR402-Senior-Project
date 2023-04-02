import serial
import signal

arduino = serial.Serial('/dev/ttyTHS1',9600,timeout=1)

def handle_serial_input():
	#Reading in line of datas
	data = arduino.readline().strip()
	try:
		#Casting it to an integer and printing
		num = int(data)
		print(num)
			
	#When anything else is transfered besides a number	
	except ValueError:
		print("error")
		
import threading
threading.Thread(target=handle_serial_input,daemon=True).start()

while True:
	print("Waiting")
	

import RPi.GPIO as GPIO
import time

buttonPIN = 32
GPIO.setmode(GPIO.BOARD)

def button_callback(channel):
    print("pressed")

GPIO.setup(buttonPIN,GPIO.IN)
GPIO.add_event_detect(buttonPIN,GPIO.FALLING,callback=button_callback, bouncetime=10)

try:
	while True:
    		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

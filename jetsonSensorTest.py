import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG_1 = 16
ECHO_1 = 17


GPIO.setup(TRIG_1,GPIO.OUT)
GPIO.setup(ECHO_1,GPIO.IN)


while True:
    #US 1
    print("Starting")
    GPIO.output(TRIG_1,False)
    time.sleep(2)

    GPIO.output(TRIG_1,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_1,False)

    while GPIO.input(ECHO_1)==0:
        pulse_start_1 = time.time()
      
    while GPIO.input(ECHO_1)==1:
        pulse_end_1 = time.time()
        
    print("Working")
    pulse_duration_1 = pulse_end_1 - pulse_start_1

    distance_1 = pulse_duration_1 * 17150
    distance_1 = round(distance_1,2)

    if(distance_1 <= 30): print("Sensor 1 ",distance_1,"cm")
    

GPIO.cleanup()
    
    


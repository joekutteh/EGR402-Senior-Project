import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG_1 = 216
ECHO_1 = 50

TRIG_2 = 14
ECHO_2 = 194

TRIG_3 = 16
ECHO_3 = 17


GPIO.setup(TRIG_1,GPIO.OUT)
GPIO.setup(ECHO_1,GPIO.IN)

GPIO.setup(TRIG_2,GPIO.OUT)
GPIO.setup(ECHO_2,GPIO.IN)

GPIO.setup(TRIG_3,GPIO.OUT)
GPIO.setup(ECHO_3,GPIO.IN)


while True:
    #US 1
    GPIO.output(TRIG_1,False)
    time.sleep(2)

    GPIO.output(TRIG_1,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_1,False)

    while GPIO.input(ECHO_1)==0:
        pulse_start_1 = time.time()
      
    while GPIO.input(ECHO_1)==1:
        pulse_end_1 = time.time()
        
        
    pulse_duration_1 = pulse_end_1 - pulse_start_1

    distance_1 = pulse_duration_1 * 17150
    distance_1 = round(distance_1,2)

    if(distance_1 <= 30): print("Sensor 1 ",distance_1,"cm")
    
    #-------------------------------------------------------------#
    
    #US 2
    GPIO.output(TRIG_2,False)
    time.sleep(2)

    GPIO.output(TRIG_2,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_2,False)

    while GPIO.input(ECHO_2)==0:
        pulse_start_2 = time.time()
      
    while GPIO.input(ECHO_2)==1:
        pulse_end_2 = time.time()
        
        
    pulse_duration_2 = pulse_end_2 - pulse_start_2

    distance_2 = pulse_duration_2 * 17150
    distance_2 = round(distance_2,2)

    if(distance_2 <= 30): print("Sensor 2 ",distance_2,"cm")
    
    #-------------------------------------------------------------#
    
    #US 3
    GPIO.output(TRIG_3,False)
    time.sleep(2)

    GPIO.output(TRIG_3,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_3,False)

    while GPIO.input(ECHO_3)==0:
        pulse_start_3 = time.time()
      
    while GPIO.input(ECHO_3)==1:
        pulse_end_3 = time.time()
        
        
    pulse_duration_3 = pulse_end_3 - pulse_start_3

    distance_3 = pulse_duration_3 * 17150
    distance_3 = round(distance_3,2)

    if(distance_3 <= 30): print("Sensor 3 ",distance_3,"cm")
    
GPIO.cleanup()
    
    


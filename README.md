# EGR402-Senior-Project

Senior Project in Engineering (EGR402) at Elizabethtown College

Students: Joe Kutteh, Nathan Griffin 

Advisor: Dr. Li

Introduction:
- Artificial intelligence and computer vision are become more used than ever before. Self-driving cars rely on computer vision and AI to allow the computer to make decisions. Self-driving cars use cameras, radar, lidar, ultrasonic sensors, and GPS. The car we plan to build will utilize cameras, ultrasonic sensors, and infrared sensors. We want to create an autonomous car just on a much smaller scale. The reason for perusing this project is to learn more about AI, computer vision, linux based SBCs, and Python. The goal is to have this project fully completed by April 2023.

Circuit overview:
- Our car will consist of multiple circuits; they will be explained here. One circuit will power 2 L293D motor controllers, 4 DC motors, and 2 infrared sensors. The IR sensors are connected to a GPIO pin on the NVIDIA Jetson Nano. The IR sensors will be used to detect a black line on a white surface. These 2 IR sensors will make up the line tracking system on the car. Next, the L293D motor controller and 4 DC motors will be on the same breadboard running on 5V. The L293D motor controller are half H-bridge chips. This means each L293D can only control 2 motors. The L293D will be used to control speed and direction of each motor. Each motor is connected to two GPIO pins. Speed of the motors will be controlled via PWM. The L293D’s will be wired to the 5V output pin on the Jetson Nano. The 4 DC motors will be connected to an external battery pack consisting of 4 AA batteries for a total of 6V.

- The next circuit will take distance measurements from the ultrasonic sensors. This circuit will run on 5V supplied from the Arduino. Our car will have an ultrasonic sensor on each side. The sensors will send their data to the NVIDIA Jetson Nano. It is not recommended to use ultrasonic sensors to take measurements on the Jetson Nano. The ultrasonic sensors need a pulse input to begin taking measurements which the Jetson Nano can’t supply. Due to this we decided to use an Arduino Nano to power our object distance system. Currently, the data will only be sent to the Arduino when the distance is under 30cm. Data will be sent to the Jetson Nano via UART, I2C may be considered as well.

Hardware list:
- Seeed Studio reComputer J1020 (Nvidia Jetson Nano 4GB)
- Arduino Nano
- DC motors and wheels
- L293D motor controllers
- Infrared sensors
- HC-SR04 ultrasonic sensors
- DC to DC voltage regulator
- AA battery pack
- 11.1V 5200 mAh RC car battery

CAD:

<img width="362" alt="image" src="https://user-images.githubusercontent.com/112097864/221240351-55a34382-772d-492a-a540-6bccaf650c7c.png">

<img width="346" alt="image" src="https://user-images.githubusercontent.com/112097864/221240429-df82163e-abb6-490f-b8e6-f355b0086d81.png">

Code overview:
- Code for this project is still in development. The main systems for our car are object detection and line tracking. Object detection will use the 4 ultrasonic sensors and a camera which will be plugged into the NVIDIA Jetson Nano. OpenCV and YOLOv5 are going to be used to accomplish object detection via the camera. Our model will be trained on a traffic specific data set. The camera will detect cars, traffic signs, and other obstacles in the road. Once the camera detects an object, we will get the distance between the car and object using ultrasonic sensors. The ultrasonic sensors will be continuously gathering data on the Arduino Nano.

	The line tracking system will be designed using the IR sensors. Two IR sensors will be needed to detect each side of the black line. Based on input from the IR sensors we will change the cars direction and speed. Motor direction and speed will be controlled using the L293D chips above. Refer below to a basic flowchart of our code. All our code can be found in this GitHub repository.




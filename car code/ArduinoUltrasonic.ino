//Trig is yellow
//Echo is white

//Front
int echoF = 9;
int trigF = 10;

//Left
int echoL = 11;
int trigL = 12;

//Back
int echoB = 7;
int trigB = 8;

//Right
int echoR = 5;
int trigR = 6;

//Variables
String returnString, front, left, right, back;


//Pin and serial config 
void setup() {
  pinMode(trigF, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoF, INPUT); // Sets the echoPin as an Input
  
  pinMode(trigR, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoR, INPUT); // Sets the echoPin as an Input

  pinMode(trigB, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoB, INPUT); // Sets the echoPin as an Input

  pinMode(trigL, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoL, INPUT); // Sets the echoPin as an Input

  Serial.begin(9600); // Starts the serial communication @ baud rate of 9600 
}

void loop() {
  
  //Get distance in cm from all sensors
  front = distance(echoF,trigF);
  left = distance(echoL,trigL);
  right = distance(echoR,trigR);
  back = distance(echoB,trigB);

  //Assemble all measurments into a string and send it to Jetson Nano
  Serial.println(String(front)+String(left)+String(right)+String(back));

  //Pause between measurments sent to Jetson Nano
  delay(5000); 
}

//This function will get the distance in cm from the specified ultrasonic sensor
String distance(int echo, int trig) {

  //Variables
  long duration;
  long distance;
  
  //Init trig pin and sending pulse 
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo, HIGH);

  // Calculating the distance in cm
  distance = duration * 0.034 / 2;

  //If distance is between 20 and 10cm we return the number
  if(distance < 20 && distance >= 10) {
    return String(distance);

    /* If distance is greater than 0 and less than 10 we 
    add a zero "0" to the front to ensure every measurment is 2 digits long 
    5 -> 05 */
  } else if(distance > 0 && distance < 10) {
    return "0" + String(distance);

    //If measurment is not greater than 0  and less than 20 then return "00"
  } else {
    return "00";
  }

}

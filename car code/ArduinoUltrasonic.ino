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


void setup() {
  //Configuring I/O
  pinMode(trigF, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoF, INPUT); // Sets the echoPin as an Input
  
  pinMode(trigR, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoR, INPUT); // Sets the echoPin as an Input

  pinMode(trigB, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoB, INPUT); // Sets the echoPin as an Input

  pinMode(trigL, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoL, INPUT); // Sets the echoPin as an Input

  //Setting baud rate to 9600. Starts the serial communication
  Serial.begin(9600); 
}

void loop() {
  //Loop to get distance from each sensor
  //The thrid argument is an identification for each sensor
  distance(echoF,trigF,100);
  distance(echoL,trigL,200);
  distance(echoR,trigR,300);
  distance(echoB,trigB,400);

}

void distance(int echo, int trig, int num) {
  //Variables
  long duration;
  long distance;

  //Sending trigger pulse to send wave. This is what the Jetson nano could not do
  //Setting trig low for 2 ms
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  //Setting trig to high for 10 ms
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);

  //Setting back to low
  digitalWrite(trig, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo, HIGH);

  //Calculating distance in cm
  distance = duration * 0.034 / 2;

  //Sends distance to Jetson Nano
  if(distance <= 30 and distance > 0){

    //The num allows us to determine which sensor the data is coming from
    Serial.println(distance+num);

    //Wait 100ms before reading data from next sensor
    delay(100);
  }
}

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
  // put your setup code here, to run once:
  pinMode(trigF, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoF, INPUT); // Sets the echoPin as an Input
  
  pinMode(trigR, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoR, INPUT); // Sets the echoPin as an Input

  pinMode(trigB, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoB, INPUT); // Sets the echoPin as an Input

  pinMode(trigL, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoL, INPUT); // Sets the echoPin as an Input

  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  distance(echoF,trigF,100);
  distance(echoL,trigL,200);
  distance(echoR,trigR,300);
  distance(echoB,trigB,400);

}

void distance(int echo, int trig, int num) {
  long duration;
  long distance;
  // put your main code here, to run repeatedly:
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  if(distance <= 30 and distance > 0){
    Serial.println(distance+num);
    delay(100);
  }
}

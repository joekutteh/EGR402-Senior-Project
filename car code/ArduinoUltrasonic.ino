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

String returnString, front, left, right, back;


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
  front = distance(echoF,trigF);
  left = distance(echoL,trigL);
  right = distance(echoR,trigR);
  back = distance(echoB,trigB);
  //Serial.println(String(front));
  //Serial.println(String(left));
  //Serial.println(String(right));
  //Serial.println(String(back));
  Serial.println(String(front)+String(left)+String(right)+String(back));



  delay(5000); 
}

String distance(int echo, int trig) {
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

  if(distance < 20 && distance >= 10) {
    return String(distance);
  } else if(distance > 0 && distance < 10) {
    return "0" + String(distance);
  } else {
    return "00";
  }

}

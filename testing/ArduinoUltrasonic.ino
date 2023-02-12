int echo = 2;
int trig = 3;

int echo2 = 4;
int trig2 = 5;

int echo3 = 6;
int trig3 = 7;

int echo4 = 8;
int trig4 = 9;


void setup() {
  // put your setup code here, to run once:
  pinMode(trig, OUTPUT); // Sets the trigPin as an Output
  pinMode(echo, INPUT); // Sets the echoPin as an Input
  
  pinMode(trig2, OUTPUT); // Sets the trigPin as an Output
  pinMode(echo2, INPUT); // Sets the echoPin as an Input

  pinMode(trig3, OUTPUT); // Sets the trigPin as an Output
  pinMode(echo3, INPUT); // Sets the echoPin as an Input

  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  distance(echo,trig,1);
  distance(echo2,trig2,2);
  distance(echo3,trig3,3);
  distance(echo4,trig4,4);

}

void distance(int echo, int trig, int num) {
  long duration;
  int distance;
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
  if(distance<=30) {
    Serial.write(distance);
    delay(1000);
  }
}

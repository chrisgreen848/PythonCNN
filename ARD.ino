// ---------------------------------------------------------------- //
// Arduino Ultrasoninc Sensor HC-SR04
// Re-writed by Arbi Abdul Jabbaar
// Using Arduino IDE 1.8.7
// Using HC-SR04 Module
// Tested on 17 September 2019
// ---------------------------------------------------------------- //


//Defining Motor A & B output pins


//Defining other variables
int ToggleMode = 0;

#define echoPin 12 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 13 //attach pin D3 Arduino to pin Trig of HC-SR04
#define echoPinA 2
#define trigPinA 3
#define echoPinB 45
#define trigPinB 46
#define motA 5
#define motB 6
#define motC 7
#define motD 8

// defines variables
long duration, durationA, durationB; // variable for the duration of sound wave travel
int distance, distanceA, distanceB; // variable for the distance measurement

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  pinMode(trigPinA, OUTPUT);
  pinMode(echoPinA, INPUT);
  pinMode(trigPinB, OUTPUT);
  pinMode(echoPinB, INPUT);
  pinMode(motA, OUTPUT);
  pinMode(motB, OUTPUT);
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor
  Serial.println("with Arduino UNO R3");
}
void loop() {
  // Clears the trigPin condition
 Serial.println("programme has started");
 
  digitalWrite(trigPin, LOW);
  delayMicroseconds (2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  distanceA = durationA * 0.034 / 2;
  distanceB= durationB * 0.034 / 2;
  // Displays the distance on the Serial Monitor
 
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  
  digitalWrite(trigPinA, LOW);
  delayMicroseconds (2);
  digitalWrite(trigPinA, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinA, LOW);
  delayMicroseconds(15);
  durationA = pulseIn(echoPinA, HIGH);
  Serial.print("DistanceA is : ");
  Serial.print(distanceA);
  Serial.println(" cm");

  delayMicroseconds(15);
    
  digitalWrite(trigPinB, LOW);
  delayMicroseconds (2);
  digitalWrite(trigPinB, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinB, LOW);
  delayMicroseconds(15);
  durationB = pulseIn(echoPinB, HIGH);

  Serial.print("DistanceB is : ");
  Serial.print(distanceB);
  Serial.println(" cm");

  //delayMicroseconds(10000);

  digitalWrite(motA, HIGH);
  digitalWrite(motB, LOW);
  analogWrite(11,255);


  digitalWrite(motC, HIGH);
  digitalWrite(motD,LOW);
  analogWrite(3,255);
  

  

  
}

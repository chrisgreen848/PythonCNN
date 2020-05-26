// Move Pin 2&3 to Pin 19&18 on Motorboard (Rx1 and Tx1 MB)(DONE)
// Move Pin 12&13 to Digi Pin 16&17 (Rx2 and Tx 2)(DONE)
// Code Change Pin (Dir A) to Pin 12 (DONE)
// Code Change Pin (Dir B) to Pin 13 (DONE)
// Pin 8 (mot D) fine (Brake A)
// Pin 7 (mot C) Code change to Pin 13 (Dir B) (DONE)
// Pin 6 (mot B) Code Change to Pin 9 (Brake B)(DONE)
// Pin 5 (mot A) Code Change to Pin 12 (Dir A)(DONE)
// Pin 11 (PWM A) Bridged to Pin 3 (PWM B)
// Pin 45 and 46 OKAY

// TRIAL CODE BELOW

//Defining Motor A & B output pins

//Defining other variables
int ToggleMode = 0;

#define echoPin 16 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 17 //attach pin D3 Arduino to pin Trig of HC-SR04
#define echoPinA 19
#define trigPinA 18
#define echoPinB 45
#define trigPinB 46
#define motA 12
#define motB 9
#define motC 13
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
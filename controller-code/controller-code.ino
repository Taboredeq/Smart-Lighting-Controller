// Smart Ambient Light System
// Controls LED brightness based on motion detection and ambient light level

const int GREEN_PIN = 5;
const int RED_PIN   = 6;
const int MOTION_SENSOR_PIN = 7;
const int PHOTORESISTOR_PIN = A7;

// System state variables
bool systemOn = false;
bool motionDetected = false;
bool isBrightEnvironment = false;

int lightLevel = 0;

// Function to gradually turn LEDs ON
void turnOn() {
  systemOn = true;

  // Fade in red LED
  for (int r = 0; r <= 255; r++) {
    analogWrite(RED_PIN, r);
    delay(5);
  }

  // Subtle green accent fade
  for (int g = 0; g <= 10; g++) {
    analogWrite(GREEN_PIN, g);
    delay(100);
  }
}

// Function to gradually turn LEDs OFF
void turnOff() {
  systemOn = false;

  for (int r = 255; r >= 0; r--) {
    analogWrite(RED_PIN, r);
    analogWrite(GREEN_PIN, r / 16);  // Maintain color ratio
    delay(5);
  }
}

void setup() {
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(MOTION_SENSOR_PIN, INPUT);
}

void loop() {

  motionDetected = digitalRead(MOTION_SENSOR_PIN);
  lightLevel = analogRead(PHOTORESISTOR_PIN);

  // Adaptive light threshold
  if (systemOn) {
    isBrightEnvironment = (lightLevel > 200);
  } else {
    isBrightEnvironment = (lightLevel > 100);
  }

  // Turn ON when motion detected in dark
  if (motionDetected && !isBrightEnvironment && !systemOn) {
    turnOn();
  }

  // Turn OFF when no motion or environment becomes bright
  if ((!motionDetected || isBrightEnvironment) && systemOn) {
    turnOff();
  }
}












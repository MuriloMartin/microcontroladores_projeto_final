#define TREBLE 31
#define INTENSITY 32
#define BASS 6

void setBassIntensity(int level) {
  analogWrite(BASS, level);
}

void setup() {
  Serial.begin(9600);
  pinMode(INTENSITY, OUTPUT);
  pinMode(TREBLE, OUTPUT);
  pinMode(BASS, OUTPUT);
  digitalWrite(TREBLE, LOW);
  analogWrite(BASS, 255); // Start with bass at full intensity
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "on") {
      digitalWrite(TREBLE, HIGH);
    } else if (command == "off") {
      digitalWrite(TREBLE, LOW);
    } else if (command == "up") {
      digitalWrite(INTENSITY, LOW);
    } else if (command == "down") {
      digitalWrite(INTENSITY, HIGH);
    } else if (command.startsWith("bass ")) {
      String value = command.substring(5); // Extract intensity value
      int intensity = value.toInt(); // Convert to integer
      intensity = constrain(intensity, 0, 255); // Ensure value is between 0-255
      setBassIntensity(intensity);
    }
  }
}

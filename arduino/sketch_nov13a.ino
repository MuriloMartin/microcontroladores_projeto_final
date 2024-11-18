#define TREBLE 31
#define INTENSITY 32
#define BASS 6

void bass(){
  digitalWrite(BASS,LOW);
  delay(100);
  digitalWrite(BASS,HIGH);
}

/*
void testaBaixo(){
    bass();
    delay(100);
    bass();
    delay(50);
    bass();
}*/


void setup() {
  Serial.begin(9600);
  pinMode(INTENSITY, OUTPUT);
  pinMode(TREBLE, OUTPUT);
  pinMode(BASS, OUTPUT);
  digitalWrite(TREBLE, LOW);
  digitalWrite(BASS, HIGH);
  //testaBaixo();
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    //Serial.println(command);
    if(command=="on") digitalWrite(TREBLE, HIGH);
    else if(command=="off") digitalWrite(TREBLE, LOW);
    else if(command=="up") digitalWrite(INTENSITY,LOW);
    else if(command=="down") digitalWrite(INTENSITY, HIGH);
    else if(command=="bass") bass();
    else if(command=="bass on") digitalWrite(BASS,LOW);
    else if(command=="bass off") digitalWrite(BASS,HIGH);
  }
}
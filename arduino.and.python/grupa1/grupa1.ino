#define LED_PORT 3

char on = '0';
 
void setup() {
  // put your setup code here, to run once:
 
  pinMode(LED_PORT, OUTPUT);
  digitalWrite(LED_PORT, HIGH);
  Serial.begin(9600);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0) {
      String input = Serial.readString();
      input.trim();
      if (input == "on") {
          on = '1';
          digitalWrite(LED_PORT, LOW);}
      else if (input == "off") {
          on = '0';
          digitalWrite(LED_PORT, HIGH);
        }
      else{
          Serial.write(on);
        }
    
  }
}

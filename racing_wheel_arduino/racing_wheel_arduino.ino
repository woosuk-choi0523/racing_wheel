void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
}

void loop() {
  float handle = analogRead(A0);
  int accelerate = digitalRead(8);
  int breakbtn = digitalRead(9);
  String var = String(handle) + " " + String(accelerate) + " " + String(breakbtn);
  Serial.println(var);

}

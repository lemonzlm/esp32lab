#include <Arduino.h>

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  int ledPin = 2;
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  // Serial.println("hello world");
  // delay(1000);
  int ledPin = 2;
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
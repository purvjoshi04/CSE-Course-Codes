### **_Practical-5_**

<hr>

**_Description_**

#### In this practical i have create circuit using arduino which display the distance of the object on the LCD screen using ultrasonic distance sensor.

<hr>

**_Circuit Diagram_**

![Screenshot (31)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/f291641e-c73f-4d41-a283-bff2f6c9b0f9)

<hr>

**_Arduino Code_**

```cpp

#include <LiquidCrystal.h>

LiquidCrystal lcd(1, 2, 4, 5, 6, 7);
const int trigPin = 9;
const int echoPin = 10;
long duration;
int distanceCm, distanceInch;

void setup() {
    lcd.begin(16,2);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}
void loop() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distanceCm= duration*0.034/2;
    distanceInch = duration*0.0133/2;

    lcd.setCursor(0,0);
    lcd.print("Distance: ");
    lcd.print(distanceCm);
    lcd.print(" cm");
    delay(10);

    lcd.setCursor(0,1);
    lcd.print("Distance: ");
    lcd.print(distanceInch);
    lcd.print(" inch");
    delay(10);
}

```

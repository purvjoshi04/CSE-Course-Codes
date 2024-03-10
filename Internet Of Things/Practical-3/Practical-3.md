### ***Practical-3***

<hr>

***Description***
#### In this practical i have create circuit using arduino which check the temperature and humidity using TMP36 sensor, the threshold humidity is 70 if humidity goes to 70 or above the LED light will blink

<hr>

***Circuit Diagram***

![Screenshot (18)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/cc40fadd-e98f-4cf1-a0a2-f5dea5839304)

<hr>

***Arduino Code***

```cpp

const int tmpPin = A0;  
const int ledPin = 13;  

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  int tmpValue = analogRead(tmpPin);
  

  float voltage = tmpValue * (5.0 / 1023.0);

  float temperatureC = (voltage - 0.5) * 100.0;
  

  int humidity = map(temperatureC, 0, 40, 0, 100);

  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.print("°C");
  Serial.print("\tHumidity: ");
  Serial.print(humidity);
  Serial.println("%");
  
  if (humidity >= 70) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  } else {
    digitalWrite(ledPin, LOW);
  }
  
  delay(1000); 
}

```  

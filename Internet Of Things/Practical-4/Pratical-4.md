### ***Practical-4***

<hr>

***Description***
#### In this practical i have create circuit using arduino which check the temperature and humidity if humidity goes on threshold value or above threshold value the LED light will start blinking.

<hr>

***Circuit Diagram***

![Screenshot (19)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/5b69dd2d-32fc-46d9-b3ca-a4c0f1f4d003)

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
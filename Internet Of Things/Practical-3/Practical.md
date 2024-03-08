### ***Practical-3***

<hr>

#### In this practical i have create circuit using arduino which check the temperature and humidity using TMP36 sensor, the threshold humidity is 70 if humidity goes to 70 or above the LED light will blink

***Circuit Diagram***

![Screenshot (17)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/23f0ed0e-8664-4443-bb95-dd451756b14c)

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

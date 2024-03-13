### ***Practical-3***

<hr>

***Description***
#### In this practical i have create circuit using arduino which check the temperature and humidity using TMP36 sensor and potentiometer.

<hr>

***Circuit Diagram***

![Screenshot (24)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/5cd52b9d-fb69-45a6-a3db-46a44be2943a)

<hr>

***Arduino Code***

```cpp

const int analogin = A0;
int humiditySensorOutput = 0;
int RawValue = 0;
double Voltage = 0;
double tempC = 0;
double tempF = 0;

void setup() {
  Serial.begin(9600);
  pinMode(A1, INPUT);
}

void loop() {
  RawValue = analogRead(analogin);
  Voltage = (RawValue / 1023.0) * 5000;
  tempC = (Voltage - 500) * 0.1; 
  tempF = (tempC * 1.8) + 32; 

  Serial.print("Raw Value = ");
  Serial.print(RawValue);
  Serial.print("\t milli volts = ");
  Serial.print(Voltage, 0);
  Serial.print("\t Temperature in C =");
  Serial.print(tempC, 1);
  Serial.print("\t Temperature in F =");
  Serial.println(tempF, 1);

  humiditySensorOutput = analogRead(A1);

  Serial.print("Humidity: "); 
  Serial.print(map(humiditySensorOutput, 0, 1023, 10, 70));
  Serial.println("%");

  delay(1000); 
}


```  

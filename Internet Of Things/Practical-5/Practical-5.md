### ***Practical-5***

<hr>

***Description***
#### In this practical i have create circuit using arduino which display the temperature on the LCD screen using TMP36 sensor.

<hr>

***Circuit Diagram***

![Screenshot (28)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/c2569892-499d-4c34-89ce-0d1382a8857f)

<hr>

***Arduino Code***

```cpp

#include<LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; 
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); 

float celsius;
int temp = A1;


void setup(){
	pinMode(temp,INPUT);
}


void loop(){
	celsius = analogRead(temp)*0.004882814;
  	celsius = (celsius - 0.5) * 100.0;
  	
  	lcd.setCursor(0,1);
	lcd.print("Temp: ");
  	lcd.print(celsius);
	lcd.print(" C");
  	delay(1000);
  	lcd.clear();
	
}

```  
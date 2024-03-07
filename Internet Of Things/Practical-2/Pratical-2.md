### ***Practical-2*** 

<hr>

#### In this practical i have created trafic light demo circuit using arduino

***Circuit Diagram***

![Practical-2](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/b3fe6756-078f-441a-9810-3454401486ca)

<hr>

***Arduino Code***

```cpp

#define DELAY 2000
#define led_red 0
#define led_yellow 1
#define led_green 2

void setup()
{
  pinMode(led_red, OUTPUT);
  pinMode(led_yellow, OUTPUT);
  pinMode(led_green, OUTPUT);
}

void loop()
{
 digitalWrite(led_green, HIGH);
 digitalWrite(led_yellow, LOW);
 digitalWrite(led_red, LOW);
 delay(DELAY);
  
 digitalWrite(led_green, LOW);
 digitalWrite(led_yellow, HIGH);
 digitalWrite(led_red, LOW);
 delay(DELAY);
  
 digitalWrite(led_green, LOW);
 digitalWrite(led_yellow, LOW);
 digitalWrite(led_red, HIGH);
 delay(DELAY);
}

```	

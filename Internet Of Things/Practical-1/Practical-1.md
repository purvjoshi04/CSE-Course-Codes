### ***Practical-1***

<hr>

***Description***
#### In this practical i have created simple circuit which is used to blink light LED using arduino 

<hr>

***Circuit Diagram***

![Screenshot (11)](https://github.com/purvjoshi04/Curriculum-Codes/assets/101319136/9f9aac26-e675-4aaf-97b8-4ac05d7c6ec5)

<hr>

***Arduino Code***

```cpp

// C++ code
//
int led_red = 0;
void setup()
{
  pinMode(led_red, OUTPUT);
}

void loop()
{
  digitalWrite(led_red, HIGH);
  delay(1000);
  digitalWrite(led_red, LOW);
  delay(1000);
}

```

***Practical-1***

<hr>

###### In this practical i have created simple circuit which is used to blink light using arduino 

[Practical.md](https://github.com/purvjoshi04/Curriculum-Codes/files/14524690/Practical.md)

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
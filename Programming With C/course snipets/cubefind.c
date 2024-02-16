#include<stdio.h>
void print()
{
printf("cube of number using user-defined function\n");
}


int cube(int a)
{
int Cube;
Cube=a*a*a;
return Cube;
}
void main()
{
int x=2,y;
y=cube(x);
//printf("The cube of %d is:%d\n",x,y);
printf("The cube of %d is:%d\n",x,cube(x));
}


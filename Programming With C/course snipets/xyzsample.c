#include<stdio.h>

void print()
{
printf("Addition of two numbers using user-defined function\n");
}
int add(int a,int b)
{
int sum;
sum=a + b;
return sum;
}
void main()
{
int x=3,y=5,z;
z=add(x,y);

//printf(Addition of %d and %d is :%d\n",x,y,z);
printf("addition of %d and %d is :%d\n",x,y,add(x,y));

}



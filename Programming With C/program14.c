#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int x,y,z;
printf("Enter 1 for Addition\n");
printf("Enter 2 for Subtraction\n");
printf("Enter 3 for Multiplication\n");
printf("Enter 4 for Division\n");
printf("Enter Choice :");
scanf("%d",&x);
printf("Enter Number :");
scanf("%d",&y);
printf("Enter Number :");
scanf("%d",&z);
switch(x)
{
case 1:
{
printf("Addition of %d and %d is %d\n",y,z,y+z);
}
break;
case 2:
{
printf("Subtraction of %d and %d is %d\n",y,z,y-z);
}
break;
case 3:
{
printf("Multiplication of %d and %d is %d\n",y,z,y*z);
}
break;
case 4:
{
printf("Division of %d and %d is %d\n",y,z,y/z);
}
break;
default:
{
printf("You have entered wrong number.\n");
}
}
}

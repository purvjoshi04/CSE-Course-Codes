#include<stdio.h>
#include"enrol.h"
void print()
{
printf("The factorial of a number using user-defined function\n");
}


int fact(int num)
{
if(num==0)

{
return 1;
}else 
{ 
return fact(num-1)*num;
}
}

void main()
{
enrol_print();
int num,z;
printf("Enter number :");
scanf("%d",&num);
z=fact(num);
printf("Factorial of %d is %d\n",num,z);
}

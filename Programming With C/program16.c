#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int Fact=1,i,num;
printf("Enter a number :");
scanf("%d",&num);
for(i=num;i>1;i--)
{
Fact*=i;
}
printf("Factorial of %d is :%d\n",num,Fact);

}

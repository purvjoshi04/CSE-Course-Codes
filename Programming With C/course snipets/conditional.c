#include<stdio.h>
void main()
{
int age=50; 
int i=45,j=12,var;


(age>=18)?printf("Eligible\n"):printf("Not Eligible\n");
var=(i>j)?i:j;
printf("The larger number is %d\n",var);
var=(i<j)?i:j;
printf("The smaller number is %d\n",var);

}

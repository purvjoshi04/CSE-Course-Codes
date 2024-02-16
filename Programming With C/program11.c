
#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int age,N;
int scan;
printf("Enter you age in year:");
scan=scanf("%d",&age);

if(scan==0)
{
printf("you have not entered valid age\n");
}
N=365*24*3600*age;
if(scan!=0)
{
printf("You have lived for %d seconds\n",N);
scan=scanf("%d",&age);
}
}


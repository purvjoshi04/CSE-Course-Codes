#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int a,b,c,big;

printf("Enter three number:");
scanf("%d %d %d",&a,&b,&c);
big=a;
if(b>big) big=b;
if(c>big) big=c;

printf("The larger amongst three is %d\n",big);
}

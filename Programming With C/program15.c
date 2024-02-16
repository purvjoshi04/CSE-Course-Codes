#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int i,n;
printf("Enter number :");
scanf("%d",&n);
for(i=1;i<=10;i++)
{
printf("%d*%d=%d\n",n,i,n*i);
}
}


#include<stdio.h>
#include"enrol.h"
/*using array to find largest and smallest number */
void main()
{ 
enrol_print();
int a[10],i,large,small;
printf("enter the number :");
for(i=0;i<10;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<10;i++)
{
if(a[i]>large) large=a[i];
else if(a[i]<small) small=a[i];
}
printf("The largest number is :%d\n",large);
printf("The smallest number is :%d\n",small);
}

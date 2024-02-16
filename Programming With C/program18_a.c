#include<stdio.h>
#include"enrol.h"
void main()
{
int i,j,n;
printf("Enter a number of rows to be printed :");
scanf("%d",&n);
{
for(i=1;i<=n;i++)
{
for(j=1;j<=i;j++)
{
printf("*");
}
printf("\n");
}
}
}

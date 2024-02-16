#include<stdio.h>
void main()
{
int t=0,m=1;
t=m++;
printf("t=%d m=%d\n",t,m);
t=0,m=1;
t=++m;

printf("t=%d m=%d\n",t,m);
}

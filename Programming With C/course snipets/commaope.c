#include<stdio.h>
void main()
{
int i,j;
i=(i=3,j+2);
printf("i=%d,j+%d\n",i,j);
printf("%ld\n",sizeof(int));
}


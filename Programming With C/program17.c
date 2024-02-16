#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int i,j;
	for(i=0;i<=100;i++)
	{
		for(j=2;j<=i;j++)
		
		if(i%j==0)
			{
				break;
			}
			
			if(i==j)
			{

				printf("%d is a prime number.\n",i);
			}
			}
			}




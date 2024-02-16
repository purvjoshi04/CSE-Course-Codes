#include<stdio.h>
#include"enrol.h"
/* accending and desending order */
void main()
{
enrol_print();
int num[10],j,k,temp;
printf("Enter ten numbers :\n");
	for(j=0;j<10;j++)
		{
			scanf("%d",&num[j]);
		}
			for(j=0;j<10;j++)
			{
				for(k=j+1;k<10;k++)
				{
					if(num[j]<num[k])
					{
						temp=num[j];
						num[j]=num[k];
						num[k]=temp;
					}
				}
			}
					printf("Acending order is :\n");
					for(j=0;j<10;j++)

		{
					printf("%d\n",num[j]);
	
			
}
}




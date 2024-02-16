#include <stdio.h>              



int main()                        
{
	int a[10],n,i,j;
	printf("Enter ten number : ");
        scanf("%d",&n);
        
        
      for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
	for (int i = 0; i < n; i++)                     
	{
		for (int j = 0; j < n; j++)        
		{
			if (a[j] > a[i])               
			{
				int tmp = a[i];        
				a[i] = a[j];            
				a[j] = tmp;             
			}  
		}
	}
	printf("\n\nAscending : ");                     
	for (int i = 0; i < n; i++)                   
	{
		printf(" %d ", a[i]);
	}
	for (int i = 0; i < n; i++)                 
	{
		for (int j = 0; j < n; j++)             
		{
			if (a[j] < a[i])                
			{
				int tmp = a[i];         
				a[i] = a[j];          
				a[j] = tmp;             
			}
		}
	}
	printf("\n\nDescending : ");                    
	for (int i = 0; i < n; i++)                     
	{
		printf(" %d ", a[i]);                   
	}

	          

}
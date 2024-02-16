#include<stdio.h>

void fun(int *a)
{
	*a=*a+1;

}
void main()
{ 

int a=10;
fun(&a);
printf("after calling function :%d\n",a);
}



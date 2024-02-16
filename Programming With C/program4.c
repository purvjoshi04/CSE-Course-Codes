#include<stdio.h>
int main()
{

int num;
printf("Enter any number :");
scanf("%d",&num);

int count;
count=0;

for(int i =2; i <=num/2; i++)
{
    if(num%i==0)
    {
        count++;
        break;

    }
}
if (count==0)
{
    printf("It is a prime number\n");

}
else
 printf("It is not a prime number\n");
}

#include<stdio.h>
void main()
{
    int num,i;
    printf("Enter any number :");
    scanf("%d",&num);
    for(i=2;i<=num/2;i++)
    if(num%i==0 || num%2==0)
    {
        printf("The number is not prime\n");

    }
    if(!(num%i==0 || num%2==0))
    {
        printf("The number is prime\n");

    }
}
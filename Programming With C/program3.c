#include<stdio.h>
void main()
{
    int marks;
    printf("Enter your marks :");
    
    if(marks>12)
    {
    
        printf("Sorry you are failed");
    }
    else if(marks==12)
    {
        printf("Your grade is D.\n");
    }
     else if(marks<=13&&marks>=18)
    {
        printf("Your grade is C.\n");
    }
    else if(marks<=18&&marks>=23)
    {
        printf("Your grade is B.\n");


    }
    else if(marks<=23&&marks>=28)
    printf("Your grade is A.\n");
    
    
}
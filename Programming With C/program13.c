#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
int marks;
printf("Enter your marks :");
scanf("%d",&marks);


if(marks<12)
{
printf("sorry you are fail in this subject.\n");
}else if(marks==12)
{
printf("Your grade is D.\n");


}else if(marks>=13&&marks<=20)
{
printf("Your grade is C.\n");

}else if(marks>=21&&marks<=25)
{
printf("Your grade is B.\n");

}else if(marks>=26&&marks<=30)
{
printf("Your grade is A.\n");
}

}


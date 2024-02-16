#include<stdio.h>
#include"enrol.h"
int swap(int x , int y);

void main()
{

enrol_print();
int x,y;
printf("Enter number 1:");
scanf("%d",&x);
printf("Enter number 2:");
scanf("%d",&y);
swap(x,y);
printf("Number before swapping :%d,%d\n",x,y);



}
int swap(int x , int y)
{
int temp=x;
x=y;
y=temp;
printf("Number after swapping :%d,%d\n",x,y);
}




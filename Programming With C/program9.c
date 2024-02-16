#include<stdio.h>
#include"enrol.h"
void main()
{
enrol_print();
char day[10];
int dd,mm,yyyy;

printf("Input the day,followed by date(dd-mm-yyyy):");
scanf("%s %d-%d-%d",day,&dd,&mm,&yyyy);
printf("\nDay:%s\n",day);
printf("Date:%d\n",dd);
{ 
 if(mm==1)
{
printf("\nMonth:January\n");
}else if(mm==2)
{
printf("Month:February\n");
}else if(mm==3)
{
printf("Month:March\n");
}else if(mm==4)
{
printf("Month:April\n");
}else if(mm==5)
{
printf("Month:May\n");
}else if(mm==6)
{
printf("Month:June\n");
}else if(mm==7)
{
printf("Month:July\n");
}else if(mm==8)
{
printf("Month:August\n");
}else if(mm==9)
{
printf("Month:September\n");
}else if(mm==10)
{
printf("Month:October\n");
}else if(mm==11)
{
printf("Month:November\n");
}else if(mm==12)
{

printf("Month:December\n");
}
}
printf("Year:%d\n",yyyy);
}


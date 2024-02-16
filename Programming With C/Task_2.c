#include<stdio.h>
void main() {


int user_array[10];
printf("Enter ten numbers:\n");
for (int i=1;i<=10;++i)
scanf ("%d",user_array + 1);

printf("you have entered :\n");
for(int i=1;i<=10;++i)
printf("%d\n",*(user_array +i));
}
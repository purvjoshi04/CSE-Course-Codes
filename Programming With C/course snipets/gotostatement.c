#include<stdio.h>
void main(){
printf("A\n");
printf("B\n");

goto mylb1;
printf("C\n");

mylb1:
printf("D\n");

goto mylb2;
printf("E\n");

mylb2:
printf("F\n");
}

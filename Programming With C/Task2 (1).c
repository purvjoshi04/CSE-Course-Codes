#include<stdio.h>
void add(int user_array[10]);
void main()
{
    int i,user_array[10];
    printf("enter 10 integers:");
    for(i=0;i<10;i++)
    {
        scanf("%d",&user_array[i]);
    }
    add(user_array);
    for(i=0;i<10;i++)
    {
        printf("%d\n",user_array[i]);
    }
}
void add(int user_array[10])
{
    int i;
    for(i=0;i<10;i++)
    user_array[i]++;
}
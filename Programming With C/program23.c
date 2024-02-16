#include<stdio.h>
void swap(int*,int*);
void main()
{
    int data1, data2;
    printf("Enter two number : \n");
    scanf("%d %d",&data1,&data2);
    printf("Data1  :%d\n",data1);
    printf("Data2  :%d\n",data2);
    swap (&data1,&data2);
    printf("After swaping :\n");
    printf("Data1  :%d\n",data1);
    printf("Data2  :%d\n",data2);

}

    void swap(int *d1,int *d2)
{
    int temp;
    temp=*d1;
    *d1=*d2;
    *d2=temp;

}
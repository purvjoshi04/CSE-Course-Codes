// PRACTICAL-7

// AIM: Implementation of sorting technique - Bubble Sort

#include<stdio.h>
void printArray(int* array, int size){
    for(int i = 0; i<size; i++){
        printf("%d ", array[i]);
    }
    printf("\n");
}

void bubbleSort(int* array, int size){
    int isSorted = 0;
    for (int i = 0; i < size-1; i++)
    {
        printf("Swap pass number %d\n", i+1);
        isSorted = 1;
        for (int j = 0; j < size-1-i; j++)
        {
            if(array[j]>array[j+1]){
            int temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
            isSorted=0;
            }
        }
        if(isSorted){
            return;
        }
        
    }
}
int main()
{
int size;
printf("Enter the size of the array: ");
scanf("%d",&size);

int array[size];
printf("Enter the element of the array: \n");
for(int i = 0; i<size; i++){
    scanf("%d",&array[i]);

}
printf("Array before sort: ");
printArray(array, size);
bubbleSort(array, size);

printf("Array after sort: ");
printArray(array, size);
return 0;
}
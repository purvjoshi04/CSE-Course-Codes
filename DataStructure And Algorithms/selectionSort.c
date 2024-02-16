// PRACTICAL-7

// AIM: Implementation of sorting technique - Selection Sort

#include<stdio.h>
void printArray(int* array, int size){
    for(int i = 0; i<size; i++){
        printf("%d ", array[i]);
    }
    printf("\n");
}

void selectionSort(int* array, int size){
    int indexOfMin , temp;
    for (int i = 0; i < size-1; i++)
    {
        indexOfMin = i;
     for ( int j = i+1; j < size; j++)
     {
        if(array[j] < array[indexOfMin]){
            indexOfMin = j;
        }
     }
     temp = array[i];
     array[i] = array[indexOfMin];
     array[indexOfMin] = temp;
        
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
selectionSort(array, size);

printf("Array after sort: ");
printArray(array, size);
return 0;
}
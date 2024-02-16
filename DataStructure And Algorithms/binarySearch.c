// PRACTICAL-8 

// AIM: Implementation of searching technique : Binary Search

#include<stdio.h>
int binarySearch(int array[], int size , int element){
    int low, mid , high;
    low = 0;
    high = size-1;
    while(low<=high){

    mid = (low + high)/2;
    if(array[mid] == element){
         return mid;
    }else if (array[mid]<element){
    low = mid + 1;
    }else{
        high = mid -1;
    }

}
  return -1; 
}
int main()
{
int size;
printf("Enter the size of the sorted array: ");
scanf("%d",&size);

int array[size];
printf("Enter the element of sorted array: \n");
for (int i = 0; i < size; i++)
{
    scanf("%d",&array[i]);
}

int searchedElement;
printf("Enter the element that you want to search in array :");
scanf("%d",&searchedElement);
 int searchIndex = binarySearch(array,size , searchedElement);
  if (searchIndex == -1) {
        printf("The element %d was not found in the array.", searchedElement);
    } else {
        printf("The element %d was found at index %d.", searchedElement, searchIndex);
    }
return 0;
}
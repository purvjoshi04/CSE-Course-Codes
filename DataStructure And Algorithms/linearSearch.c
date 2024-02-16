// PRACTICAL-8 

// AIM: Implementation of searching technique : Linear Search

#include <stdio.h>
int linearSearch(int array[], int size, int element) {
    for (int i = 0; i < size; i++) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1; 
}
int main() {
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    
    int array[size];
    printf("Enter the array elements:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &array[i]);
    }
    
    int element;
    printf("Enter the element to search: ");
    scanf("%d", &element);
    
    int searchIndex = linearSearch(array, size, element);
    if (searchIndex == -1) {
        printf("The element %d was not found in the array.", element);
    } else {
        printf("The element %d was found at index %d.", element, searchIndex);
    }
    
    return 0;
}

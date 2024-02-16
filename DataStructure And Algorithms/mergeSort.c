// PRACTICAL-7

// AIM: Implementation of sorting technique - Merge Sort
#include <stdio.h>
#include <stdlib.h>

void printArray(int *array, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void merge(int array[], int low, int mid, int high, int *temp) {
    int i, j, k;

    i = low;
    j = mid + 1;
    k = low;

    while (i <= mid && j <= high) {
        if (array[i] < array[j]) {
            temp[k] = array[i];
            i++;
        } else {
            temp[k] = array[j];
            j++;
        }
        k++;
    }

    while (i <= mid) {
        temp[k] = array[i];
        k++;
        i++;
    }

    while (j <= high) {
        temp[k] = array[j];
        k++;
        j++;
    }

    for (int i = low; i <= high; i++) {
        array[i] = temp[i];
    }
}

void mergeSort(int array[], int low, int high, int *temp) {
    if (low < high) {
        int mid = (low + high) / 2;
        mergeSort(array, low, mid, temp);
        mergeSort(array, mid + 1, high, temp);
        merge(array, low, mid, high, temp);
    }
}

int main() {
    int size;
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int *array = malloc(size * sizeof(int));
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < size; i++) {
        scanf("%d", &array[i]);
    }

    int *temp = malloc(size * sizeof(int));

    printf("Array before sort: ");
    printArray(array, size);

    mergeSort(array, 0, size - 1, temp);

    printf("Array after sort: ");
    printArray(array, size);

    free(array);
    free(temp);

    return 0;
}

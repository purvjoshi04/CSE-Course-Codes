class BubbleSort {
    constructor() {
      this.array = [];
    }
    
    getArray() {
      const length = parseInt(prompt("Enter the length of the array: "));
      for (let i = 0; i < length; i++) {
        this.array.push(parseInt(prompt(`Enter element ${i+1}: `)));
      }
      return this.array;
    }
    
    sort() {
      const n = this.array.length;
      for (let i = 0; i < n-1; i++) {
        for (let j = 0; j < n-i-1; j++) {
          if (this.array[j] > this.array[j+1]) {
            let temp = this.array[j];
            this.array[j] = this.array[j+1];
            this.array[j+1] = temp;
          }
        }
      }
      return this.array;
    }
  }
  
  const bubbleSort = new BubbleSort();
  const array = bubbleSort.getArray();
  console.log("Original Array: ", array);
  const sortedArray = bubbleSort.sort();
  console.log("Sorted Array: ", sortedArray);
  
//concat() method

const arr_1=["Purv"];
const arr_2=["Joshi"];
console.log(arr_1.concat(arr_2));
/*The concat() method concatenates (joins) two or more arrays.
The concat() method returns a new array, containing the joined arrays.
The concat() method does not change the existing arrays.
*/

/*
output:
['Purv','Joshi']
*/

//constructor method
const arr_3=["Purv","Joshi"];
console.log(arr_3.constructor);//The constructor property returns the function that created the Array prototype.

/*
output:
[Function: Array]
*/

//copywithin() method
const fruits=["Banana","Apple","Kiwi"];
console.log(fruits.copyWithin(1,0));
/*
The copyWithin() method copies array elements to another position in the array.
The copyWithin() method overwrites the existing values.
The copyWithin() method does not add items to the array.
*/

/*
output:
[ 'Banana', 'Banana', 'Apple' ]
*/

//entries() method
const arr_4=["Purv","Devenbhai","Joshi"];
var result=arr_4.entries();
for(let x of result){
  console.log(x)
}
//The entries() method returns an Array Iterator object with key/value pairs
//The entries() method does not change the original array.

/*
output:
[ 0, 'Purv' ]
[ 1, 'Devenbhai' ]
[ 2, 'Joshi' ]
*/

//every() method 
const ages=[20,50,40,45,100];
function checkAge(age){
  return age>=20;
}
console.log(ages.every(checkAge));
/*
The every() method executes a function for each array element.
The every() method returns true if the function returns true for all elements.
The every() method returns false if the function returns false for one element.
The every() method does not execute the function for empty elements.
The every() method does not change the original array
*/

/*
ouput:
true
*/

//fill() method 
const arr_5=["Purv","Devenbhai","Joshi"];
console.log(arr_5.fill("#@$"));
/*
The fill() method fills specified elements in an array with a value.
The fill() method overwrites the original array.
It will change original array 
*/

/*
output:
[ '#@$', '#@$', '#@$' ]
*/

//filter() method 
const age1=[10,30,40,50,100];
console.log(age1.filter(fetch));
function fetch(char){
  return char>=5
}
/*
The filter() method creates a new array filled with elements that pass a test provided by a function.
The filter() method does not execute the function for empty elements.
The filter() method does not change the original array.
  */

/*
ouput:
[ 10, 30, 40, 50, 100 ]
*/

//find() method
const age2=[10,3,20,45,16];
console.log(age2.find(getAge))
function getAge(Age){
  return Age>2
}
/*
The find() method returns the value of the first element that passes a test.

The find() method executes a function for each array element.

The find() method returns undefined if no elements are found.

The find() method does not execute the function for empty elements.

The find() method does not change the original array.
  */

/*
ouput:
10
*/

//findIndex() method 
const age3=[3,10,20,45,16];
console.log(age3.find(getAge))
function getAge(Age){
  return Age>2
}
/*
The findIndex() method executes a function for each array element.

The findIndex() method returns the index (position) of the first element that passes a test.

The findIndex() method returns -1 if no match is found.

The findIndex() method does not execute the function for empty array elements.

The findIndex() method does not change the original array.
*/

/*
output:
3
*/

//forEach() method
const age4=[3,10,20,45,16];
age4.forEach((Value)=>{
  console.log(Value*Value);
});
/*
The forEach() method calls a function for each element in an array.

The forEach() method is not executed for empty elements.
  */

/*
ouput:
3
9
100
400
2025
256
*/

//from() method
let var_1="ABCDEFGHIJKLMN"
console.log(Array.from(var_1))
/*
The Array.from() method returns an array from any object with a length property.

The Array.from() method returns an array from any iterable object.


  output:
  [
  'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H',
  'I', 'J', 'K', 'L',
  'M', 'N'
]
  */

//includes() method
const arr_6=["Purv","Joshi"];
console.log(arr_6.includes("Joshi"));
/*
The includes() method returns true if an array contains a specified value.

The includes() method returns false if the value is not found.

The includes() method is case sensitive.

Output:
false

*/

//indexOf() method
const arr_7=["Purv","Devenbhai","Joshi"];
console.log(arr_7.indexOf("Joshi"));
/*
The indexOf() method returns the first index (position) of a specified value.

The indexOf() method returns -1 if the value is not found.

The indexOf() method starts at a specified index and searches from left to right.

By default the search starts at the first element and ends at the last.

Negative start values counts from the last element (but still searches from left to right).

output:
1
*/

//isArray() method
const arr_8=["Purv"];
console.log(Array.isArray(arr_8))
/*
  The isArray() method returns true if an object is an array, otherwise false.

  output:
  true
*/

//join() method
const arr_9=["Purv","Joshi"];
console.log(arr_9.join(" Devenbhai ",1))
/*
  The join() method returns an array as a string.

The join() method does not change the original array.

Any separator can be specified. The default is comma (,).

Output:
  Purv Devenbhai Joshi
  */

//keys() method
const arr_10=["Purv","Joshi"];
console.log(Object.keys(arr_10))
/*
The keys() method returns an Array Iterator object with the keys of an array.

The keys() method does not change the original array.

output:
[ '0', '1' ]
 */

//lastIndexOf() method
const arr_11=["Joshi","Purv","Joshi","Purv"];
console.log(arr_11.lastIndexOf("Purv"));

/*
The lastIndexOf() method returns the last index (position) of a specified value.

The lastIndexOf() method returns -1 if the value is not found.

The lastIndexOf() starts at a specified index and searches from right to left.

By defalt the search starts at the last element and ends at the first.

Negative start values counts from the last element (but still searches from right to left).

output:
3
*/

//length method
const arr_12=[20,30,1,5,40];
console.log(arr_12.length);
/*
The length property sets or returns the number of elements in an array.

output:
5
*/

//map() method 
let a=[1,2,3,4,5];
let b=a.map((value,index,array)=>{
  console.log(index,array);
  return value*value
});
console.log(b,a)

/*
map() creates a new array from calling a function for every array element.

map() calls a function once for each element in an array.

map() does not execute the function for empty elements.

map() does not change the original array.

output:
0 [ 1, 2, 3, 4, 5 ]
1 [ 1, 2, 3, 4, 5 ]
2 [ 1, 2, 3, 4, 5 ]
3 [ 1, 2, 3, 4, 5 ]
4 [ 1, 2, 3, 4, 5 ]
[ 1, 4, 9, 16, 25 ] [ 1, 2, 3, 4, 5 ]
  */

//pop() method 
const arr_13=["Purv","Joshi"];
console.log(arr_13.pop());

/*
The pop() method removes (pops) the last element of an array.

The pop() method changes the original array.

The pop() method returns the removed element.

output:
Joshi
*/

//push() method
const arr_14=[1,2,3,4,5];
console.log(arr_14.push(10))
console.log(arr_14)

/*
The push() method adds new items to the end of an array.

The push() method changes the length of the array.

The push() method returns the new length.

output:
6
[ 1, 2, 3, 4, 5, 10 ]
*/

//reduce() method
const arr_15=[10,20,30,40,50];
const result3=arr_15.reduce((value1,value2)=>{
  return value1*value2;
});
console.log(result3);
/*
The reduce() method executes a reducer function for array element.

The reduce() method returns a single value: the function's accumulated result.

The reduce() method does not execute the function for empty array elements.

The reduce() method does not change the original array.

output:
12000000
*/

//reduceRight() method
const arr_16=[10,20,30,40,50];
console.log(arr_16.reverse());
/*
The reverse() method reverses the order of the elements in an array.

The reverse() method overwrites the original array.

output:
[50,40,30,20,10]
*/

//shift() method
const arr_17=[10,20,30,40,50];
console.log(arr_17.shift());
/*
The shift() method removes the first item of an array.

The shift() method changes the original array.

The shift() method returns the shifted element.

output:
10
*/

//unshift() method 
const arr_18=[10,20,30,40,50];
arr_18.unshift(1,2,3);
console.log(arr_18);
/*
The unshift() method adds new elements to the beginning of an array.

The unshift() method overwrites the original array.

output:
[1,2,3,10,20,30,40,50]
*/

//slice() method
const arr_19=[10,20,30,40,50];
console.log(arr_19.slice(2,4));
/*
The slice() method returns selected elements in an array, as a new array.

The slice() method selects from a given start, up to a (not inclusive) given end.

The slice() method does not change the original array.

output:
[30,40]
*/

//some() method 
const arr_20=[10,20,30,40,50];
console.log(arr_20.some(bigNum));
function bigNum(num) {
  return num>25;
   
}
/*
The some() method checks if any array elements pass a test (provided as a callback function).

The some() method executes the callback function once for each array element.

The some() method returns true (and stops) if the function returns true for one of the array elements.

The some() method returns false if the function returns false for all of the array elements.

The some() method does not execute the function for empty array elements.

The some() method does not change the original array.

output:
true
*/

//sort() method 
const arr_21=[20,10,50,30,40];
console.log(arr_21.sort());
/*
The sort() sorts the elements of an array.

The sort() overwrites the original array.

The sort() sorts the elements as strings in alphabetical and ascending order.

output:
[ 10, 20, 30, 40, 50 ]
*/

//splice() method 
const arr_22=[10,20];
arr_22.splice(1,1,30);
console.log(arr_22)

/*
The splice() method adds and/or removes array elements.

The splice() method overwrites the original array.

output:
[10,30]
*/

//toString() method 
const arr_23=[10,20,30];
console.log(arr_23.toString());

/*
The toString() method returns a string with array values separated by commas.

The toString() method does not change the original array.

output:
10,20,30
*/

//valueOf() method 
const arr_24=["Purv","Devenbhai","Joshi"];
console.log(arr_24.valueOf());
/*
The valueOf() method returns the array itself.

The valueOf() method does not change the original array.

output:
[ 'Purv', 'Devenbhai', 'Joshi' ]

*/

//prototype method 


//reduceRight() method 
const numbers = [1, 2, 3, 4];
const sum = numbers.reduceRight((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum);  
/*
The reduceRight() method executes a reducer function for each array element.

The reduceRight() method works from right to left.

The reduceRight() method returns a single value: the function's accumulated result.

The reduceRight() method does not execute the function for empty elements.

output:
10
*/


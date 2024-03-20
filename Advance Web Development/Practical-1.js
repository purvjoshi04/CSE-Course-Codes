 //charAt() method
 var str = "hello world!!"
console.log(str.charAt(6)) //returns the character at the specified index

 /*
 Output:
  d
*/

//concat()method
var str_1 = "hello"
var str_2 = "world"
var str_3 = str_1.concat(" ", str_2)//Joins two or more strings together.
console.log(str_3)

/*
Output:
 hello world
*/

//endswith() method
var str = "hello world"
var result = str.endsWith("d")//Determines whether a string ends with a specified string.
console.log(result)

/*
Output:
 true
*/

//fromCharCode() method 
let text = String.fromCharCode(72, 101, 108, 108, 111);
console.log(text)// Returns a string created from the specified sequence of Unicode values.
/*
Output:
Hello
*/

//charCodeAt() method
let string = "hello world"
console.log(string.charCodeAt(1))//The charCodeAt() method returns the Unicode of the character at a specified index (position) in a string.

/*
Output:
101
*/



// includes() method
let in_str = "JavaScript"
console.log(in_str.includes("s"))// Determines whether a string contains a specified string or character.

/*
Output:
false
*/

//constructor method
function string_method() {
  let str_4 = "hello wolrd"
  console.log(str_4.constructor)//The constructor property returns the function that created the String prototype.

  const cars = { "Saab": 1, "Volvo": 2, "BMW": 3 }
  console.log(cars.constructor)


}
string_method()

/*
Output:
[Function: String]
[Function: Object]
*/


//indexOf() method
var text_2 = "Hello world, welcome to the universe.";
console.log(text_2.indexOf("welcome"));//Returns the first index at which a given element can be found in the array, or -1 if it is not present.

/*
Output:
13
*/

//lastIndexOf() method
let text_3 = "Hello planet earth";
console.log(text_3.lastIndexOf("earth"));

/*
Output:
13
*/


//length method 
let str_5 = "Hello World"
console.log(str_5.length)//The length property returns the length of a string.

/*
Output:
11
*/

//localeCompare() method
let text1 = "CA";
let text2 = "cd";
console.log(text1.localeCompare(text2));
// The localeCompare() method compares two strings in the current locale.
// The localeCompare() method returns sort order -1, 1, or 0 (for before, after, or equal).

/*
Output:
-1
*/

//match() method 
let str_6 = "Hello world"
console.log(str_6.match(/el/gi))
/*
The match() method matches a string against a regular expression **
The match() method returns an array with the matches.
The match() method returns null if no match is found.

Output:
[ 'el' ]
*/

//prototype method 
function student_info(name,branch,sem){
this.name="Purv";
  this.branch="Btech CSE";
  this.sem="4th sem ";
}
//The prototype property allows you to add new properties and methods to strings.
student_info.prototype.university="Uka Tarsadia university Bardoli";

const obj=new  student_info();
console.log(obj.university)

/*
Output:
Uka Tarsadia university Bardoli
*/

//repeat() method 
let str_7="Hello World "
console.log(str_7.repeat(3))//The repeat() method returns a string with a number of copies of a string.

/*
Output:
Hello World Hello World Hello World
*/

//replace() method
let str_8="Hello world"
console.log(str_8.replace("world","Earth"))//The replace() method searches a string for a value or a regular expression.

/*
Output:
Hello Earth
*/

//search() method
let str_9="Hello world!!"
console.log(str_9.search("!"))
//It searches a specified regular expression in a given string and returns its position if a match occurs.

/*
Output:
11
*/

//slice() method 
let str_10="Hello world"
console.log(str_10.slice(0,5))
//It is used to fetch the part of the given string. It allows us to assign positive as well negative index.

/*
Output:
Hello 
*/

//split() method 

let str_11="hello world";
console.log(str_11.split(" "));
//It splits a string into substring array, then returns that newly created array.

/*
output:
[ 'hello', 'world' ]
*/

//substr() method
let str_12="hello world";
console.log(str_12.substr(0,6))
//It is used to fetch the part of the given string on the basis of the specified starting position and length.

/*
  output:
hello
*/


//toString() method 

let str_13="Hello World";
console.log(str_13.toString())
// 	It provides a string representing the particular object.

/*
  output:
Hello World
*/

//valueOf() method 
let str_14="hello world";
console.log(str_14.valueOf())
//It provides the primitive value of string object.

/*
  output:
hello world
*/

//toLowerCase() method

let str_15="HELLO WORLD";
console.log(str_15.toLowerCase());
//It converts the given string into lowercase letter.

/*
output:
hello world 
*/

//toLocaleLowerCase method 

let str_16="HELLO WORLD";
console.log(str_16.toLocaleLowerCase())
//JavaScript string toLocaleLowerCase() method converts the string to lowercase letter on the basis of host's current locale. In most cases, this method returns the similar result as the toLowerCase() method.

/*
  output:
hello world 
*/

//toUpperCase() method 

let str_17="hello world";
console.log(str_17.toUpperCase())
//It converts the given string into uppercase letter.

/*
output:
HELLO WORLD 
*/

//toLocaleUpperCase() method 

let str_18="HELLO WORLD";
// console.log(str_18.toLocaleLowercase())

/*
  output:
HELLO WORLD
*/

//trim() method

let str_19=" hello world ";
console.log(str_19.trim());
//It trims the white space from the left and right side of the string.

/*
output:
hello world 
*/

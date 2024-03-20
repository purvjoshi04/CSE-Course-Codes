// // javascript to delete the name property and change the sclass property value from the follwing object also print the object before and after the said opreations hint: use data properties of js object 
//object is student having key : sclass ,rollnum

let studentName=prompt('Enter your name:');
let studentClass=prompt('Enter your class');
let studentRollnumber=prompt('Enter your rollnumber:');
let obj_1={
  name: studentName,
  sClass:studentClass,
  rollNumber:studentRollnumber,
  configrable:true,
  writable: true
}
console.log("Before changing the object property: ",obj_1);

delete obj_1.name;
let studentEditedClass=prompt('Enter you new class:')
obj_1.sClass=studentEditedClass;
console.log("After updating the object property:" ,obj_1);







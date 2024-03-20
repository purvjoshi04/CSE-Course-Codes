//write javascript of demonstration of function closure 
function addNum(num_1){
    return function innerFunc(num_2){
      return num_1+num_2;
       };
   }
   var obj=addNum(parseInt(prompt("Enter first number:")));
   console.log(obj(parseInt(prompt("Enter second number:"))));
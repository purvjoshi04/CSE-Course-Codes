
//fucntion overloading using function internal arguments

function calculate() {
    if (arguments.length === 1 && typeof arguments[0] === 'number') {
      return arguments[0] * 2;
    } else if (arguments.length === 2 && typeof arguments[0] === 'number' && typeof arguments[1] === 'number') {
      return arguments[0] + arguments[1];
    } else {
      throw new Error('Invalid arguments');
    }
  }
  
  console.log(calculate(10)); 
  console.log(calculate(10, 20)); 
  console.log(calculate('hello')); 
  
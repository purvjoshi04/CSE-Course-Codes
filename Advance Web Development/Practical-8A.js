//function internals 
console.log("Function internals output:")
function greet(name) {
  console.log(`Hello, ${name}!`);
  console.log(`The number of arguments passed is: ${arguments.length}`);
  console.log(`The function was called by: ${greet.caller} `);
  console.log(`The new.target property is: ${new.target}`);
}
function call(){
  let obj=new greet("Purv");
}

call() 
console.log("\nFunction method outout:")


//function methods
const personGreet = {
  name: "Purv",
  greet: function(greetMessage){
    console.log(`${greetMessage} ${this.name}!`);
  }
};

personGreet.greet.call({name:"Joshi"} , "Hello");

personGreet.greet.apply({name:"Purv"} , ["Hello"]);

const bind = personGreet.greet.bind({name: "Joshi"});
bind('Hello');

console.log(personGreet.greet.toString())




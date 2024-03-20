let arr = [];
let input;

do {
  input = prompt("Enter a number to generate a Fibonacci sequence (or type 'done' to exit):");
  if (input !== "done") {
    arr.push(parseInt(input));
  }
} while (input !== "done");

function fibonacciIterative(n) {
  let fib = [0, 1];
  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2];
  }
  return fib.slice(0, n+1);
}

arr.forEach(num => {
  console.log(fibonacciIterative(num));
});

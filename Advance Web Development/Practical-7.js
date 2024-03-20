let numbers = [];
for (let i = 0; i < 5; i++) {
  numbers[i] = parseInt(prompt(`Enter number ${i + 1}:`));
}
function recursiveFactorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * recursiveFactorial(n - 1);
}
let result = [];
numbers.forEach(num => {
  result.push(recursiveFactorial(num));
});
console.log(`Factorials of given array element: ${JSON.stringify(result)}`);

let cylinderArea=parseFloat(prompt("Enter cylinder area:"));
let cylinderHeight=parseFloat(prompt("Enter cylinder height:"));

let cylinderDesc={
  Area: cylinderArea,
  height:cylinderHeight
};
let result =function(cylinderDesc){
  let volume=Math.PI*cylinderDesc.Area*cylinderDesc.Area*cylinderDesc.height
  return volume.toFixed(4);
}

console.log(result(cylinderDesc));

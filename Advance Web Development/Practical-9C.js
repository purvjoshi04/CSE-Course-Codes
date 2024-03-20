//typed array with arraybuffer
const buffer = new ArrayBuffer(8);
const floatArray = new Float64Array(buffer);
floatArray[0] = 3.14159;
const intArray = new Int32Array(buffer);
console.log(intArray[1]); 

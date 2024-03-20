const myObject = {
    a: 1,
    b: 2,
    c: 3,
    [Symbol.iterator]: function* () {
      for (let key of Object.keys(this)) {
        yield [key, this[key]];
      }
    }
  };
  
  for (let [key, value] of myObject) {
    console.log(`Key: ${key}, Value: ${value}`);
  }
  
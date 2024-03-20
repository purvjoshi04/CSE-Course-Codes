// Referance Collection Map()
const map = new Map();

map.set("FirstName","Purv");
map.set('LastName',"Joshi");


alert(map.has("FirstName"));
alert(map.get("FirstName"));

alert(map.size);

map.delete("FirstName");
alert(map.get("FirstName"));

map.set("FirstName","Purv");
alert(map.get("FirstName"));

alert(map.keys());
alert(map.entries());
alert(map.values());

map.forEach((Value,key)=>{
  console.log(key + ":" + Value)
});
 map.clear();
alert(map.size);

// Referance Collection WeakMap()

const weakmap=new WeakMap();
const object_1={};
const object_2={}

weakmap.set(object_1,"Purv");
weakmap.set(object_2,'Joshi');
alert(weakmap.get(object_1));
alert(weakmap.get(object_2));

alert(weakmap.has(object_1));
alert(weakmap.has('Joshi'));

weakmap.delete(object_2);

alert(weakmap.has(object_2))

// Referance Collection Set()
const set = new Set();
set.add('Purv')
   .add('Joshi');

alert(set.has('FirstName'))
alert(set.has("LastName"));

alert(set.size);

alert(set.values());
alert(set.entries());

set.forEach((Value)=>{
  console.log(Value);
});




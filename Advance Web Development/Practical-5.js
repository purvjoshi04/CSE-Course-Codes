let text = "In this essay on technology, we are going to discuss what technology is, what are its uses, and also what technology can do? First of all, technology refers to the use of technical and scientific knowledge to create, monitor, and design machinery. Also, technology helps in making other goods that aid mankind.";


let pattern_consonants = /\b[b-df-hj-np-tv-z]\w*/igm;
console.log("Word Starting With All The Consonants");
 console.log(text.match(pattern_consonants));


let pattern_a_beginning = /\b[a]\w*/igm;
 console.log("Word Starting With The 'A'");
console.log(text.match(pattern_a_beginning));
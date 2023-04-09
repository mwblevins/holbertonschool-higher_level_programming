#!/usr/bin/node
// prints the same string multiple times
const x = parseInt(process.argv[2], 10);
if(Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

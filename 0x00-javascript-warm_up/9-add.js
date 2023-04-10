#!/usr/bin/node
// adding
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const a = process.argv[2];
const b = process.argv[3];

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}

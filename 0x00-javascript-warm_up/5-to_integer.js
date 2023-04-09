#!/usr/bin/node
// Print my number
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My numer: ' + parseInt(args[2]));
}

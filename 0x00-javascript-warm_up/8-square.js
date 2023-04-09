#!/usr/bin/node
// prints a square
const size = parseInt(process.argv[2], 10);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}

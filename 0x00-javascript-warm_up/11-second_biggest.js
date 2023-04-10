#!/usr/bin/node
// second biggest int
function secondMax (arr) {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < arr.length; i++) {
    const num = parseInt(arr[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }

  return secondMax;
}

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  console.log(secondMax(args));
}

#!/usr/bin/node
let numArgs = 0;

exports.logMe = function (item) {
  console.log(numArgs + ': ' + item);
  numArgs++;
};

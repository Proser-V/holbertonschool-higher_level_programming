#!/usr/bin/node

const arg = process.argv[2];

const num = Number(arg); /* Convert a string to an int (or NaN) */
if (Number.isInteger(num)) { /* Check if its an int */
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}

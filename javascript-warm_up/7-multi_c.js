#!/usr/bin/node

const x = process.argv[2];
const num = Number(x);
const toPrint = 'C is fun';

if (Number.isInteger(num)) {
  for (let i = 0; i < x; i++) {
    console.log(toPrint);
  }
} else {
  console.log('Missing number of occurrences');
}

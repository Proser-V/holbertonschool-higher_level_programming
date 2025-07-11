#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
let i = 0;
const argsNumber = args.length;
let currentNumber;
let biggest = Number.MIN_SAFE_INTEGER;
let secondBiggest = Number.MIN_SAFE_INTEGER;

if (argsNumber === 0 || argsNumber === 1) {
  secondBiggest = 0;
} else {
  biggest = Math.max(...args);
  currentNumber = args.indexOf(biggest);
  args.splice(currentNumber, 1)
  secondBiggest = Math.max(...args);
}
console.log(secondBiggest);

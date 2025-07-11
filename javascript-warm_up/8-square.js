#!/usr/bin/node

const x = process.argv[2];
const num = Number(x);

if (Number.isInteger(num)) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}

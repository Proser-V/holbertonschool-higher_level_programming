#!/usr/bin/node

function add () {
  const a = process.argv[2];
  const numA = Number(a);
  const b = process.argv[3];
  const numB = Number(b);

  if (Number.isInteger(numA) && Number.isInteger(numB)) {
    const sum = numA + numB;
    console.log(sum);
  } else {
    console.log(NaN);
  }
}

add();

#!/usr/bin/node

function factorielle (a) {
  if (a == undefined) return 1;
  const numA = Number(a);
  if (a == 0 || a == 1) return 1;
  if (Number.isInteger(numA)){
      return a * factorielle(numA - 1);
  }
}

console.log(factorielle(process.argv[2]));

#!/usr/bin/node

const { argv } = require('node:process');

const argument = argv[2];
const onlynumber = /^\d+$/.test(argument);

if (onlynumber !== true || argv[2] == null) {
  console.log('Not a number');
} else {
  const digits = argument.match(/\d+/g);
  console.log('My number: ' + digits);
}

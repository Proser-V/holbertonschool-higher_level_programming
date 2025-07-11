#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  let i = 1
  while (x >= i) {
    i++;
  }
  theFunction(i);
};

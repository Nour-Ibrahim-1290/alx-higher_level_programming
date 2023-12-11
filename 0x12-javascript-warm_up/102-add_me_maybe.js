#!/usr/bin/node
// increment and call function

exports.addMeMaybe = function (x, theFunction) {
  theFunction(x + 1);
};

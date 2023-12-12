#!/usr/bin/node

let nbO = 0;

exports.logMe = function (item) {
  console.log(nbO + ': ' + item);
  nbO = nbO + 1;
};

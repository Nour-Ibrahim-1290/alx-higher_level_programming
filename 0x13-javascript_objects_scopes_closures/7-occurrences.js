#!/usr/bin/node
// Funstion returns number of oocurance of an Element in aList

exports.nbOccurences = function (list, searchElement) {
  let nbO = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nbO = nbO + 1;
    }
  }

  return nbO;
};

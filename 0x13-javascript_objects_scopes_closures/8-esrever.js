#!/usr/bin/node
// Funstion returns reverse of a List

exports.esrever = function (list) {
  const rList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    rList.push(list[i]);
  }

  return rList;
};

#!/usr/bin/node
// print 3 lines using array and loop

const args = process.argv;

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(args[2], args[3]);

#!/usr/bin/node
// print 3 lines using array and loop

const n = process.argv[2];

if (n === undefined) {
  console.log('Missing number of occurrences');
} else if (n >= 0) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}

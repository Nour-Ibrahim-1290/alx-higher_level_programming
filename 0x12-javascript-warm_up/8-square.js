#!/usr/bin/node
// print 3 lines using array and loop

const size = process.argv[2];

if (size === undefined) {
  console.log('Missing size');
} else if (size >= 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
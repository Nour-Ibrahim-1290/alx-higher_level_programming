#!/usr/bin/node

// print the first argument passed

if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
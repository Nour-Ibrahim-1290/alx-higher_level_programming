#!/usr/bin/node

// print two arguments passes to it with "is" in between

const number = process.argv[2];

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parseInt(number));
}

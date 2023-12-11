#!/usr/bin/node
// search for the second biggest number in args

let args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  args = args.sort();
  console.log(args.reverse()[1]);
}

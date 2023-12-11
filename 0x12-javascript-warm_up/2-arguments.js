#!/usr/bin/node
// print message depending on the number of args passed

if (ProcessingInstruction.argv.length === 2) {
    console.log("No argument");
} else if (ProcessingInstruction.argv.length === 3) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
#!/usr/bin/node
// define a Square subclass with exta instance functions

const Squarebase = require('./5-square.js');

module.exports = class Square extends Squarebase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

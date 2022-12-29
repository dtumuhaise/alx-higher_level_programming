#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // prints rectangle using character 'C'
  charPrint (c) {
    if (c === 'C') {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write('C');
        }
        console.log('');
      }
    } else {
      super.print();
    }
  }
};

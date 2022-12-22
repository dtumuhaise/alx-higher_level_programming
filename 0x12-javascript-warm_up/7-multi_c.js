#!/usr/bin/node

const args = process.argv.slice(2);

const x = parseInt(args[0]);
let count = 0;

if (!x) {
  console.log('Missing number of occurrences');
}
while (count < x) {
  count++;
  console.log('C is fun');
}

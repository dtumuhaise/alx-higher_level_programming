#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv.slice(2);
if (args.length > 2) {
  console.log(NaN);
} else {
  console.log(add(parseInt(args[0]), parseInt(args[1])));
}

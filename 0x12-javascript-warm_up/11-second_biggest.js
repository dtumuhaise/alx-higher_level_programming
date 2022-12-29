#!/usr/bin/node

const args = process.argv.slice(2);
if (!args[0]) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  console.log(Math.max(parseInt(args)));
}

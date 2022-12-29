#!/usr/bin/node

function fact (num) {
  if (num === 0 || num === 1) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}
const args = process.argv.slice(2);
if (!args[0]) {
  console.log(1);
} else {
  console.log(fact(parseInt(args[0])));
}

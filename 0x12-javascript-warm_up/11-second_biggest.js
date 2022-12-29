#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const size = process.argv.length;
  const arr = [];
  for (let i = 2; i < size; i++) {
    arr[i - 2] = parseInt(process.argv[i]);
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}

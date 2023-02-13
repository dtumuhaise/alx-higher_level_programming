#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});

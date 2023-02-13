#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (const movie of data.results) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});

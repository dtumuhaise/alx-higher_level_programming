#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const characters = films[i].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

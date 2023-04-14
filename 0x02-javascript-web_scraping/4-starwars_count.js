#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((total, film) => {
    if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
      return total + 1;
    }
    return total;
  }, 0);
  console.log(count);
});

// fetches and lists the titles for all movies by using this URL:

const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(URL, function (data) {
  const movies = data.results;
  for (const movie of movies) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});

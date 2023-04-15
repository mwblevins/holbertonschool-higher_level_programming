$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(url, function (data) {
    $.each(data.results, function (index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(url, function (data) {
    $('#character').text(data.name);
  });
});
$(document).ready(function () {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.getJSON(url, function (data) {
    $('#hello').text(data.hello);
  });
});
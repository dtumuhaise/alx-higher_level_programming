// fetches from URL and displays value of hello
// from that fetch in the tag DIV#hello

URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(URL, function (data) {
  $('DIV#hello').text(data.hello);
});

// toggles the class of <header> between red and green when
// the user clicks on the tag DIV#toggle_header

$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red green');
});

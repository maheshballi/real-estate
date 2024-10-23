const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$(document).ready(function() {
  setTimeout(function(){
    $('#message').fadeOut('slow');
  }, 3000);
});

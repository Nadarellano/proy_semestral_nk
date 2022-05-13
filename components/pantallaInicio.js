let contadorClicks = 0;

$(document).ready(function(){
  $('.card-img-top').click(function() {
    contadorClicks += 1;
    console.log(contadorClicks);
})
});

let contadorClicks = 0;
//agrega color a parrafo de "nosotros"

console.log("probando")


$(document).ready(function(){
  $('.card-img-top').click(function() {
    contadorClicks += 1;
    console.log(contadorClicks);
})
});

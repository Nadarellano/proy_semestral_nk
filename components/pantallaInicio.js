let contadorClicks = 0;
//agrega color a parrafo de "nosotros"
function mouseOver() {
  document.getElementsByClassName("somos").style.color = "red";
}

function mouseOut() {
  document.getElementsByClassName("somos").style.color = "black";
}

console.log("probando")


$(document).ready(function(){
  $('.card-img-top').click(function() {
    contadorClicks += 1;
    console.log(contadorClicks);
})
});


console.log("funcionando")




 $(document).ready(function() {

// //     $("#get-producto").click(function () {
// //         $.ajax(
// //             {
// //                 url: "http://127.0.0.1:8000/api/lista_productos",
// //                 datatype: 'json',
// //                 method: 'GET',
// //                 success: function (data) {  
// //                     $("#producto").replaceWith(`
// //                     <h2>hola obtuviste un ${data.Producto.nombreProducto}</h2>
                    
// //                     `);
// //                 }
// //             }
// //         );
// //     });

// // $(document).ready(function() {
// // $.get('http://127.0.0.1:8000/api/lista_productos', function(data) { 
// //  console.log(data)
// //  $("#producto").html(`
// //  //                     <h2>hola obtuviste un ${data.Producto.nombreProducto}</h2>
    
// //  `);
// //             }
// //         );
// //     });


     
$.ajax(
      {
           url: "http://127.0.0.1:8000/api/lista_",
          datatype: 'json',
          method: 'GET',
         success: function (data) {  
         


            $.each(data, function (i, item) { 
//                     //Por cada elemento  agregamos una nueva fila en la tabla categorias
                     $("#order").append("<p>"+item.get_cart_items+"</p><p>" +
                                            "</p><p>" +item.get_cart_total+"");
                     
                }); 

              

              
           }
         }   );

// });

$(function() {
    //hide first div or remove after append using `$(".card:first").remove()`
    $(".card:first").hide()
   

    

    $.ajax({
      url: "http://127.0.0.1:8000/api/lista_productos",
      datatype: 'json',
                   method: 'GET',
      success: function(data) {
        $.each(data, function(index, item) {
          var cards = $(".card:first").clone() //clone first divs
          var idProducto = item.idProducto;
          var nombreProducto = item.nombreProducto;
          var precioProducto = item.precioProducto;
          var imagenProducto = item.imagenProducto;
          var categoria = item.categoria;
          
          
          //add values inside divs

          $(cards).find(".card-header").html( nombreProducto);
          $(cards).find(".thumbnail").html(imagenProducto);
          $(cards).find(".card-img-top").html(imagenProducto);
          $(cards).find(".card-text").html(precioProducto);
          $(cards).find(".card-text").html(precioProducto);
          $(cards).find(".data-product").html(idProducto);
          

          $(cards).show() //show cards  
          $(cards).appendTo ($(".container")) //append to container

        });
      }
    });
  });


  // $(function() {
  //   //hide first div or remove after append using `$(".card:first").remove()`
  //   $(".cart-row:first").hide()
  //   $.ajax({
  //     url: "http://127.0.0.1:8000/api/",
  //     datatype: 'json',
  //                  method: 'GET',
  //     success: function(data) {
  //       $.each(data, function(index, item) {
  //         let cards = $(".card:first").clone() //clone first divs
          
  //         let nombreProducto = item.nombreProducto;
  //         let precioProducto = item.precioProducto;
  //         let imagenProducto = $(src="item.imagenProducto");
  //         let idProducto = item.idProducto;
  //         let categoria = item.categoria;
  //         //add values inside divs

  //         $(cards).find(".card-header").html( nombreProducto);
  //         $(cards).find(".card-title").html(precioProducto);
  //         $(cards).find(".card-img-top").html(imagenProducto);
  //         $(cards).show() //show cards
  //         $(cards).appendTo ($(".container")) //append to container
  //       });
  //     }
  //   });
  // });

});

$(document).ready(function(){
    $('.img-rounded')
      .wrap('<span style="display:inline-block"></span>')
      .css('display', 'block')
      .parent()
      .zoom();
  });

//Funcion de mostrar formulario de cliente en el menu de opcionesCredito
$(document).ready(function(){
    $("#mostrar").click(function(){
       $("#divmuestra").each(function() {
         displaying = $(this).css("display");
         if(displaying == "block") {
           $(this).fadeOut('slow',function() {
            $(this).css("display","none");
           });
         } else {
           $(this).fadeIn('slow',function() {
             $(this).css("display","block");
           });
         }
       });
     });
   });
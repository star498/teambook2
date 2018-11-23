
$(document).ready(function() {
        
       

});
 function registrar(){
            var nombre= $('#nombre').val();
            var apellido= $('#apellido').val();
            var celular= $('#celular').val();
            var fnacimiento= $('#fnacimiento').val();
            var sexo= $('input[name="sexo"]:checked').val();
            var usuario= $('#usuario').val();
            var clave= $('#clave').val();

            console.log("nacimiento:"+ fnacimiento+ " sexo " + sexo);

          
}
function crearcuenta(){
   var usuario= $('#user').val();
   var pass= $('#pass').val();
   var url = "/login";
        $.ajax({                        
           type: "POST",                 
           url: url,                     
           data: {
            'user': usuario,
            'pass': pass
           }, 
           success: function(data)             
           {
             alert("llego");              
           }
       });
}

 function onFormSubmit() {

    var datoslistos = validarDatos();

    if(datoslistos != undefined){
        alert("Los datos se buscaran.")
    }


}

function validarDatos(){
    var formDatos = {};
    var mensaje = ""
    var aux = true;
    formDatos[0] = document.getElementById('btnGroupAddon').value
    
    

    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio.\n\n"
            aux =false;
            break;
        }
    }
    if (!validarID(formDatos[0])) {
      mensaje = mensaje + " *El ID de Cliente no es valido"
      aux=false;
    }
    
    
   
  if(aux ){
        return formDatos;

    }
    else{
        alert(mensaje)
    }
    // return formData;

   
   
   

}


    function validarID(valor){                  
        var regex = /^\d{4}/                                                   
        var response = regex.test(valor)                                                           
        return response;                                                                        
}                                                                          
var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 
                                                                                                                                                               
function ValidarArchivo(oninput) { //Verifica las extenciones de lo archivos.                                                                                                                                                      
    if (oninput.type == "file") {  // S                                                                                                                                                           
        var nombre = oninput.value;                                                                                                                                   
         if (nombre.length > 0) {                                                                                                                                                              
            var bandera = false;                                                                                                                                               
            for (var j = 0; j < extValidas.length; j++) {                                                                                                                  
                var sCurExtension = extValidas[j];                              
                if (nombre.substr(nombre.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {                                         
                    bandera = true;                            
                    break;                                                                                                                                                                      
                }                                                                                                                                                                                 
            }                                                                  
                                                                        
            if (!bandera) {    
                var modal = $('#errorfileModal')
                modal.find('.modal-title').text("Error")
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: jpg,png,jpeg.")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
} 

function onFormSubmit() {

    var datoslistos = validarDatos();

    if(datoslistos != undefined){
        alert("Los datos estan listos para ser enviados a la base de datos.")
    }


}

function validarDatos(){
    var formDatos = {};
    var mensaje = ""
    var aux = true;
    formDatos[0] = document.getElementById('btnGroupAddon').value
    formDatos[1] = document.getElementById('Monto_pres').value
    formDatos[2] = document.getElementById('SemanasPlazo').value
    formDatos[3] = document.getElementById('Fch_Inicio').value
    formDatos[4] = document.getElementById('Fch_Limite').value
    formDatos[5] = document.getElementById('file').value
    

    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio.\n\n"
            aux =false;
            break;
        }
    }
    if(!isNaN(formDatos[0])){


    }
    else{
        aux=false;
        mensaje=mensaje +", ID es invalido deben ser  numeros"
    }
    
    if(!isNaN (formDatos[1])){
        
    }
    else {
        aux=false;
        mensaje= mensaje + " , el monto es  invalido, tiene que ser un numero.\n\n "
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
                                                







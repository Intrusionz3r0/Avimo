var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 
                                                                                                                                                               
function ValidarArchivo(oninput) {                                                                                                                                                      
    if (oninput.type == "file") {                                                                                                                                                                  
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
                                                        
                alert("Solo se permiten archivos con extensiones: " + extValidas.join(", "));                                                                                                
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
    formDatos['nombre'] = document.getElementById('nombre').value
    formDatos['apellido'] = document.getElementById('apellido').value
    formDatos['genero'] = document.getElementById('genero').value
    formDatos['estado'] = document.getElementById('estado').value
    formDatos['municipio'] = document.getElementById('municipio').value
    formDatos['colonia'] = document.getElementById('colonia').value
    formDatos['calle1'] = document.getElementById('calle1').value
    formDatos['calle2'] = document.getElementById('calle2').value
    formDatos['ninterno'] = document.getElementById('ninterno').value
    formDatos['nexterno'] = document.getElementById('nexterno').value
    formDatos['telefono'] = document.getElementById('telefono').value
    formDatos['curp'] = document.getElementById('curp').value
    formDatos['fnacimiento'] = document.getElementById('fnacimiento').value
    formDatos['fregistro'] = document.getElementById('fregistro').value

    for (const key in formDatos) {
        if(formDatos[key] == ""){
            mensaje = mensaje + "Alguno de los campos esta vacio.\n\n"
            aux =false;
            break;
        }
    }
 
    if(!validarCURP(formDatos['curp'])){
        mensaje = mensaje + "La curp introducida es invalida.\n\n"
        aux =false;
    }

    if(!validarTelefono(formDatos['telefono'])){
        mensaje = mensaje + "El telefono introducido es invalido.\n\n"
        aux =false;
    }

    if(aux){
        return formDatos
    }
    else{
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
    }
    

}
                                                                               
function validarCURP(valor){                                                                
        var regex = /^[A-Z]{4}\d{6}\w{8}/                                                     
        var reponse = regex.test(valor)                                 
        return reponse;                                                                        
}                                                                                       
                                                                               
function validarTelefono(valor){                                
        var regex = /^\d{3}-\d{3}-\d{4}$/                                                     
        var response = regex.test(valor)                                            
        return response;                                                                        
}                                                                       
                                                                                          
function validarID(valor){                  
        var regex = /^\d{4}/                                                   
        var response = regex.test(valor)                                                           
        return response;                                                                        
}                                                                                   
                                                
function validarNumero(valor){                                                          
        var regex = /^\d+/                                                                
        var response = regex.test(valor)                                                           
        return response;                                                                      
}    



function agregarEstados(array){

    for (const key in array) {
        document.getElementById('estado').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
}

function consultaEstados(){
    var array = [];
    let url ='https://api-sepomex.hckdrk.mx/query/get_estados'
    var r1 = new XMLHttpRequest();
    r1.open("GET",url,false)
    r1.send(null)
    res = JSON.parse(r1.responseText)
    arr = res.response.estado
    for (const i in arr) {
        array.push(arr[i])
    }
    agregarEstados(array)
}

function agregarMunicipio(array){

    for (const key in array) {
        document.getElementById('municipio').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    document.getElementById('estado').disabled=true;
}

function consultarMunicipio(){
    var array = [];
    var estado = document.getElementById('estado').value
    let url ='https://api-sepomex.hckdrk.mx/query/get_municipio_por_estado/'+estado
    var r2 = new XMLHttpRequest();
    r2.open("GET",url,false)
    r2.send(null)
    res = JSON.parse(r2.responseText)
    arr = res.response.municipios
    for (const i in arr) {
        array.push(arr[i])
    }
    agregarMunicipio(array)
}

function agregarColonia(array){
    for (const key in array) {
        document.getElementById('colonia').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    document.getElementById('municipio').disabled=true;
}


function consultarColonia(){
    var array = [];
    var municipio = document.getElementById('municipio').value
    let url ='https://api-sepomex.hckdrk.mx/query/get_colonia_por_municipio/'+municipio
    var r3 = new XMLHttpRequest();
    r3.open("GET",url,false)
    r3.send(null)
    res = JSON.parse(r3.responseText)
    arr = res.response.colonia
    for (const i in arr) {
        array.push(arr[i])
    }
    agregarColonia(array)
}

function desactivarColonia(){
    document.getElementById('colonia').disabled=true;
}


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
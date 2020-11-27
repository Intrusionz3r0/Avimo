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
    formDatos[0] = document.getElementById('nombreCliente').value
    formDatos[1] = document.getElementById('apellidoCliente').value
    formDatos[2] = document.getElementById('generoCliente').value
    formDatos[3] = document.getElementById('estadoCliente').value
    formDatos[4] = document.getElementById('municipioCliente').value
    formDatos[5] = document.getElementById('coloniaCliente').value
    formDatos[6] = document.getElementById('calleCliente').value
    formDatos[7] = document.getElementById('entrecallesCliente').value
    formDatos[8] = document.getElementById('ninternoCliente').value
    formDatos[9] = document.getElementById('nexternoCliente').value
    formDatos[10] = document.getElementById('telefonoCliente').value
    formDatos[11] = document.getElementById('curpCliente').value
    formDatos[12] = document.getElementById('fnacimientoCliente').value
    formDatos[13] = document.getElementById('fregistroCliente').value
    formDatos[14] = document.getElementById('file1Cliente').value
    formDatos[15] = document.getElementById('file2Cliente').value
    formDatos[16] = document.getElementById('file3Cliente').value


    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Alguno de los campos esta vacio.\n\n"
            aux =false;
            break;
        }
    }
 
    if(!validarCURP(formDatos[11])){ // Si la curp es invalida devuelve un false.
        mensaje = mensaje + "La curp introducida es invalida.\n\n"
        aux =false;
    }

    if(!validarTelefono(formDatos[10])){ // si el telefono es invalido devuelve un false.
        mensaje = mensaje + "El telefono introducido es invalido.\n\n"
        aux =false;
    }

    if(aux){ //Si la variable aux es True entonces envia los datos.
        return formDatos
    }
    else{// si la variable aux es false entonces muestra un error en pantalla.
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
        document.getElementById('estadoCliente').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
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
        document.getElementById('municipioCliente').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    document.getElementById('estadoCliente').disabled=true;
}

function consultarMunicipio(){
    var array = [];
    var estado = document.getElementById('estadoCliente').value
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
        document.getElementById('coloniaCliente').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    document.getElementById('municipioCliente').disabled=true;
}


function consultarColonia(){
    var array = [];
    var municipio = document.getElementById('municipioCliente').value
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
    document.getElementById('coloniaCliente').disabled=true;
}


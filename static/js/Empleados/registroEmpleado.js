var extValidas = [".jpg", ".jpeg",".png"]; 

function onFormSubmit(){
    var datoslistos=validarDatosEmpleado();
    if(datoslistos !=undefined){
        alert("Los datos del Nuevo Empleado estan listos para ser enviados a la base de datos.");
        
    }
}

function validarDatosEmpleado(){
    var formDatos={};
    var mensaje="";
    var aux=true;
    formDatos[0]=document.getElementById("NombreEmp").value;
    formDatos[1]=document.getElementById("ApellidosEmp").value;
    formDatos[2]=document.getElementById("generoEmp").value;
    formDatos[3]=document.getElementById("estadoEmp").value;
    formDatos[4]=document.getElementById("municipioEmp").value;
    formDatos[5]=document.getElementById("coloniaEmp").value;
    formDatos[6]=document.getElementById("calleEmp").value;
    formDatos[7]=document.getElementById("ninternoEmp").value;
    formDatos[8]=document.getElementById("nexternoEmp").value;
    formDatos[9]=document.getElementById("entrecallesEmp").value;
    formDatos[10]=document.getElementById("telefonoEmp").value;
    formDatos[11]=document.getElementById("curpEmp").value;
    formDatos[12]=document.getElementById("fnacimientoEmp").value;
    formDatos[13]=document.getElementById("fingresoEmp").value;
    formDatos[14]=document.getElementById("fine1").value;
    formDatos[15]=document.getElementById("fine2").value;
    formDatos[16]=document.getElementById("ComproDomi").value;
    formDatos[17]=document.getElementById("Usuario").value;
    formDatos[18]=document.getElementById("Contraseña1").value;
    formDatos[19]=document.getElementById("Contraseña2").value;
    formDatos[20]=document.getElementById("Rol").value;
    formDatos[21]=document.getElementById("fotoempe").value;
   
    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje+"Varios campos estan vacios."
            aux=false;
            break;
        }
    }


    if(!validarTelefono(formDatos[10])){//telefono
        mensaje=mensaje+" *Formato de telefono no valido"
        aux=false;
    }

    if(!validarCURP(formDatos[11])){//CURP
        mensaje=mensaje+" *Formato de CURP no valido"
        aux=false;
    }
    

    if(!validarContraseña(formDatos[18],formDatos[19])){
        mensaje=mensaje+" La contraseña no coincide"
        aux=false;
    }

    if(aux){ //Si la variable aux es True entonces envia los datos.
        return formDatos;
    }
    else{// si la variable aux es false entonces muestra un error en pantalla.
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
    }
}

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
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: .jpg  .png  .jpeg")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
}

function validarNombre(nombre){
    var regex = /^[A-Z]{1}\w+/                                                                
    var response = regex.test(nombre)                                                           
    return response;    
}

function validarApellidos(apellidos){
    var regex = /^\w{8}/                                                                
    var response = regex.test(apellidos)                                                           
    return response;
}

function validarUsuario(Usuario){
    var regex = /^\w{5}/                                                                
    var response = regex.test(Usuario)                                                           
    return response;
}

function validarContraseña(dato1,dato2){
    if(dato1==dato2){
        return true;
    }
    else{
        return false;
    }
}

function validarNumero(Numero){
    var regex = /^\d+/                                                                
        var response = regex.test(Numero)                                                           
        return response; 
}

function validarTelefono(valor){                                
    var regex = /^\d{3}-\d{3}-\d{4}$/                                                     
    var response = regex.test(valor)                                            
    return response;                                                                        
}

function validarCURP(valor){                                                                
    var regex = /^[A-Z]{4}\d{6}\w{8}/                                                     
    var reponse = regex.test(valor)                                 
    return reponse;                                                                        
}

function validarCalle(calle){
    var regex = /^\w{3}/                                                                
    var response = regex.test(calle)                                                           
    return response;
}

function validarEntreCalles(Entre_Calles){
    var regex = /^\w{7}/                                                                
    var response = regex.test(Entre_Calles)                                                           
    return response;
}

//DOMICILIO

function agregarEstados(array){//agregar Estado
    for(const key in array){
        document.getElementById('estadoEmp').innerHTML+= "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
}

function consultaEstados(){//consultar Estado
    var obj = "";
    var arr;
    const xhr = new XMLHttpRequest();
    xhr.open("GET","https://api-sepomex.hckdrk.mx/query/get_estados");
    xhr.onload = function (){
        if (this.status === 200){
            obj = JSON.parse(this.responseText);
            arr = obj.response.estado
            agregarEstados(arr)
        }
    }

    xhr.send(); 
}

function agregarMunicipio(array){

    for (const key in array) {//agregar Municipio
        document.getElementById('municipioEmp').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    
}

function consultarMunicipio(){//consultar Municipio
    var array = [];
    var estado = document.getElementById('estadoEmp').value
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

function agregarColonia(array){//agregar Colonia
    for (const key in array) {
        document.getElementById('coloniaEmp').innerHTML += "<option value='"+array[key]+"'>"+array[key]+"</option>";
    }
    //document.getElementById('municipioCliente').disabled=true;
}

function consultarColonia(){//consultar Colonia
    var array = [];
    var municipio = document.getElementById('municipioEmp').value
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
    
}

function Limpiar(){
    document.getElementById("NombreEmp").value="";
    document.getElementById("ApellidosEmp").value="";
    document.getElementById("generoEmp").value="";
    document.getElementById("estadoEmp").value="";
    document.getElementById("municipioEmp").value="";
    document.getElementById("coloniaEmp").value="";
    document.getElementById("calleEmp").value="";
    document.getElementById("ninternoEmp").value="";
    document.getElementById("nexternoEmp").value="";
    document.getElementById("entrecallesEmp").value="";
    document.getElementById("telefonoEmp").value="";
    document.getElementById("curpEmp").value="";
    document.getElementById("fnacimientoEmp").value="";
    document.getElementById("fingresoEmp").value="";
    document.getElementById("fine1").value="";
    document.getElementById("fine2").value="";
    document.getElementById("ComproDomi").value="";
    document.getElementById("Usuario").value="";
    document.getElementById("Contraseña").value="";
    document.getElementById("Rol").value="";
}

function MostrarDiv(div){
    document.getElementById(div).style.display="block";
}

function OcultarDiv(div){
    document.getElementById(div).style.display="none";
}

function MostrarRegEmp(){
    MostrarDiv("Reg_Empleado");
    OcultarDiv("Asig_Rol");
}

function MostrarAsigRol(){
    MostrarDiv("Asig_Rol");
    OcultarDiv("Reg_Empleado");
}
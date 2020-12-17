var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 
                                                                                                                                                               

function onFormSubmit(){
    var datoslistos= validarDatosPago();
    if(datoslistos != undefined){

    }
    
}

function validarDatosPago(){
    var formDatos={};
    var mensaje="";
    var aux=true;
    formDatos[0]=document.getElementById("ID_Cliente").value;
    formDatos[1]=document.getElementById("ID_Credito").value;
    formDatos[2]=document.getElementById("Monto").value;
    formDatos[3]=document.getElementById("Semanas").value;
    formDatos[4]=document.getElementById("Fch_Pago").value;
    formDatos[5]=document.getElementById("F_Comprobante").value;
    formDatos[6]=document.getElementById("curp").value;

    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje + "Varios campos estan vacios.\n"
            aux=false;
            break;
        }
    }

    if(!validarCURP(formDatos[6])){
        mensaje=mensaje+"La curp introducida es invalida"
    }
    
    if(isNaN(formDatos[0])){
        mensaje=mensaje+" Ingresaste datos incorrectos"
        aux=false
    }
    if(isNaN(formDatos[1])){
        mensaje=mensaje+" Ingresaste datos incorrectos"
        aux=false
    }
    if(isNaN(formDatos[2])){
        mensaje=mensaje+" Ingresaste datos incorrectos"
        aux=false
    }




    

    if(aux){
        document.getElementById("comprobar").style.display="none"
        document.getElementById("enviar").style.display="block"
        return formDatos;
        
    }else{
        var modal=$('#errorModal')
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
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: jpg,png,jpeg.")
                modal.modal('show')                                                                                                                                     
                oninput.value = "";                                             
                return false;                                   
            }                                                                  
        }                                                                           
    }                                                                               
    return true;                                                        
}

function validarNumero(val){
    var regex= /^\d[0-9]+/
    var response=regex.test(val)
    return response;
}

function validarCURP(valor){                                                                
    var regex = /^[A-Z]{4}\d{6}\w{8}/                                                     
    var reponse = regex.test(valor)                                 
    return reponse;                                                                        
}  
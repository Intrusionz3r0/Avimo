var extValidas = [".jpg", ".jpeg",".png"];                                                                                                                                 
                                                                                                                                                               

function onFormSubmit(){
    var datoslistos= validarDatosPago();
    if(datoslistos != undefined){
        alert("Los datos estan listos para ser enviados a la base de datos.");
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

    for(const key in formDatos){
        if(formDatos[key]==""){
            mensaje=mensaje + "Alguno de los campos esta vacio.\n"
            aux=false;
            break;
        }
    }

    if(!validarCliente(formDatos[0])){
        mensaje=mensaje+"El ID de Cliente no es valido\n"
        aux=false
    }

    if(!validarCredito(formDatos[1])){
        mensaje=mensaje+"El ID de Crédito no es valido\n"
        aux=false
    }

    if(!validarMonto(formDatos[2])){
        mensaje=mensaje+"El ID Monto ingresado no es valido\n"
        aux=false
    }

    

    if(aux){
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

function validarCliente(ID_Cli){
    var regex= /^\d{4}/
    var response=regex.test(ID_Cli)
    return response;
}

function validarCredito(ID_Cre){
    var regex= /^\d{4}/
    var response=regex.test(ID_Cre)
    return response;
}

function validarMonto(Monto){
    var regex = /^\d+/                                                                
        var response = regex.test(Monto)                                                           
        return response;
}



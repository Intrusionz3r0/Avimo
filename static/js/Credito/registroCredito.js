var extValidas = [".jpg", ".jpeg", ".png"];

function onFormSubmit() {

    var datoslistos = validarDatos();

    if (datoslistos != undefined) {
        
    }


}

function validarDatos() {
    var formDatos = {};
    var mensaje = ""
    var aux = true;
    formDatos[0] = document.getElementById('idcliente').value;
    formDatos[1]= document.getElementById('idempleado').value;
    formDatos[2] = document.getElementById('monto').value;
    formDatos[3] = document.getElementById('SemanasPlazo').value;
    formDatos[5] = document.getElementById('Fch_Inicio').value;
    formDatos[6] = document.getElementById('Fch_Limite').value;
    formDatos[7] = document.getElementById('entregaC').value;
   



    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if (formDatos[key] == "") { //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Varios campos estan vacios."
            aux = false;
            break;
        }
    }



    if(formDatos[2]<=9999){
        mensaje=mensaje+" El monto debe ser mayor a 10000"
        aux=false;
    }

    if(!validarMonto(formDatos[2])){
        mensaje=mensaje+" El monto ingresado no es valido"
        aux=false;
    }


    if (aux) {
        document.getElementById("enviar").style.display="block";
        document.getElementById("comprobar").style.display="none";
        return formDatos;

    }
    else {
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
                modal.find('.modal-body').text("Solo se permiten archivos con extenciones: jpg,png,jpeg.")
                modal.modal('show')
                oninput.value = "";
                return false;
            }
        }
    }
    return true;
}


function validarCredito(ID_Credito) {
    var regex = /^\d{4}/
    var response = regex.test(ID_Credito)
    return response;
}

function validarMonto(Monto) {
    var regex = /^\d[0-9]+/
    var response = regex.test(Monto)
    return response;
}

function validarCURP(valor){                                                                
    var regex = /^[A-Z]{4}\d{6}\w{8}/                                                     
    var reponse = regex.test(valor)                                 
    return reponse;                                                                        
}  

function Limpiar(){
    document.getElementById('ID_Credito').value="";
    document.getElementById('Monto_pres').value="";
    document.getElementById('SemanasPlazo').value="";
    document.getElementById('Fch_Inicio').value="";
    document.getElementById('Fch_Limite').value="";
}








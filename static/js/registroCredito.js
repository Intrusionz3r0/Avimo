var extValidas = [".jpg", ".jpeg", ".png"];

function onFormSubmit() {

    var datoslistos = validarDatos();

    if (datoslistos != undefined) {
        alert("Los datos estan listos para ser enviados a la base de datos.")
        Limpiar();
    }


}

function validarDatos() {
    var formDatos = {};
    var mensaje = ""
    var aux = true;
    formDatos[0] = document.getElementById('ID_Credito').value;
    formDatos[1] = document.getElementById('Monto_pres').value;
    formDatos[2] = document.getElementById('SemanasPlazo').value;
    formDatos[3] = document.getElementById('Fch_Inicio').value;
    formDatos[4] = document.getElementById('Fch_Limite').value;



    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if (formDatos[key] == "") { //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Varios campos estan vacios. Favor de ingresar los datos:"
            aux = false;
            break;
        }
    }

    if(!validarCredito(formDatos[0])){
        mensaje=mensaje+" *El ID de Crédito no es valido"
        aux=false;
    }

    if(!validarMonto(formDatos[1])){
        mensaje=mensaje+" *El monto ingresado no es valido"
    }


    if (aux) {
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
    var regex = /^\d+/
    var response = regex.test(Monto)
    return response;
}

function Limpiar(){
    document.getElementById('ID_Credito').value="";
    document.getElementById('Monto_pres').value="";
    document.getElementById('SemanasPlazo').value="";
    document.getElementById('Fch_Inicio').value="";
    document.getElementById('Fch_Limite').value="";
}








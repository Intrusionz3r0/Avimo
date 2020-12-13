function onFormSubmit() {
    var datoslistos = validarConsultaEmpleado();
    if (datoslistos != undefined) {
        alert("ID Valido,Iniciando Consulta");
        Limpiar();
    }
}

function validarConsultaEmpleado() {
    var formDatos={};
    var mensaje="";
    var aux=true;

    formDatos[0]=document.getElementById("ID_Empleado").value;

    for (const key in formDatos) {
        if (formDatos[key] == "") {
          mensaje = mensaje + "Datos faltantes : "
          aux = false;
          break;
        }
    }

    if(!validarEmpleado(formDatos[0])){
        mensaje=mensaje + " *El ID de Empleado no es valido"
        aux=false;
    }

    if (aux) {
        return formDatos;
      } else {
        var modal = $('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
      }


}

function validarEmpleado(ID_Emp){
    var regex = /^\d{4}/
  var response = regex.test(ID_Emp)
  return response;
}

function Limpiar(){
  document.getElementById("ID_Empleado").value="";
}
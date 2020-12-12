function onFormSubmit() {
  var datoslistos = validarConsultaCredito();
  if (datoslistos != undefined) {
    alert("ID valido,Iniciando Consulta");
    Limpiar();
  }
}

function validarConsultaCredito() {
  var formDatos = {};
  var mensaje = "";
  var aux = true;
  formDatos[0] = document.getElementById("ID_Credito").value;

  for (const key in formDatos) {
    if (formDatos[key] == "") {
      mensaje = mensaje + "Datos faltantes"
      aux = false;
      break;
    }
  }

  if (!validarCredito(formDatos[0])) {
    mensaje = mensaje + " *El ID de Credito no es valido"
    aux = false;
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

function validarCredito(ID_Cre) {
  var regex = /^\d{4}/
  var response = regex.test(ID_Cre)
  return response;
}

function Limpiar(){
  document.getElementById("ID_Credito").value="";
}
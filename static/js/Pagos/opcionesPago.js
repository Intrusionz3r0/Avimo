function onFormSubmit() {
    var datoslistos = validarDatosPago();
    if (datoslistos != undefined) {
      alert("ID valido,Iniciando Consulta");
      Limpiar();
    }
  }

  function validarDatosPago(){
    var formDatos = {};
    var mensaje = "";
    var aux = true;
    formDatos[0] = document.getElementById("ID_Cliente").value;

    for (const key in formDatos) {
      if (formDatos[key] == "") {
        mensaje = mensaje + "Datos faltantes : "
        aux = false;
        break;
      }
    }
    
    if (!validarCliente(formDatos[0])) {
      mensaje = mensaje + " *El ID de Cliente no es valido"
      aux=false;
    }
    
    if (aux) {
      return formDatos;
    } else {
      var modal=$('#errorModal')
      modal.find('.modal-title').text("Error")
      modal.find('.modal-body').text(mensaje)
      modal.modal('show')
    }
  }

  function validarCliente(ID_Cli) {
    var regex = /^\d{4}/
    var response = regex.test(ID_Cli)
    return response;
  }

  function Limpiar(){
    document.getElementById("ID_Cliente").value="";
  }

  
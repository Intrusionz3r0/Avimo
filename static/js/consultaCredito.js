function onFormSubmit() {
    var datoslistos = validarConsultaDatos();
    if (datoslistos != undefined) {
      alert("ID valido");
    }
  }

  function validarConsultaDatos(){
    var formDatos = {};
    var mensaje = "";
    var aux = true;
    formDatos[0] = document.getElementById("btnGroupAddon").value;

    for (const key in formDatos) {
      if (formDatos[key] == "") {
        mensaje = mensaje + "Algunos campos estan vacios : "
        aux = false;
        break;
      }
    }
    
    if(!isNaN(formDatos[0])){


    }
    else{
        aux=false;
        mensaje=mensaje +", ID es invalido deben ser  numeros"
    }
    if(aux ){
        return formDatos;

    }
    else{
        alert(mensaje)
    
        
    }
    
  }

  function validarID(valor) {
    var regex = /^\d{4}/
    var response = regex.test(valor)
    return response;
  }
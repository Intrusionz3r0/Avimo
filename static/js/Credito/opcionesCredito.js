
 function onFormSubmit() {

    var datoslistos = validarDatos();

    if(datoslistos != undefined){
        alert("ID Credito Valido,Iniciando Consulta.")
        Limpiar();
    }


}

function validarDatos(){
    var formDatos = {};
    var mensaje = ""
    var aux = true;
    formDatos[0] = document.getElementById('ID_Credito').value
    
    

    for (const key in formDatos) { //Recorre todo los campos del formulario.

        if(formDatos[key] == ""){ //Verifica si los campos estan vacios y si es así devuelve un error y en la variable aux devuelve un false.
            mensaje = mensaje + "Varios campos estan vacios. Favor de ingresar los datos"
            aux =false;
            break;
        }
    }
    if (!validarID_Credito(formDatos[0])){
      mensaje = mensaje + " *El ID de Credito no es valido"
      aux=false;
    }
    
    
   
  if(aux ){
        return formDatos;

    }
    else{
        var modal=$('#errorModal')
        modal.find('.modal-title').text("Error")
        modal.find('.modal-body').text(mensaje)
        modal.modal('show')
    }
    
}


    function validarID_Credito(valor){                  
        var regex = /^\d{4}/                                                   
        var response = regex.test(valor)                                                           
        return response;                                                                        
}

function Limpiar(){
    document.getElementById("ID_Credito").value="";
}


function getCredito(){
    id=document.getElementById("clavesita").value;
    location.href="/consultaindividual/"+id;
}
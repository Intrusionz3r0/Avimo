function deleteCliente(){
  var clave = document.getElementById("clavesita").value
  location.href="/clientes/opcionesCliente/eliminar/"+clave
}


function modificarCliente(){
  var clave = document.getElementById("clavesita").value
  location.href="/clientes/opcionesCliente/"+clave
}


function getCliente(){
  var id = document.getElementById("clavesita").value
  location.href="/clientes/opcionesCliente/clave/"+id

}







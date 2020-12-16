function getValue(){
  id=document.getElementById("clavesita").value;
  location.href="/Pago/registraPago/"+id;
}

function getModi(){
  id=document.getElementById("clavesita").value;
  location.href="/Pago/consultarmispagos/"+id
}
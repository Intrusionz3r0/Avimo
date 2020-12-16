import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Clientes,Avales,Empleados,Credito,Pagos
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "4V1M0S3CR3TKEY"



 
#Configuración SqlAlchemy Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/AVIMO'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
print(app.config['UPLOADED_PHOTOS_DEST'])
 
db = SQLAlchemy(app)

@app.route('/Login')
def Login():
    return render_template('Login.html')

@app.route('/CerrarSesion')
def CerrarSesion():
    return redirect(url_for("Login"))

#Comienzo del CRUD de Clientes y Avales.

@app.route('/clientes/registrocliente')
def ventanaCliente():
    return render_template('Clientes/registroClientes.html')

@app.route('/clientes/registrocliente/nuevo',methods=['POST'])
def agregarCliente():
    cliente=Clientes()
    cliente.Nombre = request.form['nombreCliente']
    cliente.Apellidos = request.form['apellidoCliente']
    cliente.Genero = request.form['generoCliente']
    cliente.Estado = request.form['estadoCliente']
    cliente.Municipio = request.form['municipioCliente']
    cliente.Colonia = request.form['coloniaCliente']
    cliente.CallePrincipal = request.form['calleCliente']
    cliente.NumInterior = request.form['ninternoCliente']
    cliente.NumExterior = request.form['nexternoCliente']
    cliente.EntreCalles = request.form['entrecallesCliente']
    cliente.Telefono = request.form['telefonoCliente']
    cliente.CURP = request.form['curpCliente']
    cliente.Clave = cliente.CURP[:10]+cliente.CURP[-3:]
    cliente.Fecha_Nacimiento = request.form['fnacimientoCliente']
    cliente.Fecha_Registro = request.form['fregistroCliente']
    cliente.Estatus = "Activo"
    cliente.insertar()
    #cliente.FotoINE_Delantera =request.files['file1Cliente']
    #cliente.FotoINE_Trasera =request.files['file1Cliente']
    #cliente.FotoCliente =request.files['file1Cliente']
    #cliente.Comprobante_Domicilio =request.files['file1Cliente']
    
    aval=Avales()
    aval.Clave = cliente.CURP[:10]+cliente.CURP[-3:]
    aval.Nombre = request.form['nombreAval']
    aval.Apellidos = request.form['apellidoAval']
    aval.Estado = request.form['estadoAval']
    aval.Municipio = request.form['municipioAval']
    aval.Colonia = request.form['coloniaAval']
    aval.CallePrincipal = request.form['calleAval']
    aval.NumInterior = request.form['ninternoAval']
    aval.NumExterior = request.form['nexternoAval']
    aval.EntreCalles = request.form['entrecallesAval']
    aval.Telefono = request.form['telefonoAval']
    #aval.FotoINE_Delantera = request.form['file1Aval']
    #aval.FotoINE_Trasera = request.form['file2aval']
    #aval.Comprobante_Domicilio = request.form['file3Aval']
    aval.insertar()


    return redirect(url_for('ventanaCliente'))

@app.route("/clientes/opcionesCliente/")
def ventanaConsultaCliente():
    cliente=Clientes()
    cliente=cliente.consultaGeneral()

    aval=Avales()
    aval=aval.consultaGeneral()

    return render_template("Clientes/opcionesCliente.html",cliente=cliente,aval=aval)

@app.route("/clientes/opcionesCliente/<int:id>")
def obtenerDatosClienteAval(id):
    
    aval=Avales()
    aval.ID_Aval=id
    aval=aval.consultaIndividual()
    
    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente=cliente.consultaIndividual()

    return render_template("Clientes/consultaCliente.html",cliente=cliente,aval=aval)

@app.route("/clientes/opcionesCliente/eliminar/<int:id>")
def eliminarClienteAval(id):

    aval=Avales()
    aval.ID_Aval=id
    aval.eliminar()

    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente.eliminar()

    return redirect(url_for("ventanaConsultaCliente"))

@app.route("/opcionesCliente/modificar/<int:id>")
def modificarClienteAval(id):
    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente=cliente.consultaIndividual()

    aval=Avales()
    aval.ID_Aval=id
    aval=aval.consultaIndividual()

    return render_template("Clientes/modificarCliente.html",cliente=cliente,aval=aval)

@app.route("/opcionesCliente/actualizar/",methods=['POST'])
def actualizarDatos():
    cliente=Clientes()
    cliente.ID_Cliente=request.form['idCliente']
    cliente.Nombre = request.form['nombreCliente']
    cliente.Apellidos = request.form['apellidoCliente']
    cliente.Genero = request.form['generoCliente']
    cliente.Estado = request.form['estadoCliente']
    cliente.Municipio = request.form['municipioCliente']
    cliente.Colonia = request.form['coloniaCliente']
    cliente.CallePrincipal = request.form['calleCliente']
    cliente.NumInterior = request.form['ninternoCliente']
    cliente.NumExterior = request.form['nexternoCliente']
    cliente.EntreCalles = request.form['entrecallesCliente']
    cliente.Telefono = request.form['telefonoCliente']
    cliente.CURP = request.form['curpCliente']
    cliente.Clave = cliente.CURP[:10]+cliente.CURP[-3:]
    cliente.Fecha_Nacimiento = request.form['fnacimientoCliente']
    cliente.Fecha_Registro = request.form['fregistroCliente']
    cliente.Estatus = request.form['estatusCliente']
    cliente.actualizar()

    aval=Avales()
    aval.ID_Aval=request.form['idAval']
    aval.Clave = cliente.CURP[:10]+cliente.CURP[-3:]
    aval.Nombre = request.form['nombreAval']
    aval.Apellidos = request.form['apellidoAval']
    aval.Estado = request.form['estadoAval']
    aval.Municipio = request.form['municipioAval']
    aval.Colonia = request.form['coloniaAval']
    aval.CallePrincipal = request.form['calleAval']
    aval.NumInterior = request.form['ninternoAval']
    aval.NumExterior = request.form['nexternoAval']
    aval.EntreCalles = request.form['entrecallesAval']
    aval.Telefono = request.form['telefonoAval']
    #aval.FotoINE_Delantera = request.form['file1Aval']
    #aval.FotoINE_Trasera = request.form['file2aval']
    #aval.Comprobante_Domicilio = request.form['file3Aval']
    aval.actualizar()

    aval=Avales()
    return redirect(url_for("ventanaConsultaCliente"))


#Comienzo de CRUD de Empleados.
@app.route("/empleados/registroempleado/")
def ventanaRegistroEmpleados():    
    return render_template("Empleados/registroEmpleado.html")

@app.route('/empleados/registroempleado/nuevo',methods=['POST'])
def registrarEmpleado():
    empleado=Empleados()
    empleado.Nombre=request.form['NombreEmp']
    empleado.Apellidos=request.form['ApellidosEmp']
    empleado.Sexo=request.form['generoEmp']
    empleado.Estado=request.form['estadoEmp']
    empleado.Municipio=request.form['municipioEmp']
    empleado.Colonia=request.form['coloniaEmp']
    empleado.CallePrincipal=request.form['calleEmp']
    empleado.NumInterior=request.form['ninternoEmp']
    empleado.NumExterior=request.form['nexternoEmp']
    empleado.EntreCalles=request.form['entrecallesEmp']
    empleado.Telefono=request.form['telefonoEmp']
    empleado.CURP=request.form['curpEmp']
    empleado.Fecha_Nacimiento=request.form['fnacimientoEmp']
    empleado.Fecha_Contratacion=request.form['fingresoEmp']
    empleado.Estatus="Activo"
    #empleado.Foto_Empleado=request.files['fotoempe']
    #empleado.FotoINE_Delantera=request.files['file1']
    #empleado.FotoINE_Trasera=request.files['file1']
    #empleado.Comprobante_Domicilio=request.files['ComproDomi']
    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    empleado.Rol=request.form['Rol']
    
    empleado.insertar()

    return redirect(url_for('ventanaRegistroEmpleados'))

@app.route("/opcionesEmpleado/")
def ventanaConsultaEmpleado():
    empleado=Empleados()
    empleado=empleado.consultaGeneral()

    return render_template("Empleados/opcionesEmpleado.html",empleado=empleado)

@app.route("/opcionesEmpleado/<int:id>")
def consultarEmpleadoIn(id):
    empleado=Empleados()
    empleado.ID_Empleado=id
    empleado=empleado.consultaIndividual()
    
    return render_template("Empleados/consultaEmpleado.html",empleado=empleado)

@app.route("/opcionesEmpleado/eliminar/<int:id>")
def eliminarEmpleado(id):
    empleado=Empleados()
    empleado.ID_Empleado=id
    empleado=empleado.eliminar()

    return redirect(url_for('ventanaConsultaEmpleado'))

@app.route("/opcionesEmpleado/modificar/<int:id>")
def modificarDatosEmpleado(id):
    empleado=Empleados()
    empleado.ID_Empleado=id
    empleado=empleado.consultaIndividual()
    
    return render_template("Empleados/modificarEmpleado.html",empleado=empleado)

@app.route("/opcionesEmpleado/actualizar/",methods=['POST'])
def actualizarDatosEmpleado():
    empleado=Empleados()
    empleado.ID_Empleado=request.form['idEmpleado']
    empleado.Nombre=request.form['NombreEmp']
    empleado.Apellidos=request.form['ApellidosEmp']
    empleado.Sexo=request.form['generoEmp']
    empleado.Estado=request.form['estadoEmp']
    empleado.Municipio=request.form['municipioEmp']
    empleado.Colonia=request.form['coloniaEmp']
    empleado.CallePrincipal=request.form['calleEmp']
    empleado.NumInterior=request.form['ninternoEmp']
    empleado.NumExterior=request.form['nexternoEmp']
    empleado.EntreCalles=request.form['entrecallesEmp']
    empleado.Telefono=request.form['telefonoEmp']
    empleado.CURP=request.form['curpEmp']
    empleado.Fecha_Nacimiento=request.form['fnacimientoEmp']
    empleado.Fecha_Contratacion=request.form['fingresoEmp']
    empleado.Estatus=request.form['estatusAval']
    #empleado.Foto_Empleado=request.files['fotoempe']
    #empleado.FotoINE_Delantera=request.files['file1']
    #empleado.FotoINE_Trasera=request.files['file1']
    #empleado.Comprobante_Domicilio=request.files['ComproDomi']
    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    pass2=request.form['Contraseña']
    empleado.Rol=request.form['Rol']
    
    if(empleado.Contraseña==pass2):
        empleado.actualizar()
    
    return redirect(url_for('ventanaRegistroEmpleados'))

#CRUD de Creditos.

@app.route("/credito/registraCredito")
def ventanaCredito():
    return render_template("Credito/registroCredito.html")

@app.route("/credito/registrarCredito/new",methods=['POST'])
def registrarCredito():
    credito=Credito()
    credito.Cliente=request.form['idempleado']
    credito.Empleado_Responsable=request.form['idempleado']
    credito.MontoPrestado=request.form['monto']
    credito.MontoPagar=request.form['monto']
    credito.Semanas=request.form['SemanasPlazo']
    credito.Fecha_Inicio=request.form['Fch_Inicio']
    credito.Fecha_Limite=request.form['Fch_Limite']
    credito.Estatus="Activo"
    #credito.Foto_EntregaCredito=request.files['file']
    credito.insertar()
    return redirect(url_for("consultaCreditoGeneral"))

@app.route("/consultaindividual/<int:id>")
def consultaindividualCredito(id):

    credito=Credito()
    credito.ID_Credito=id
    credito=credito.consultaIndividual()

    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente=cliente.consultaIndividual()
    
    return render_template("Credito/consultaCredito.html",credito=credito,cliente=cliente)


@app.route("/credito/opcionesCredito")
def consultaCreditoGeneral():
    credito=Credito()
    credito=credito.consultaGeneral()
    
    return render_template("Credito/opcionesCredito.html",credito=credito)

@app.route("/credito/eliminarCredito/<int:id>")
def eliminarCredito(id):

    credito=Credito()
    credito.ID_Credito=id
    credito.eliminar()

    return redirect(url_for('consultaCreditoGeneral'))

@app.route("/modificarCredito/<int:id>")
def modificarCredito(id):

    credito=Credito()
    credito.ID_Credito=id
    credito=credito.consultaIndividual()

    return render_template("Credito/modificarCredito.html",credito=credito)

@app.route("/actualizarCredito/nuevo",methods=['POST'])
def actualizar():

    credito=Credito()
    
    credito.ID_Credito=request.form['idcredito']
    credito.Cliente=request.form['idempleado']
    credito.Empleado_Responsable=request.form['idempleado']
    credito.MontoPrestado=request.form['monto']
    credito.Semanas=request.form['SemanasPlazo']
    credito.Fecha_Inicio=request.form['Fch_Inicio']
    credito.Fecha_Limite=request.form['Fch_Limite']
    credito.Estatus="Deuda"
    #credito.Foto_EntregaCredito=request.files['file']
    credito.actualizar()
    return redirect(url_for("consultaCreditoGeneral"))


#Crud de Pagos.


@app.route("/Pago/registraPago/<int:id>")
def ventanaRegistraPago(id):
    credito=Credito()
    credito.ID_Credito=id
    credito=credito.consultaIndividual()

    return render_template("Pagos/registroPago.html",credito=credito)


@app.route("/Pago/RegistraPago/nuevo",methods=['POST'])
def registrarPago():
    pago=Pagos()
    pago.Credito=request.form['ID_Cliente']
    pago.Cliente=request.form['ID_Credito']
    pago.Monto=request.form['Monto']
    pago.Semana=request.form['Semanas']
    pago.Fecha_Pago=request.form['Fch_Pago']
    #pago.Foto_Comprobante=request.files['F_Comprobante']
    pago.insertar()

    credito=Credito()
    credito.ID_Credito=request.form['ID_Credito']
    credito.MontoPagar=request.form['Total']
    credito.MontoPagar=int(credito.MontoPagar)-int(pago.Monto)

    if(credito.MontoPagar<=0):
        credito.Estatus="Saldado"
        credito.MontoPagar=0
    credito.actualizar()


    return redirect(url_for('consultaPagos'))


@app.route("/Pago/ConsultaPagos")
def consultaPagos():
    return render_template("Pagos/opcionesPago.html")


@app.route("/Pago/consultarmispagos/<int:id>")
def consultaPagosIn(id):

    pagos=Pagos()
    pagos.ID_pagos=id
    pagos=pagos.consultaGeneral()

    return render_template("Pagos/consultaPago.html",pagos=pagos)




if __name__ == "__main__":
    
    app.run(port = 3000, debug = True)

import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Clientes,Avales,Empleados
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "4V1M0S3CR3TKEY"



 
#Configuración SqlAlchemy Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/AVIMO'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
print(app.config['UPLOADED_PHOTOS_DEST'])
 
db = SQLAlchemy(app)


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
    if(cliente.Genero == "Masculino"):
        cliente.Genero="M"
    elif(cliente.Genero == "Femenino"):
        cliente.Genero="F"
    elif(cliente.Genero == "Otro"):
        cliente.Genero="O"
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
    cliente.Estatus = "A"
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
    if(cliente.Genero == "Masculino" or cliente.Genero == "M"):
        cliente.Genero="M"
    elif(cliente.Genero == "Femenino" or cliente.Genero == "F"):
        cliente.Genero="F"
    elif(cliente.Genero == "Otro" or cliente.Genero == "O"):
        cliente.Genero="O"
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
    if(cliente.Estatus == "Activo" or cliente.Estatus == "A"):
        cliente.Estatus="A"
    elif(cliente.Estatus == "Inactivo" or cliente.Estatus == "I"):
        cliente.Estatus="I"
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
    if(empleado.Sexo == "Masculino"):
        empleado.Sexo="M"
    elif(empleado.Sexo == "Femenino"):
        empleado.Sexo="F"
    elif(empleado.Sexo == "Otro"):
        empleado.Sexo="O"
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
    empleado.Estatus="A"
    #empleado.Foto_Empleado=request.files['fotoempe']
    #empleado.FotoINE_Delantera=request.files['file1']
    #empleado.FotoINE_Trasera=request.files['file1']
    #empleado.Comprobante_Domicilio=request.files['ComproDomi']
    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    empleado.Rol=request.form['Rol']
    
    if(empleado.Rol == "Jefe/Subjefe"):
        empleado.Rol="J"
    
    elif(empleado.Rol == "Administrador"):
        empleado.Rol="A"
    
    elif(empleado.Rol == "Asesor de Crédito"):
        empleado.Rol="C"
    
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
    if(empleado.Sexo == "Masculino" or empleado.Sexo == "M"):
        empleado.Sexo="M"
    elif(empleado.Sexo == "Femenino" or empleado.Sexo == "F"):
        empleado.Sexo="F"
    elif(empleado.Sexo == "Otro" or empleado.Sexo == "O"):
        empleado.Sexo="O"
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
    if(empleado.Estatus=="Activo" or empleado.Estatus=="A"):
        empleado.Estatus="A"
    elif(empleado.Estatus=="Inactivo" or empleado.Estatus=="I"):
        empleado.Estatus="I"
    #empleado.Foto_Empleado=request.files['fotoempe']
    #empleado.FotoINE_Delantera=request.files['file1']
    #empleado.FotoINE_Trasera=request.files['file1']
    #empleado.Comprobante_Domicilio=request.files['ComproDomi']
    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    pass2=request.form['Contraseña']
    empleado.Rol=request.form['Rol']
    
    if(empleado.Rol == "Jefe/Subjefe" or empleado.Rol == "J"):
        empleado.Rol="J"
    
    elif(empleado.Rol == "Administrador" or empleado.Rol == "A"):
        empleado.Rol="A"
    
    elif(empleado.Rol == "Asesor de Crédito" or empleado.Rol == "C"):
        empleado.Rol="C"
    
    if(empleado.Contraseña==pass2):
        empleado.actualizar()
    

    return redirect(url_for('ventanaRegistroEmpleados'))

if __name__ == "__main__":
    
    app.run(port = 3000, debug = True)

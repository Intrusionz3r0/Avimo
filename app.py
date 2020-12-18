import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Clientes,Avales,Empleados,Credito,Pagos
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = "4V1M0S3CR3TKEY"


#Configuración SqlAlchemy Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/AVIMO'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/uploads/"
loginManager=LoginManager()
loginManager.init_app(app)
loginManager.login_view="ventanaCliente"
db = SQLAlchemy(app)



@loginManager.user_loader
def load_user(id):
    return Empleados.query.get(int(id))

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route("/CerrarSesion")
def cerrarSes():
    if(current_user.is_authenticated):
         logout_user()
         return redirect(url_for("ventanaCliente"))
    else:
        abort(404)

@app.route("/login",methods=['POST'])
def iniciarSesion():
    Em=Empleados()
    Em=Em.validar(request.form['user'],request.form['pass'])
    if(Em!=None):
        print(Em.getTipo())
        login_user(Em)
        return render_template("Clientes/registroClientes.html")
    else:
        return "El usuario o la contraseña es invalido"
    
    
        
#Comienzo del CRUD de Clientes y Avales.

@app.route('/clientes/registrocliente')
def ventanaCliente():
    if( current_user.is_authenticated):
        return render_template('Clientes/registroClientes.html')
    else:
        return render_template("Login.html")


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
    
    if not os.path.isdir("static/uploads/"+cliente.Clave):
        os.mkdir("static/uploads/"+cliente.Clave)
        os.mkdir("static/uploads/"+cliente.Clave+"/Clientes")
        os.mkdir("static/uploads/"+cliente.Clave+"/Avales")
    ine1 = request.files['file1Cliente']
    ine2 = request.files['file2Cliente']
    fotocliente = request.files['file3Cliente']
    comprobante = request.files['file4Cliente']

    filename1 = secure_filename(ine1.filename)
    filename2 = secure_filename(ine2.filename)
    filename3 = secure_filename(fotocliente.filename)
    filename4 = secure_filename(comprobante.filename)
    
    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Clientes", ine1.filename)
    ine1.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Clientes", ine2.filename)
    ine2.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Clientes", fotocliente.filename)
    fotocliente.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Clientes", comprobante.filename)
    comprobante.save(path)
    
    cliente.FotoINE_Delantera = filename1
    cliente.FotoINE_Trasera = filename2
    cliente.FotoCliente = filename3
    cliente.Comprobante_Domicilio = filename4

    cliente.insertar()
    
    
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


    ine1a = request.files['file1Aval']
    ine2a = request.files['file2aval']
    comprobantea = request.files['file3Aval']

    filename1 = secure_filename(ine1a.filename)
    filename2 = secure_filename(ine2a.filename)
    filename3 = secure_filename(comprobantea.filename)
    
    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Avales", ine1a.filename)
    ine1a.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Avales", ine2a.filename)
    ine2a.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+cliente.Clave+"/Avales", comprobantea.filename)
    comprobantea.save(path)
    
    aval.FotoINE_Delantera = filename1
    aval.FotoINE_Trasera = filename2
    aval.Comprobante_Domicilio = filename3
    
    aval.insertar()


    return redirect(url_for('ventanaCliente'))


@app.route("/clientes/opcionesCliente/")
@login_required
def ventanaConsultaCliente():
    cliente=Clientes()
    cliente=cliente.consultaGeneral()

    aval=Avales()
    aval=aval.consultaGeneral()

    return render_template("Clientes/opcionesCliente.html",cliente=cliente,aval=aval)

@app.route("/clientes/opcionesCliente/<int:id>")
@login_required
def obtenerDatosClienteAval(id):
    
    aval=Avales()
    aval.ID_Aval=id
    aval=aval.consultaIndividual()
    
    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente=cliente.consultaIndividual()

    return render_template("Clientes/consultaCliente.html",cliente=cliente,aval=aval)

@app.route("/opcionesCliente/clave/<string:clave>")
@login_required
def obtenerDatosClienteAvalC(clave):
    
    aval=Avales()
    aval.Clave=clave
    aval=aval.consultaIndividualClave()
    
    cliente=Clientes()
    cliente.Clave=clave
    cliente=cliente.consultaIndividualClave()

    

    return render_template("Clientes/consultaClienteV2.html",cliente=cliente,aval=aval)

@app.route("/clientes/opcionesCliente/eliminar/<int:id>")
@login_required
def eliminarClienteAval(id):

    aval=Avales()
    aval.ID_Aval=id
    aval.eliminar()

    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente.eliminar()

    return redirect(url_for("ventanaConsultaCliente"))

@app.route("/opcionesCliente/modificar/<int:id>")
@login_required
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

    aval.actualizar()

    aval=Avales()
    return redirect(url_for("ventanaConsultaCliente"))


#Comienzo de CRUD de Empleados.
@app.route("/empleados/registroempleado/")
@login_required
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
    empleado.Clave=empleado.CURP[:10]+empleado.CURP[-3:]

    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    empleado.Rol=request.form['Rol']
    

    os.mkdir("static/uploads/"+empleado.Clave)
    ine1 = request.files['fine1']
    ine2 = request.files['fine2']
    fotoempleado = request.files['fotoempe']
    comprobante = request.files['ComproDomi']

    filename1 = secure_filename(ine1.filename)
    filename2 = secure_filename(ine2.filename)
    filename3 = secure_filename(fotoempleado.filename)
    filename4 = secure_filename(comprobante.filename)
    
    path = os.path.join(app.config['UPLOAD_FOLDER']+empleado.Clave, ine1.filename)
    ine1.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+empleado.Clave, ine2.filename)
    ine2.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+empleado.Clave, fotoempleado.filename)
    fotoempleado.save(path)

    path = os.path.join(app.config['UPLOAD_FOLDER']+empleado.Clave, comprobante.filename)
    comprobante.save(path)
    
    empleado.FotoINE_Delantera = filename1
    empleado.FotoINE_Trasera = filename2
    empleado.Foto_Empleado = filename3
    empleado.Comprobante_Domicilio = filename4


    empleado.insertar()

    return redirect(url_for('ventanaRegistroEmpleados'))

@app.route("/opcionesEmpleado/")
@login_required
def ventanaConsultaEmpleado():
    empleado=Empleados()
    empleado=empleado.consultaGeneral()

    return render_template("Empleados/opcionesEmpleado.html",empleado=empleado)

#@app.route("/opcionesEmpleado/<int:id>")
#def consultarEmpleadoIn(id):
#    empleado=Empleados()
    #empleado.ID_Empleado=id
    #empleado=empleado.consultaIndividual()
#    
#    return render_template("Empleados/consultaEmpleado.html",empleado=empleado)

@app.route("/opcionesEmpleado/<string:clave>")
@login_required
def consultarEmpleadoInC(clave):
    empleado=Empleados()
    empleado.Clave=clave
    empleado=empleado.consultaIndividualClave()
    
    return render_template("Empleados/consultaEmpleadoV2.html",empleado=empleado)

@app.route("/opcionesEmpleado/eliminar/<int:id>")
def eliminarEmpleado(id):
    empleado=Empleados()
    empleado.ID_Empleado=id
    empleado=empleado.eliminar()

    return redirect(url_for('ventanaConsultaEmpleado'))

@app.route("/opcionesEmpleado/modificar/<int:id>")
@login_required
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
    empleado.Usuario=request.form['Usuario']
    empleado.Contraseña=request.form['Contraseña2']
    pass2=request.form['Contraseña']
    empleado.Rol=request.form['Rol']
    
    if(empleado.Contraseña==pass2):
        empleado.actualizar()
    
    return redirect(url_for('ventanaConsultaEmpleado'))

#CRUD de Creditos.

@app.route("/credito/registraCredito")
@login_required
def ventanaCredito():
    return render_template("Credito/registroCredito.html")

@app.route("/credito/registrarCredito/new",methods=['POST'])
def registrarCredito():
    credito=Credito()
    credito.Clave=request.form['idcliente']
    
    credito.Empleado_Responsable=request.form['idempleado']
    credito.MontoPrestado=request.form['monto']
    credito.MontoPagar=request.form['monto']
    credito.Semanas=request.form['SemanasPlazo']
    credito.Fecha_Inicio=request.form['Fch_Inicio']
    credito.Fecha_Limite=request.form['Fch_Limite']
    curp = request.form['idcliente']
    credito.Estatus="Deuda"
    
    file1=request.files['entregaC']
    filename1=secure_filename(file1.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+curp, file1.filename)
    
    
    credito.Foto_EntregaCredito=filename1



    credito.insertar()
    file1.save(path)
    return redirect(url_for("consultaCreditoGeneral"))

@app.route("/consultaindividual/<int:id>")
@login_required
def consultaindividualCredito(id):

    credito=Credito()
    credito.ID_Credito=id
    credito=credito.consultaIndividual()

    cliente=Clientes()
    cliente.ID_Cliente=id
    cliente=cliente.consultaIndividual()
    
    return render_template("Credito/consultaCreditoV2.html",credito=credito,cliente=cliente)


@app.route("/credito/opcionesCredito")
@login_required
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
@login_required
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
    credito.MontoPagar=request.form['monto']
    credito.Semanas=request.form['SemanasPlazo']
    credito.Fecha_Inicio=request.form['Fch_Inicio']
    credito.Fecha_Limite=request.form['Fch_Limite']
    credito.Estatus="Deuda"
    #credito.Foto_EntregaCredito=request.files['file']
    credito.actualizar()
    return redirect(url_for("consultaCreditoGeneral"))


#Crud de Pagos.


@app.route("/Pago/registraPago/<int:id>")
@login_required
def ventanaRegistraPago(id):
    credito=Credito()
    credito.ID_Credito=id
    credito=credito.consultaIndividual()

    return render_template("Pagos/registroPago.html",credito=credito)


@app.route("/Pago/RegistraPago/nuevo",methods=['POST'])
def registrarPago():
    pago=Pagos()
    pago.Credito=request.form['ID_Credito']
    pago.Clave=request.form['ID_Cliente']
    pago.Monto=request.form['Monto']
    pago.Semana=request.form['Semanas']
    pago.Fecha_Pago=request.form['Fch_Pago']
    curp = pago.Clave
    
    file1=request.files['F_Comprobante']
    filename1=secure_filename(file1.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER']+curp, file1.filename)
    pago.Foto_Comprobante=filename1
    pago.insertar()
    file1.save(path)

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
@login_required
def consultaPagos():
    pagos=Pagos()
    pagos=pagos.consultaGeneral()
    return render_template("Pagos/opcionesPago.html",pagos=pagos)


@app.route("/consultarmispagos/<int:id>")
@login_required
def consultaPagosIn(id):

    pagos=Pagos()
    pagos.Credito=id
    pagos=pagos.consultaPagosCreditoIndi()

    return render_template("Pagos/consultaPago.html",pagos=pagos)





if __name__ == "__main__":
    
    app.run(port = 3000, debug = True)


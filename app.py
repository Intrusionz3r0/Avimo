import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from modelo.models import Clientes,Avales
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "4V1M0S3CR3TKEY"



 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/AVIMO'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
print(app.config['UPLOADED_PHOTOS_DEST'])
 
db = SQLAlchemy(app)

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

    cliente.insertar()
    aval.insertar()
    return redirect(url_for('ventanaCliente'))



@app.route("/clientes/consultaCliente/")
def consultaCliente():
    return render_template('Clientes/consultaCliente.html')

@app.route("/clientes/consultaCliente/<string:clave>")
def obtenerDatosCliente(clave):

    aval=Avales()
    aval.Clave=clave
    aval=aval.consultaIndividual()

    cliente=Clientes()
    cliente.Clave=clave
    cliente=cliente.consultaIndividual()

    return render_template('Clientes/consultaCliente.html',cliente=cliente,aval=aval)



@app.route("/clientes/opcionesCliente/")
def opcionesCliente():
    return render_template('Clientes/opcionesCliente.html')


@app.route('/clientes/opcionesCliente/eliminar/<string:clave>')
def eliminarCliente(clave):

    aval=Avales()
    aval.Clave=clave
    aval=aval.eliminar()

    cliente=Clientes()
    cliente.Clave=clave
    cliente.eliminar()
    return redirect(url_for('consultaCliente'))
    
@app.route('/clientes/opcionesCliente/<string:clave>')
def obtenerDatosClienteAval(clave):
    aval=Avales()
    aval.Clave=clave
    aval=aval.consultaIndividual()

    cliente=Clientes()
    cliente.Clave=clave
    cliente=cliente.consultaIndividual()

    return render_template('Clientes/modificarCliente.html',cliente=cliente,aval=aval)

@app.route('/clientes/actualizarcliente',methods=['POST'])
def actualizarClienteAval():    
    return redirect(url_for('ventanaCliente'))

if __name__ == "__main__":
    
    app.run(port = 3000, debug = True)

from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'avimo'

mysql = MySQL(app)

@app.route('/clientes')
def registraClientes():
    return render_template('registroClientes.html')


@app.route('/registraCliente',methods=['POST'])
def addClienteAval():
    if request.method == 'POST':

        nombreCliente = request.form['nombreCliente']
        apellidoCliente = request.form['apellidoCliente']
        generoCliente = request.form['generoCliente']
        estadoCliente = request.form['estadoCliente']
        municipioCliente = request.form['municipioCliente']
        coloniaCliente = request.form['coloniaCliente']
        calleCliente = request.form['calleCliente']
        ninternoCliente = request.form['ninternoCliente']
        nexternoCliente = request.form['nexternoCliente']
        entrecallesCliente = request.form['entrecallesCliente']
        telefonoCliente = request.form['telefonoCliente']
        curpCliente = request.form['curpCliente']
        fnacimientoCliente = request.form['fnacimientoCliente']
        fregistroCliente = request.form['fregistroCliente']
        file1Cliente = request.form['file1Cliente']
        file2Cliente = request.form['file2Cliente']
        file3Cliente = request.form['file3Cliente']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (nombre,apellido,genero,estado,municipio,colonia,calle,ninterno,nexterno,entrecalles,telefono,curp,fechanacimiento,fecharegistro,fotoine1,fotoine2,comdomicilio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null,null,null)",(nombreCliente,apellidoCliente,generoCliente,estadoCliente,municipioCliente,coloniaCliente,calleCliente,ninternoCliente,nexternoCliente,entrecallesCliente,telefonoCliente,curpCliente,fnacimientoCliente,fregistroCliente,file1Cliente,file2Cliente,file3Cliente))
        mysql.connection.commit()

        return 'simon'

if __name__ == "__main__":
    app.run(port = 3000, debug = True)

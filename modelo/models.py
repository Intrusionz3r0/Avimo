from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,BLOB
from sqlalchemy.orm import relationship                                                                                                                                                          
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()                                                                                                                                                                                  
                                                                                                                                                                                                 
class Clientes(db.Model):                                                                                                                                                                        
    __tablename__='Clientes'                                                                                                                                                                    
    ID_Cliente=Column(Integer,primary_key=True)
    Clave=Column(String,nullable=False)
    Nombre=Column(String,nullable=False)
    Apellidos=Column(String,nullable=False)
    Genero=Column(String,nullable=False)
    Estado=Column(String,nullable=False)
    Municipio=Column(String,nullable=False)
    Colonia=Column(String,nullable=False)
    CallePrincipal=Column(String,nullable=False)
    NumInterior=Column(Integer,nullable=False)
    NumExterior=Column(Integer,nullable=False)
    EntreCalles=Column(String,nullable=False)
    Telefono=Column(String,nullable=False)
    CURP=Column(String,nullable=False)
    Fecha_Nacimiento=Column(Date,nullable=False)
    Fecha_Registro=Column(Date,nullable=False)
    Estatus=Column(String,nullable=False)
    FotoINE_Delantera=Column(String,nullable=False)
    FotoINE_Trasera=Column(String,nullable=False)
    FotoCliente=Column(String,nullable=False)
    Comprobante_Domicilio=Column(String,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        cliente=self.query.all()                                                                                                                                                                   
        return cliente
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        cli=self.consultaIndividual()
        db.session.delete(cli)
        db.session.commit()
    def consultaIndividual(self):
        cliente=self.query.get(self.ID_Cliente)
        return cliente
    def consultaIndividualClave(self):
        cliente=self.query.filter_by(Clave=self.Clave).first()
        return cliente



class Avales(db.Model):                                                                                                                                                                        
    __tablename__='Avales'
    ID_Aval=Column(Integer,primary_key=True)
    Clave=Column(String,nullable=False)
    Nombre=Column(String,nullable=False)
    Apellidos=Column(String,nullable=False)
    Estado=Column(String,nullable=False)
    Municipio=Column(String,nullable=False)
    Colonia=Column(String,nullable=False)
    CallePrincipal=Column(String,nullable=False)
    NumInterior=Column(Integer,nullable=False)
    NumExterior=Column(Integer,nullable=False)
    EntreCalles=Column(String,nullable=False)
    Telefono=Column(String,nullable=False)
    FotoINE_Delantera=Column(String,nullable=False)
    FotoINE_Trasera=Column(String,nullable=False)
    Comprobante_Domicilio=Column(String,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        aval=self.query.all()                                                                                                                                                                   
        return aval
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        cli=self.consultaIndividual()
        db.session.delete(cli)
        db.session.commit()
    def consultaIndividual(self):
        aval=self.query.get(self.ID_Aval)
        return aval
    def consultaIndividualClave(self):
        aval=self.query.filter_by(Clave=self.Clave).first()
        return aval

class Empleados(db.Model):
    __tablename__='Empleados'
    ID_Empleado=Column(Integer,primary_key=True)
    Clave=Column(String,nullable=False)
    Nombre=Column(String,nullable=False)
    Apellidos=Column(String,nullable=False)
    Sexo=Column(String,nullable=False)
    Telefono=Column(String,nullable=False)
    Estado=Column(String,nullable=False)
    Municipio=Column(String,nullable=False)
    Colonia=Column(String,nullable=False)
    CallePrincipal=Column(String,nullable=False)
    EntreCalles=Column(Integer,nullable=False)
    NumExterior=Column(Integer,nullable=False)
    NumInterior=Column(String,nullable=False)
    CURP=Column(String,nullable=False)
    Fecha_Nacimiento=Column(Date,nullable=False)
    Fecha_Contratacion=Column(Date,nullable=False)
    Estatus=Column(String,nullable=False)
    Foto_Empleado=Column(String,nullable=False)
    FotoINE_Delantera=Column(String,nullable=False)
    FotoINE_Trasera=Column(String,nullable=False)
    Comprobante_Domicilio=Column(String,nullable=False)
    Usuario=Column(String,nullable=False)
    Contraseña=Column(String,nullable=False)
    Rol=Column(String,nullable=False)

    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        aval=self.query.all()                                                                                                                                                                   
        return aval
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        emp=self.consultaIndividual()
        db.session.delete(emp)
        db.session.commit()
    def consultaIndividual(self):
        emp=self.query.get(self.ID_Empleado)
        return emp
    def consultaIndividualClave(self):
        emp=self.query.filter_by(Clave=self.Clave).first()
        return emp
    
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    
    def validarPassword(self,passs):
        pwd = Empleados.query.filter_by(Contraseña=passs).first()
        return pwd

    def is_active(self):
        if self.Estatus=='Activo':
            return True
        else:
            return False
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.ID_Empleado
    
    def getTipo(self):
        return self.Rol
    
    def validar(self,us,ps):
        emp=Empleados.query.filter_by(Usuario=us).first()
        if(emp!=None):
            if(emp.validarPassword(ps)):
                return emp
            else:
                return None

class Credito(db.Model):
    __tablename__='Credito'
    ID_Credito=Column(Integer,primary_key=True)
    Clave=Column(String,nullable=False)
    Empleado_Responsable=Column(Integer,nullable=False)
    MontoPrestado=Column(Integer,nullable=False)
    MontoPagar=Column(Integer,nullable=False)
    Semanas=Column(Integer,nullable=False)
    Estatus=Column(String,nullable=False)
    Fecha_Inicio=Column(Date,nullable=False)
    Fecha_Limite=Column(Date,nullable=False)
    Foto_EntregaCredito=Column(String,nullable=False)

    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        credito=self.query.all()                                                                                                                                                                   
        return credito
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        credito=self.consultaIndividual()
        db.session.delete(credito)
        db.session.commit()
    def consultaIndividual(self):
        credito=self.query.get(self.ID_Credito)
        return credito

class Pagos(db.Model):
    __tablename__ = "Pagos"
    ID_pagos=Column(Integer,primary_key=True)
    Credito=Column(Integer,nullable=False)
    Clave=Column(String,nullable=False)
    Monto=Column(Integer,nullable=False)
    Semana=Column(Integer,nullable=False)
    Fecha_Pago=Column(Date,nullable=False)
    Foto_Comprobante=Column(String,nullable=False)

    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        pago=self.query.all()                                                                                                                                                                   
        return pago
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        pago=self.consultaIndividual()
        db.session.delete(pago)
        db.session.commit()
    def consultaIndividual(self):
        pago=self.query.get(self.ID_pagos)
        return pago
    
    def consultaPagosCreditoIndi(self):
        pago=self.query.filter_by(Credito=self.Credito).all()
        return pago
    


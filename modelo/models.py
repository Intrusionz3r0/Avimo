from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,LargeBinary,BLOB
from sqlalchemy.orm import relationship                                                                                                                                                          


db=SQLAlchemy()                                                                                                                                                                                  
                                                                                                                                                                                                 
class Clientes(db.Model):                                                                                                                                                                        
    __tablename__='Clientes'                                                                                                                                                                    
    ID_Cliente=Column(Integer,primary_key=True)                                                                                                                                                  
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
    Fecha_Registro=Column(DateTime,nullable=False)
    Estatus=Column(String,nullable=False)
    FotoINE_Delantera=Column(BLOB,nullable=False)
    FotoINE_Trasera=Column(BLOB,nullable=False)
    FotoCliente=Column(BLOB,nullable=False)
    Comprobante_Domicilio=Column(BLOB,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        Clientes=self.query.all()                                                                                                                                                                   
        return Clientes
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        Clientes=self.consultaIndividual()
        db.session.delete(Clientes)
        db.session.commit()
    def consultaIndividual(self):
        Clientes=self.query.get(self.ID_Cliente)
        return Clientes
    def consultaID(self):
        Clientes=self.query.get(self.Nombre)
        return Clientes



class Avales(db.Model):                                                                                                                                                                        
    __tablename__='Avales'
    ID_Avales=Column(Integer,primary_key=True)
    Cliente = Column(Integer,ForeignKey('Clientes.ID_Cliente'))
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
    FotoINE_Delantera=Column(BLOB,nullable=False)
    FotoINE_Trasera=Column(BLOB,nullable=False)
    Comprobante_Domicilio=Column(BLOB,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        Avales=self.query.all()                                                                                                                                                                   
        return Avales
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        Avales=self.consultaIndividual()
        db.session.delete(Avales)
        db.session.commit()
    def consultaIndividual(self):
        Avales=self.query.get(self.Cliente)
        return Avales
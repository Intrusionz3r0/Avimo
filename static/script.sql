CREATE DATABASE AVIMO;
show databases; 

Use AVIMO;
/*Creacion tabla Clientes */
create table Clientes (
ID_Cliente INT auto_increment,
Clave varchar(20) not null UNIQUE,
Nombre VARCHAR(60) not null,
Apellidos VARCHAR(60) not null,
Genero VARCHAR(9) not null,
Estado VARCHAR(30) not null,
Municipio VARCHAR(40) not null,
Colonia VARCHAR(40) not null,
CallePrincipal VARCHAR(30) not null,
NumInterior int not null,
NumExterior int ,
EntreCalles VARCHAR(60) not null,
Telefono VARCHAR(12) not null,
CURP VARCHAR(18) not null,
Fecha_Nacimiento date not null,
Fecha_Registro date not null,
Estatus varchar(8) not null,
FotoINE_Delantera varchar(100),
FotoINE_Trasera varchar(100),
FotoCliente varchar(100),
Comprobante_Domicilio varchar(100),

Primary key (ID_Cliente)

);
ALTER TABLE Clientes AUTO_INCREMENT=1000;

/* Creacion tabla Avales*/
create table Avales(
ID_Aval INT auto_increment,
Clave VARCHAR(20) not null UNIQUE,
Nombre VARCHAR(30) not null,
Apellidos VARCHAR(60) not null,
Estado VARCHAR(30) not null,
Municipio VARCHAR(40) not null,
Colonia VARCHAR(40) not null,
CallePrincipal VARCHAR(30) not null,
NumInterior int not null,
NumExterior int ,
EntreCalles VARCHAR(60) not null,
Telefono VARCHAR(13) not null,
FotoINE_Delantera varchar(100),
FotoINE_Trasera varchar(100),
Comprobante_Domicilio varchar(100),

primary key(ID_Aval),
Foreign key(Clave) references Clientes (Clave)
);
ALTER TABLE Avales AUTO_INCREMENT=1000;

/*Creacion tabla Empleados*/
create table Empleados(
    
ID_Empleado int auto_increment,
Clave VARCHAR(20) not null UNIQUE,
Nombre VARCHAR(30) not null,
Apellidos VARCHAR(60) not null,
Sexo VARCHAR(9) not null,
Telefono VARCHAR(13) not null,
Estado VARCHAR(30) not null,
Municipio VARCHAR(40) not null,
Colonia VARCHAR(40) not null,
CallePrincipal VARCHAR(30) not null,
EntreCalles VARCHAR(60) not null,
NumExterior int ,
NumInterior int not null,
CURP VARCHAR(18) not null,
Fecha_Nacimiento date not null,
Fecha_Contratacion date not null,
Estatus VARCHAR(8) not null,
Foto_Empleado varchar(100),
FotoINE_Delantera varchar(100),
FotoINE_Trasera varchar(100),
Comprobante_Domicilio varchar(100),
Usuario varchar(25) unique not null,
Contraseña varchar(25) not null,
Rol varchar(20) not null,
primary key(ID_Empleado)
);
ALTER TABLE Empleados AUTO_INCREMENT=1000;

/*Creacion tabla Credito*/
create table Credito(
ID_Credito int auto_increment,
Clave varchar(14) not null,
Empleado_Responsable int not null,
MontoPrestado int not null,
MontoPagar int not null,
Semanas int not null,
Estatus VARCHAR(8) not null,
Fecha_Inicio date not null,
Fecha_Limite date not null,
Foto_EntregaCredito varchar(100), /* Checar si la foto se subira en que tiempo*/

primary key(ID_Credito),
foreign key(Clave) references Clientes(Clave),
foreign key(Empleado_Responsable) references Empleados(ID_Empleado)
);
ALTER TABLE Credito AUTO_INCREMENT=1000;

/*Creacion de tabla Pagos*/
Create table Pagos(
ID_pagos int auto_increment,
Credito int not null,
Clave VARCHAR(13) not null,
Monto int not null,
Semana int not null,
Fecha_Pago date not null,
Foto_Comprobante varchar(100),

primary key(ID_Pagos)
);
ALTER TABLE Pagos AUTO_INCREMENT=1;

insert into Empleados(Clave,Nombre,Apellidos,Sexo,Telefono,Estado,Municipio,Colonia,CallePrincipal,EntreCalles,NumExterior,NumInterior,CURP,Fecha_Nacimiento,Fecha_Contratacion,Estatus,Foto_Empleado,FotoINE_Delantera,FotoINE_Trasera,Comprobante_Domicilio,Usuario,Contraseña,Rol) value('AAAA000000A00','Administrador',' ','Masculino','351-519-8521',' ',' ',' ',' ',' ','0','10','AAAA000000AAAAAA00','1990-10-10','2020-12-17','Activo','null','null','null','null','PowerFull','pa55Word','Jefe');
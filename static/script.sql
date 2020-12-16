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
FotoINE_Delantera blob,
FotoINE_Trasera blob,
FotoCliente blob,
Comprobante_Domicilio blob,

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
FotoINE_Delantera blob,
FotoINE_Trasera blob,
Comprobante_Domicilio blob,

primary key(ID_Aval)
);
ALTER TABLE Avales AUTO_INCREMENT=1000;

/*Creacion tabla Empleados*/
create table Empleados(
    
ID_Empleado int auto_increment,
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
Foto_Empleado blob,
FotoINE_Delantera blob,
FotoINE_Trasera blob,
Comprobante_Domicilio blob,
Usuario varchar(25) unique not null,
Contraseña varchar(25) not null,
Rol varchar(20) not null,
primary key(ID_Empleado)
);
ALTER TABLE Empleados AUTO_INCREMENT=1000;

/*Creacion tabla Credito*/
create table Credito(
ID_Credito int auto_increment,
Cliente int not null,
Empleado_Responsable int not null,
MontoPrestado int not null,
MontoPagar int not null,
Semanas int not null,
Estatus VARCHAR(8) not null,
Fecha_Inicio date not null,
Fecha_Limite date not null,
Foto_EntregaCredito blob, /* Checar si la foto se subira en que tiempo*/

primary key(ID_Credito),
foreign key(Cliente) references Clientes(ID_Cliente),
foreign key(Empleado_Responsable) references Empleados(ID_Empleado)
);
ALTER TABLE Credito AUTO_INCREMENT=1000;

/*Creacion de tabla Pagos*/
Create table Pagos(
ID_pagos int auto_increment,
Credito int not null,
Cliente int not null,
Monto int not null,
Semana int not null,
Fecha_Pago date not null,
Foto_Comprobante blob,

primary key(ID_Pagos),
foreign key(Credito) references Credito(ID_Credito),
foreign key(Cliente) references Clientes(ID_Cliente)
);
ALTER TABLE Pagos AUTO_INCREMENT=1;


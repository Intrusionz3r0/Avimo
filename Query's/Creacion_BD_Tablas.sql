CREATE DATABASE AVIMO;
show databases; 

Use AVIMO;
/*Creacion tabla Clientes */
create table Clientes (
ID_Cliente INT auto_increment,
Nombre VARCHAR(100) not null,
Sexo CHAR(1) not null,
Telefono VARCHAR(13) not null,
Direccion VARCHAR(150) not null,
CURP VARCHAR(18) not null,
Fecha_Nacimiento date not null,
Fecha_Registro date not null,
Estatus char(1) not null,
FotoINE_Delantera blob,
FotoINE_Trasera blob,
FotoCliente blob,
Comprobante_Domicilio blob,

Primary key (ID_Cliente)
);

/* Creacion tabla Avales*/
create table Avales(
Cliente int not null,
Nombre VARCHAR(100) not null,
Telefono VARCHAR(13) not null,
Direccion VARCHAR(150) not null,
FotoINE_Delantera blob,
FotoINE_Trasera blob,
Comprobante_Domicilio blob,

foreign key(Cliente) references Clientes(ID_Cliente)
);

/*Creacion tabla Empleados*/
create table Empleados(
ID_Empleado int auto_increment,
Nombre VARCHAR(100) not null,
Sexo CHAR(1) not null,
Telefono VARCHAR(13) not null,
Direccion VARCHAR(150) not null,
CURP VARCHAR(18) not null,
Fecha_Nacimiento date not null,
Fecha_Contratacion date not null,
Estatus CHAR(1) not null,
Foto_Empleado blob,
FotoINE_Delantera blob,
FotoINE_Trasera blob,
Comprobante_Domicilio blob,

primary key(ID_Empleado)
);

/*Creacion tabla Credito*/
create table Credito(
ID_Credito int auto_increment,
Cliente int not null,
Empleado_Responsable int not null,
MontoPrestado int not null,
Semanas int not null,
Estatus CHAR(1) not null,
Fecha_Inicio date not null,
Fecha_Limite date not null,
Foto_EntregaCredito blob, /* Checar si la foto se subira en que tiempo*/

primary key(ID_Credito),
foreign key(Cliente) references Clientes(ID_Cliente),
foreign key(Empleado_Responsable) references Empleados(ID_Empleado)
);

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
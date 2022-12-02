create schema practica_sql authorization oxfyyjpy;

create table practica_sql.grupos_coches(
	cod_grupo varchar(5) not null,
	des_grupo varchar(100) not null,
	inf1_grupo varchar(100) null,
	inf2_grupo varchar(100) null,	
	constraint grupos_coches_PK primary key (cod_grupo)
);


create table practica_sql.aseguradoras(
	cod_aseguradora varchar(5) not null,
	des_aseguradora varchar(100) not null,
	inf1_aseguradora varchar(100) null,
	inf2_aseguradora varchar(100) null,
	constraint aseguradoras_PK primary Key (cod_aseguradora)
);

create table practica_sql.marcas_coches(
	cod_marca varchar(5) not null,
	cod_grupo varchar(5) not null,
	des_marca varchar(100) not null,
	inf1_marca varchar(100) null,
	inf2_marca varchar(100) null,
	constraint marcas_coches_PK primary Key(cod_marca)
);

alter table practica_sql.marcas_coches
add constraint marcas_coches_FK foreign key (cod_grupo)
references practica_sql.grupos_coches (cod_grupo); 

create table practica_sql.polizas(
	cod_poliza varchar(100) not null,
	cod_aseguradora varchar(5) not null,
	constraint cod_poliza_PK primary Key (cod_poliza)
);

alter table practica_sql.polizas
add constraint polizas_FK foreign key (cod_aseguradora)
references practica_sql.aseguradoras (cod_aseguradora);

create table practica_sql.modelos_coches(
	cod_modelo varchar(5) not null,
	cod_marca varchar(100) not null,
	des_modelo varchar(100) not null,
	inf_modelo varchar(100) null,
	constraint modelos_coches_PK primary Key (cod_modelo)
);

alter table practica_sql.modelos_coches
add constraint modelos_coches_FK foreign key (cod_marca)
references practica_sql.marcas_coches (cod_marca);

create table practica_sql.coches(
	cod_matricula varchar(10) not null,
	km_totales varchar(100) not null,
	color varchar(100) not null,
	cod_poliza varchar(100) not null,
	fecha_compra timestamp not null,
	cod_modelo varchar(100) not null,
	cod_marca varchar(100) not null,
	
	constraint coches_PK primary Key (cod_matricula),
	constraint coches_poliza_FK foreign key (cod_poliza) references practica_sql.polizas (cod_poliza),
	constraint coches_modelo_FK foreign key (cod_modelo) references practica_sql.modelos_coches (cod_modelo),
	constraint coches_marca_FK foreign key (cod_marca) references practica_sql.marcas_coches (cod_marca)
);


create table practica_sql.revisiones (
	cod_factura varchar(20) not null,
	cod_matricula varchar(10) not null,
	fecha timestamp not null, 
	kms integer not null, 
	importe decimal(5,2) not null, 
	moneda varchar(10) not null,
	
	constraint revisiones_PK primary key (cod_factura),
	constraint revisiones_coches_FK foreign key (cod_matricula) references practica_sql.coches (cod_matricula)	
);

-- INSERT Aseguradoras --
insert into practica_sql.aseguradoras  (cod_aseguradora, des_aseguradora, inf1_aseguradora, inf2_aseguradora) 
	values ('001', 'mutua', null, null);
insert into practica_sql.aseguradoras  (cod_aseguradora, des_aseguradora, inf1_aseguradora, inf2_aseguradora) 
	values ('002', 'mapfre', null, null);
insert into practica_sql.aseguradoras  (cod_aseguradora, des_aseguradora, inf1_aseguradora, inf2_aseguradora) 
	values ('003', 'Linea directa', null, null);

-- INSERT Polizas --
insert into practica_sql.polizas  (cod_poliza, cod_aseguradora)
	values ('00001', '001');
insert into practica_sql.polizas  (cod_poliza, cod_aseguradora)
	values ('00002', '002');
insert into practica_sql.polizas  (cod_poliza, cod_aseguradora)
	values ('00003', '003');

-- INSERT Grupos coches --
insert into practica_sql.grupos_coches  (cod_grupo, des_grupo, inf1_grupo, inf2_grupo)
	values ('01', 'VAG', NULL, NULL);
insert into practica_sql.grupos_coches  (cod_grupo, des_grupo, inf1_grupo, inf2_grupo)
	values ('02', 'RENAULT', NULL, NULL);
insert into practica_sql.grupos_coches  (cod_grupo, des_grupo, inf1_grupo, inf2_grupo)
	values ('03', 'MAZDA', NULL, NULL);

-- INSERT Marcas coches --
insert into practica_sql.marcas_coches  (cod_marca, des_marca, inf1_marca, inf2_marca, cod_grupo)
	values ('001', 'Seat', NULL, NULL, '01');
insert into practica_sql.marcas_coches  (cod_marca, des_marca, inf1_marca, inf2_marca, cod_grupo)
	values ('002', 'Renault', NULL, NULL, '02');
insert into practica_sql.marcas_coches  (cod_marca, des_marca, inf1_marca, inf2_marca, cod_grupo)
	values ('003', 'Mazda', NULL, NULL, '03');

-- INSERT Modelos coches --
insert into practica_sql.modelos_coches  (cod_modelo, cod_marca, des_modelo, inf_modelo)
	values ('0001', '001', 'ibiza', NULL);
insert into practica_sql.modelos_coches  (cod_modelo, cod_marca, des_modelo, inf_modelo)
	values ('0002', '002', 'clio', NULL);
insert into practica_sql.modelos_coches  (cod_modelo, cod_marca, des_modelo, inf_modelo)
	values ('0003', '003', 'mazda3', NULL);

-- INSERT Coches --
insert into practica_sql.coches (cod_matricula, km_totales, color, cod_poliza, fecha_compra, cod_modelo, cod_marca) 
	values ('2345mpb', 12000, 'rojo', '00001', current_timestamp, '0001', '001');
insert into practica_sql.coches (cod_matricula, km_totales, color, cod_poliza, fecha_compra, cod_modelo, cod_marca) 
	values ('2111lps', 24322, 'verde', '00002', current_timestamp, '0002', '002');
insert into practica_sql.coches (cod_matricula, km_totales, color, cod_poliza, fecha_compra, cod_modelo, cod_marca) 
	values ('1432blm', 124000, 'negro', '00003', current_timestamp, '0003', '003');

-- INSERT Revisiones --
insert into practica_sql.revisiones (cod_factura, cod_matricula, fecha, kms, importe, moneda) 
	values ('000001', '2345mpb', current_timestamp, 12000, 125, 'EURO');
insert into practica_sql.revisiones (cod_factura, cod_matricula, fecha, kms, importe, moneda) 
	values ('000002', '2111lps', current_timestamp, 24322, 300, 'EURO');
insert into practica_sql.revisiones (cod_factura, cod_matricula, fecha, kms, importe, moneda) 
	values ('000003', '1432blm', current_timestamp, 124000, 60, 'DOLAR');





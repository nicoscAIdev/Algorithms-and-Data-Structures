%hechos

chofer(10101,'Juan_de_la_Prueba',direccion('Cabrera',123),12.45,'No',licencia(2018,'D1')).
chofer(10021,'German_de_la_Prueba',direccion('Alvear',125),12.45,'Si',licencia(2016,'D2')).
chofer(10034,'Jose_de_la_Prueba',direccion('Santiago_del_Estero',454),15.60,'Si',licencia(2016,'D2')).
chofer(10343,'Esteban_de_la_Prueba',direccion('San_Juan',556),15.60,'No',licencia(2017,'D1')).
chofer(12034,'Carlo_de_la_Prueba',direccion('San_Martin',52),11.50,'No',licencia(2017,'D2')).
chofer(44312,'Ignacio_de_la_Prueba',direccion('Belgrano',435),12.45,'Si',licencia(2017,'D2')).
chofer(14553,'Marcos_de_la_Prueba',direccion('Belgrano',743),12.45,'Si',licencia(2016,'D1')).
chofer(4532,'Oscar_de_la_Prueba',direccion('Ayacucho',566),15.60,'No',licencia(2018,'D2')).
chofer(12344,'Mariano_de_la_Prueba',direccion('Vilcapugio',454),11.50,'Si',licencia(2018,'D2')).
chofer(34398,'Juan_Carlos_de_la_Prueba',direccion('Salta',124),14.80,'No',licencia(2018,'D1')).

tramo(1,'Tramo_A',200,1,6,10101).
tramo(2,'Tramo_B',150,4,3,12034).
tramo(3,'Tramo_C',80,4,2,10343).
tramo(4,'Tramo_D',150,6,5,44312).
tramo(5,'Tramo_E',100,1,2,14553).
tramo(6,'Tramo_F',200,1,4,10101).
tramo(7,'Tramo_G',80,1,5,12344).
tramo(8,'Tramo_H',200,5,1,34398).
tramo(9,'Tramo_I',150,5,4,4532).

localidad(1,'Cordoba').
localidad(2,'Coronel_Moldes').
localidad(3,'Adelia_Maria').
localidad(4,'Rio_Cuarto').
localidad(5,'Villa_Maria').
localidad(6,'San_Francisco').

% Determinar Nombre, Direcci�n completa y Refrigerio de los choferes que
% tiene tramos con Origen en la Ciudad de C�rdoba

item1(Nombre,Calle,Numero,Refrigerio):-chofer(Leg,Nombre,direccion(Calle,Numero),_,Refrigerio,_),tramo(_,_,_,Origen,_,Leg),localidad(Origen,'Cordoba').

regla1(Nom, Direc, Re):- chofer(Leg, Nom, Direc, _, Re,_),
tramo(_,_,_,Origen,_,Leg),
localidad(Origen,'Cordoba').


% Informar el Nombre del chofer, la localidad de origen, la localidad
% de destino y el nombre del tramo de
% aquellos tramos cuya distancia es superior a un valor de referencia

item2(Nombre,Origen,Destino,Tramo,X):-chofer(Leg,Nombre,_,_,_,_),tramo(_,Tramo,Distancia,NumOrigen,NumDestino,Leg),localidad(NumOrigen,Origen),localidad(NumDestino,Destino),X < Distancia.

regla2(Nom,LocO,LocD,NomT,D):- chofer(Leg,Nom,_,_,_,_),
tramo(_,NomT,Dis,CodO,CodD,Leg),
localidad(CodO, LocO),
localidad(CodD,LocD),
Dis > D.

% 3. Determinar por cada chofer cual es el total que se le paga por
% recorrer el tramo asignado sabiendo que el total se calcula como el
% producto entre la distancia del tramo por el precio por kil�metro ms
% un 20% adicional si cobra refrigerio.

regla3P(Nom,Total):- chofer(Leg,Nom,_,Precio,Refrigerio,_),
tramo(_,_,Distancia,_,_,Leg),
((Refrigerio = 'Si',
Monto is Precio * Distancia,
Total is Monto + Monto * 0.2);
(Refrigerio = 'No',
Total is Precio * Distancia
)
).

%4. Indicar la cantidad de choferes que tienen un tipo de licencia X.


%5. Indicar la cantidad de tramos definidos para un Origen X.

%6. Listar el nombre del chofer, la direccin, el total a cobrar de
% todos aquellos choferes que tengan la licencia de un tipo X.

%7. Indicar el nombre de los choferes que tienen ms de 2 hijos.
% Resultado:
% ?-  punto7(Nombre).
% Nombre = 'Jose_de_la_Prueba'
% Nombre = 'Esteban_de_la_Prueba'
% Nombre = 'Oscar_de_la_Prueba'


%8. Indicar el nombre de los choferes que tienen un hijo llamado
% "maximo"
%Resultado: ?- punto8(Nombre). Nombre = 'Esteban_de_la_Prueba'
% ; Nombre = 'Juan_Carlos_de_la_Prueba'.


% 9. Mostrar el sueldo que perciben los choferes que tienen ms de 2
% hijos.
% Resultado:
%?- punto9(Nombre,Monto).
% Nombre = 'Esteban_de_la_Prueba', Monto = 1248.0 ;
% Nombre = 'Oscar_de_la_Prueba', % Monto = 2340.0 ;
% Nota: el chofer 10034 tiene ms de 2 hijos pero no
% esta trabajando en ning�n tramo.


%10. Determine cual es la cantidad de hijos promedio entre los choferes





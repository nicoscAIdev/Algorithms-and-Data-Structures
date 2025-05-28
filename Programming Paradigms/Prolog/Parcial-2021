Area(1, 'Gerencia').
area(2, 'Marketing').
area(3, 'Limpieza').

localidad(1, 'Córdoba').
localidad(2, 'Capilla del Monte').
localidad(3, 'Calamuchita').
localidad(4, 'Laborde').

%          1- legajo, 2- nombre, 3- apellido, 4- calle / nro / cod loc,
%          5-codarea, 6- cnt dias / precio hora / hs al dia,
%          7- basico / antiguedad / coef
trabajador(111, 'María', 'Richardi', domicilio('Jujuy', 142, 1), 3, contrato(24, 25.5, 5)).
trabajador(222, 'Diana', 'Bambini', domicilio('Calle 1', 339, 3), 3, contrato(20, 25.5, 7)).
trabajador(333, 'Lara', 'Pointer', domicilio('Perú', 721, 3), 2, efectivo(2200, 1, 2)).
trabajador(444, 'Victoria', 'Dove', domicilio('Jujuy', 344, 4), 2, efectivo(2000, 12, 1.5)).
trabajador(555, 'Ximena', 'Coraggio', domicilio('Salta', 545, 1), 3, contrato(24, 25.5, 8)).
trabajador(666, 'Gaspar', 'Gioia', domicilio('Chile', 123, 2), 3, contrato(20, 25.5, 7)).
trabajador(777, 'Vera', 'Petro', domicilio('Salta', 888, 2), 1, efectivo(2500, 0.2, 5)).
trabajador(888, 'Gastón', 'Bravi', domicilio('Luján', 104, 1), 2, efectivo(1800, 9, 2)).



Regla1(X,Y,Z):-
    trabajador(X, _, _, _,Area, contrato(CantDias, _, CantHoras)),
    area(Area, Z),
    Y is CantDias * CantHoras.


regla2(A,B,C,D,E,F):-
    trabajador(A, B, C, domicilio(_,_,NL), Area, contrato(CantDias, _,CantHoras)),
    localidad(NL, D),
    area(Area, E),
    F is CantDias * CantHoras,
    F > 125.

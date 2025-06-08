mueble('00100','Mesa de luz',300,1500.00,1,['A','B','C']).
mueble('00101','Placard infantil',500,2000.00,1,['A','B']).
mueble('00102','Cucheta madera',400,2800.00,2,['C']).
mueble('00103','Ropero',550,1850.00,3,['A','C']).

venta('55555','00101','Martinez Mario',fecha(11,06,2020),30,0).
venta('66666','00102','Casablanca Laura',fecha(05,06,2020),150,5).
venta('77777','00100','Bartoli María',fecha(12,07,2020),260,5).
venta('88888','00103','Altamirano Juan',fecha(16,08,2020),50,0).

categoria(1,'Infantil').
categoria(2,'Camas').
categoria(3,'Roperos').

regla1(Codigo):- venta(Codigo, _,_,_,_,_).

regla2(Mes,Cliente,CodFactura,CantPedida,DescMueble,Descuento):-
    venta(CodFactura,CodMueble,Cliente,fecha(_,Mes,_),CantPedida,Descuento),
    mueble(CodMueble,DescMueble,_,_,_,_).

regla3(Valor,ListaSort):-
    findall(Nombre,
            (categoria(CodCategoria,Nombre),
             mueble(_,_,Disp,_,CodCategoria,MatPrima),
             Disp > Valor,
            member('A',MatPrima)),
            Lista),
    sort(Lista,ListaSort).








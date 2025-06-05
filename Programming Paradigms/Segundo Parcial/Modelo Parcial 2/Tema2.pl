% farmaco(codigo_fármaco, denominacion, stock, costo_unitario, codigo_sucursal,
%categorias)
farmaco( '0001', 'Paracetamol', 100, 200, 1, [ 'Libre', 'Antifebril'] ).
farmaco( '0002', 'Ibuprofeno ', 300, 300, 2, [ 'Libre'] ).
farmaco( '0003', 'Salbutamol', 150, 800, 1, [ 'Recetado', ' Broncodilatador'] ) .
farmaco( '0004', 'Decidex', 50, 500, 3, [ 'Recetado', 'Antihistamínico'] ).

% orden_distribucion(codigo_orden_distribucion, codigo_farmaco,
%responsable, fecha_orden_distribucion(dia, mes, anio),
%cantidad, cantidad_por_paquete)
%orden_distribucion( 'R001', '0002', 'López Maria', fecha(15, 07, 2024), 50, 10 ).
orden_distribucion( 'R002', '0003', 'Gómez Pedro', fecha(02, 08, 2024), 80, 5 ).
orden_distribucion( 'R003', '0001', 'Díaz Ana', fecha(10, 08, 2024), 100, 20).
orden_distribucion( 'R004', '0004', 'Pérez Juan', fecha(22, 08, 2024), 60, 10).

% sucursal(codigo_sucursal, descripcion_sucursal)
sucursal(1, 'Central').
sucursal(2, 'Norte').
sucursal(3, 'Sur').

regla1(Codigo,CodFarmaco,DenomFarmaco,Mes,CantPaquete,CostoTotal):-
    (orden_distribucion(Codigo,CodFarmaco,_,fecha(_,Mes,_),Cant,CantPaquete),
     farmaco(CodFarmaco,DenomFarmaco,_,CostoUnitario,_,_),
     CostoTotal is Cant*CostoUnitario
    ).

regla2(StockMin, Lista) :-
    findall(DescSucursal,
        (farmaco(CodFarmaco, _, Stock, _, CodSucursal, Categorias),
            Stock > StockMin,
            member('Recetado', Categorias),
            orden_distribucion(_, CodFarmaco, _, fecha(_, 8, _), _, _),
            sucursal(CodSucursal, DescSucursal)),
            Lista).


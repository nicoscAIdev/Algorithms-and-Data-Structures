%HECHOS DE TIPOS DE PAN.
%pan/4
%pan(CodigoPan,Descripcion, PesoPromedioGramos, PrecioPorKG).

pan('BG','Baguette',350,1800.0).
pan('PI','Pan integral',500,2200.0).
pan('CI','Ciabatta',400,2000.0).
pan('PS','Pan de semillas',450,2500.0).


%HECHOS DE INGREDIENTES EXTRAS
%ingrediente/2
%ingrediente(Codigo, Descripcion).

ingrediente('Ag','Agua').
ingrediente('Sa','Sal').
ingrediente('Le','Levadura').
ingrediente('Az','Azúcar').
ingrediente('Sm','Semillas').

%HECHOS DE CICLOS DE PRODUCCION
% ciclo/5
%ciclo(CodigoCiclo, CodigoPan, IngredientesExtras, Fecha/3, CantidadKg).
% ciclo(CodigoCiclo, CodigoPan, IngredientesExtras, Fecha(Dia,Mes,Anio),
% CantidadKg).


ciclo(1,'BG',['Ag','Le'],fecha(12,3,2025),30.0).
ciclo(2,'PI',[],fecha(12,3,2025),25.0).
ciclo(3,'CI',['Ag','Sm'],fecha(13,3,2025),20.0).
ciclo(4,'PS',['Ag','Az','Le'],fecha(13,3,2025),18.0).
ciclo(5,'BG',['Ag','Sa'],fecha(14,3,2025),35.0).

%regla1(CodigoCiclo, ImporteTotalVentaCiclo)

regla1(CodigoCiclo, Importe) :-
    ciclo(CodigoCiclo, CodigoPan, _, _, Cantidad),
    pan(CodigoPan, _, _, Precio),
    Importe is Cantidad * Precio.
regla1(_, 0).

% regla3: verifica si existe un ciclo que haya usado 'Le' o producido <
% 25 kg

regla3 :-
    ciclo(_, _, Ingredientes, _, _),
    member('Le', Ingredientes),
    !.

regla3 :-
    ciclo(_, _, _, _, Cantidad),
    Cantidad < 25,
    !.

%regla5(CodigoPan, ImporteTotalAcumulado)

regla5(CodigoPan, Total) :-
    findall(Importe, (
        ciclo(CodigoCiclo, CodigoPan, _, _, _),
        regla1(CodigoCiclo, Importe)
    ), Importes),
    sum_list(Importes, Total).


%regla6(CodigoPan, ListaCiclosConMinimo25Kg)

regla6(CodigoPan, Lista) :-
    findall(CodigoCiclo, (
        ciclo(CodigoCiclo, CodigoPan, _, _, Cantidad),
        Cantidad >= 25
    ), Lista).

%regla7(CodigoPan, CantidadCiclosSinExtras)

regla7(CodigoPan, Cantidad) :-
    findall(1, (
        ciclo(_, CodigoPan, Ingredientes, _, _),
        Ingredientes == []
    ), Lista),
    length(Lista, Cantidad).





















% Hechos base

% tipo(CodigoTipoPan, Nombre, Stock, PrecioUnitario).
tipo('BG','Baguette',350,1800.0).
tipo('PI','Pan integral',500,2200.0).
tipo('CI','Ciabatta',400,2000.0).
tipo('PS','Pan de semillas',450,2500.0).

% ingrediente(CodigoIngrediente, Nombre).
ingrediente('Ag','Agua').
ingrediente('Sa','Sal').
ingrediente('Le','Levadura').
ingrediente('Az','Azúcar').
ingrediente('Sm','Semillas').

% ciclo(IdCiclo, CodigoTipoPan, ListaCodIngredientes, Fecha, Cantidad).
ciclo(1,'BG',['Ag','Le'],fecha(12,3,2025),30.0).
ciclo(2,'PI',[],fecha(12,3,2025),25.0).
ciclo(3,'CI',['Ag','Sm'],fecha(13,3,2025),20.0).
ciclo(4,'PS',['Ag','Az','Le'],fecha(13,3,2025),18.0).
ciclo(5,'BG',['Ag','Sa'],fecha(14,3,2025),35.0).

% -----------------------------------------------------------
% Consigna 1:
% Dado un Código de Ciclo de Producción, obtener el importe total (ITVPC)
% que representa la cantidad producida * precio de venta del tipo de pan.
% Ejemplo: regla1(1, PrecioT).
regla1(CodigoC,PrecioT):- 
    ciclo(CodigoC,CodP,_,_,Cantidad),
    tipo(CodP,_,_,PrecioV),
    PrecioT is (Cantidad*PrecioV).

% -----------------------------------------------------------
% Consigna 3:
% Dado cierto código de Tipo de Pan (primer argumento),
% calcular el Importe Total Acumulado de Ciclo de Producción (ITACPP)
% Es decir, sumar los ITVPC de todos los ciclos de producción de ese tipo.
% Reutilizar regla1/2. Regla sugerida: regla5/1
% Ejemplo: regla5('BG', Total).
regla5(CodP, Total):- 
    findall(PrecioT, (ciclo(C, CodP, _, _, _), regla1(C, PrecioT)), Lista),
    sum_list(Lista, Total).

% -----------------------------------------------------------
% Consigna adicional:
% Verifica si existe algún ciclo con levadura o con cantidad producida < 25.
% Ejemplo: regla3.
regla3:- 
    (ciclo(_,_,Lista,_,_), member('Le',Lista)); 
    (ciclo(_,_,_,_,Cant), Cant < 25).

% -----------------------------------------------------------
% Consigna adicional:
% Obtener la lista de códigos de ciclo para un tipo de pan donde la cantidad producida >= 25.
% Ejemplo: regla6('CI', Lista).
regla6(CodP,ListaCiclos):- 
    findall(C, (ciclo(C, CodP, _, _, Cant), Cant >= 25), ListaCiclos).

% -----------------------------------------------------------
% Consigna adicional:
% Contar cuántos ciclos de un tipo de pan no utilizaron ingredientes (lista vacía).
% Ejemplo: regla7('PI', Cantidad).
regla7(CodP,Cantidad):- 
    findall(1, (ciclo(_,CodP,Ingredientes,_,_), Ingredientes == []), Lista),
    length(Lista,Cantidad).

% Segundo Parcial - Paradigmas de Progrmación
% Turno 1 – Programación Lógica (Prolog)

%tipo_hamburguesa(CódigoTipoBurguer,Descripción,PesoEnGramosPorUnidad,Prec
 ioPorUnidad,PorcDescuento,ListadoIngredientes). 
tipo_hamburguesa('bur01','hamburguesa simple',200,1400,10,['pan de 
hamburguesa','medallón de carne','mayonesa']). 
tipo_hamburguesa('bur02','hamburguesa doble',300,2000,25,['pan de 
hamburguesa','medallón de carne','medallón de 
carne','chédar','mayonesa','kétchup']). 
tipo_hamburguesa('bur03','hamburguesa completa',350,2500,0,['pan de 
hamburguesa','medallón de carne','medallón de 
carne','chédar','beicon','mayonesa','kétchup']). 
tipo_hamburguesa('bur04','hamburguesa pollo',220,1800,20,['pan de 
hamburguesa','medallón de pollo','mayonesa']). 


% orden_elaboración(CódigoOrden,CódigoTipoBurguer, CódigoOperario 
%fecha(Día,Mes,Año),CantidadTotalUnidadesElaboradas,TiempoTotalEnMinutos). 
orden_elaboración('ord01','bur02','ope001',fecha(14,10,2024),150,75). 
orden_elaboración('ord02','bur03','ope001',fecha(14,10,2024),180,225). 
orden_elaboración('ord03','bur01','ope003',fecha(15,10,2024),120,180). 
orden_elaboración('ord04','bur04','ope002',fecha(15,10,2024),200,150). 


%operario(CódigoOperario,Nombre,Apellido). 
operario('ope001','María','Méndez'). 
operario('ope002','Rocío','González'). 
operario('ope003','Camila','Juárez'). 


% 1. Implementar una regla que permita calcular el precio total de una orden de elaboración,
% teniendo en cuenta el precio del tipo de hamburguesa correspondiente y la cantidad
% solicitada. En caso de que el tipo de hamburguesa tenga un descuento, este se aplica
% al total. 
% Nombre sugerido: precio_total_orden/2

% 2. Implementar una regla que reciba como parámetro el código de un operario y devuelva
% la cantidad total de hamburguesas que elaboró, considerando todas las órdenes que
% tenga asignadas. 
% Nombre sugerido: cantidad_total_operario/2

% 3. Implementar una regla que reciba una lista de códigos de orden de elaboración y devuelva
% la lista de nombres de los operarios que participaron en esas órdenes.
% Nombre sugerido: operarios_en_ordenes/2


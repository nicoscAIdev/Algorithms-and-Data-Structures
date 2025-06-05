%HECHOS

cancion(1,'De Música Ligera',fecha(31,8,2023), ['A','B','C'],1).

cancion(2,'El Matador',fecha(1,9,2023),['B','E'],2).

cancion(3,'Demoliendo hoteles',fecha(10,9,2023), ['A','C','E'],3).

cancion(4,'Muchacha (Ojos de papel)',fecha(20,9,2023),['A'],1).

cancion(5,'El Amor Después del Amor',fecha(1,10,2023),['C','D','E'],4).

interpretes_autores('De Música Ligera','Soda Stereo','Gustavo Cerati y Zeta Bosio').

interpretes_autores('El Matador','Los Fabulosos Cadillacs','Flavio Cianciarulo').

interpretes_autores('Demoliendo hoteles','Charly García','Charly García').

interpretes_autores('Muchacha (Ojos de papel)','Almendra','Luis Alberto Spinetta').

interpretes_autores('El Amor Después del Amor','Fito Páez','Fito Páez').


discografica(1,'CBS Discos').

discografica(2,'Sony Music').

discografica(3,'Interdisc').

discografica(4,'Warner Music').



%  código de pista, título de la canción, interprete, año de la fecha de
% incorporación y nombre de la discográfica.


regla1(CodDiscografica, CodPista,TituloCancion,Interprete,AñoIncorp,NombreDisc):-
    cancion(CodPista,TituloCancion,fecha(_,_,AñoIncorp),_,CodDiscografica),
    interpretes_autores(TituloCancion,Interprete,_),
     discografica(CodDiscografica,NombreDisc).

% Mostrar si existen autores que tengan una canción en un determinado mes especificado como
% argumento y que el código de la discográfica sea 1.

regla2(Mes):-
    (cancion(_,_,fecha(_,Mes,_),_,1)).




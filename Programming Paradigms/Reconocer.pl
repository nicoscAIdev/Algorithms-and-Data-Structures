% ------------------------------------------
% reconocer.pl
% Programa simple en Prolog para reconocer el tema de una frase
% según palabras clave. Ideal para principiantes.
% ------------------------------------------

% ------------------------------------------
% Base de conocimiento: palabras clave y sus temas
% ------------------------------------------

palabra_clave(escuela, educacion).
palabra_clave(estudiar, educacion).
palabra_clave(profesor, educacion).
palabra_clave(futbol, deporte).
palabra_clave(basquet, deporte).
palabra_clave(correr, deporte).
palabra_clave(hamburguesa, comida).
palabra_clave(pizza, comida).
palabra_clave(comer, comida).

% ------------------------------------------
% Predicado principal: reconocer/1
% Dado un string (frase), intenta reconocer el tema
% ------------------------------------------

reconocer(Frase) :-
    % Dividimos la frase en palabras individuales (lista de strings)
    split_string(Frase, " ", "", Palabras),
    
    % Buscamos el tema analizando cada palabra
    buscar_tema(Palabras, Tema),

    % Si encontramos un tema, lo mostramos por consola
    format('Tema reconocido: ~w~n', [Tema]), !.

% ------------------------------------------
% buscar_tema/2
% Recorre la lista de palabras y busca si alguna coincide
% con una palabra clave. Devuelve el tema correspondiente.
% ------------------------------------------

buscar_tema([Palabra|_], Tema) :-
    % Convertimos de string a átomo para poder buscar en la base
    atom_string(AtomPalabra, Palabra),

    % Verificamos si es una palabra clave y obtenemos el tema
    palabra_clave(AtomPalabra, Tema).

buscar_tema([_|Resto], Tema) :-
    % Si no coincide, seguimos buscando en el resto de la lista
    buscar_tema(Resto, Tema).

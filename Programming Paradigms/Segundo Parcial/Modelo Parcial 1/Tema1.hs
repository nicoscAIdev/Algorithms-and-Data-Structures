{- Segundo Parcial - Paradigmas de Programación
Turno 1 – Programación Funcional (Haskell)

1. Implementar una función que reciba como parámetro el código de un tipo de alfajor y
retorne el precio de venta unitario correspondiente, según los datos de la tabla 1: Tipos
de alfajores. En caso de recibirse un código de tipo de alfajor que no figure en la tabla,
la función deberá devolver 0.0. Utilizar expresión case of.
Nombre sugerido de la función: funcion1.

2. Implementar una función que reciba como parámetro una lista de códigos de tipos de
alfajores. La función deberá devolver la sumatoria total de los precios de venta de cada
uno de los tipos de alfajores cuyos códigos figuren en la lista recibida como parámetro.
Reutilizar la función del punto 1).
Nombre sugerido de la función: funcion2.

3. Implementar una función que reciba 3 parámetros: una lista de precios, un valor de
referencia min, y un valor de referencia max.
La función deberá devolver una lista con los precios de la lista recibida como primer
parámetro, tales que sean mayores o iguales al valor de referencia min y menores o
iguales al valor de referencia max. Utilizar lista por comprensión.
Nombre sugerido de la función: funcion3.
-}

funcion1 codigo 
	| codigo == 1 = "Paracetamol"
	| codigo == 2 = "Ibuprofeno"
	| codigo == 3 = "Salbutamol"
	| otherwise = "Inexistente" 

funcion2 _ [] = []
funcion2 ref (x:xs) 
		    | x > ref   = x : funcion2 ref xs
    		    | otherwise = funcion2 ref xs



funcion3 [] = 0
funcion3 (x:xs)
    | x >= 10 && x <= 50 = x + funcion3 xs
    | otherwise          = funcion3 xs

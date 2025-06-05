-- Implementar una función que reciba 2 parámetros: una lista con la cantidad de 
-- reproducciones de las canciones en el primer cuatrimestre del año en curso y 
-- un valor de referencia. La función deberá retornar  la cantidad de valores de la 
-- lista recibida como primer parámetro que sean menores al valor de 
-- referencia (recibido como segundo parámetro)

funcion1 codigo | codigo == 1 = "CBS Discos"
		| codigo == 2 = "Sony Music"
		| codigo == 3 = "Interdisc"
		| codigo == 4 = "Warner Music"
		 

funcion2 [] ref = 0
funcion2 (x:xs) ref 	|	 x < ref = 1 + funcion2 xs ref
			|otherwise = funcion2 xs ref


funcion3 [] min max = 0
funcion3 (x:xs) min max | min < x && x < max = 1 + funcion3 xs min max
			| otherwise = funcion3 xs min max
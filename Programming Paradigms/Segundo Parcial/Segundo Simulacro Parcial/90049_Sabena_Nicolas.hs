funcion1 tipo | tipo == 1 = 0.5
		| tipo == 2 = 0.8
		| tipo == 3 = 1.2


funcion2 tipo importe = importe + (importe * (funcion1 tipo) / 100)


funcion3 [] ref = 0
funcion3 (x:xs) ref     | ref > x = 1 + funcion3 xs ref
			| otherwise = funcion3 xs ref

funcion1 valor  | valor == "CS" = 2500.0
		| valor == "CD" = 3500.0
		| valor == "CT" = 4000.0
		| valor == "PG" = 5900.0
		| otherwise = 0.0


funcion2 [] ref = []
funcion2 (x:xs) ref 	| x <= ref = x : funcion2 xs ref
			| otherwise = funcion2 xs ref

funcion3 [] max = 0.0
funcion3 (x:xs) max 	| x > max = x + funcion3 xs max
			| otherwise = funcion3 xs max
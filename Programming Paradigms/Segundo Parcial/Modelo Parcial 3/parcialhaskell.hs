funcion1 valor  | valor == "NF" = 12.5
		| valor == "NA" = 15.0
		| valor == "CF" = 18.0
		| valor == "T" = 10.0
		| otherwise = 0.0

funcion2 [] min max = []
funcion2 (x:xs) min max | x >= min && x <= max = x: funcion2 xs min max
			| otherwise = funcion2 xs min max

funcion3 [] ref = 0
funcion3 (x:xs) ref 	| x > ref = x + funcion3 xs ref
			| otherwise = funcion3 xs ref
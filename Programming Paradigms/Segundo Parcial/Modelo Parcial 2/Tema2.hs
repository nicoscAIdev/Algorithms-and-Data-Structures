funcion1 :: String -> Int
funcion1 codigo | codigo == "NF" = 350
		| codigo == "NA" = 420
		| codigo == "CF" = 280
		| codigo == "teatro" = 120
		| otherwise = 0


funcion2 :: [Int] -> Int -> [Int]
funcion2 [] _ = []
funcion2 (x:xs) ref 	| ref >= x = x : funcion2 xs ref
			| otherwise = funcion2 xs ref 


funcion3 :: [String] -> String -> Int
funcion3 [] _ = 0
funcion3 (x:xs) ref 	| x == ref = 1 + funcion3 xs ref
			| otherwise = funcion3 xs ref
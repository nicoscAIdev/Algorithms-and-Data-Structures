{-Implementar una función que reciba como parámetro el código de un tipo de alfajor y
retorne el precio de venta unitario correspondiente, según los datos de la tabla 1: Tipos
de alfajores. En caso de recibirse un código de tipo de alfajor que no figure en la tabla,
la función deberá devolver 0.0. Utilizar expresión case of. Nombre sugerido de la función:
funcion1.
-}

funcion1::String -> Float
funcion1 cod = case cod of 
               "MT"  -> 1500.0
               "TDL" -> 2500.0
               "DDL" -> 2200.0
               "DM"  -> 1200.0
               _    -> 0.0


{-Implementar una función que reciba como parámetro una lista de códigos de tipos de
alfajores. La función deberá devolver la sumatoria total de los precios de venta de cada
uno de los tipos de alfajores cuyos códigos figuren en la lista recibida como parámetro.
Reutilizar la función del punto 1). Nombre sugerido de la función: funcion2.-}


funcion2 :: [String] -> Float
funcion2 [] = 0
funcion2 (x:xs) = funcion1 x + funcion2 xs

{-Implementar una función que reciba 3 parámetros: una lista de precios, un valor de
referencia min, y un valor de referencia max.
La función deberá devolver una lista con los precios de la lista recibida como primer
parámetro, tales que sean mayores o iguales al valor de referencia min y menores o
iguales al valor de referencia max. Utilizar lista por comprensión. Nombre sugerido de la
función: funcion3.-}

funcion3 :: [Float] -> Float -> Float -> [Float]
funcion3 lista min max = [x | x <- lista, x >= min, x <= max]



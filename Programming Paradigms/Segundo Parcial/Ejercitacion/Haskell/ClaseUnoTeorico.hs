--Función que recibe una lista de Bool y devuelve True en caso que haya al menos un
valor True en la lista, y False en caso que todos los elementos de la lista fuesen
False.
hayAlgunTrue :: [Bool] -> Bool
hayAlgunTrue [] = False
hayAlgunTrue (x:xs) = x || hayAlgunTrue xs 

--función que recibe como parámetro una lista y devuelve la suma de todos los
elementos de la misma.
sumatoriaLista :: [Int] -> Int
sumatoriaLista [] = 0
sumatoriaLista (h:t) = h + sumatoriaLista(t) 

--Función que recibe una lista de Bool y devuelve True en caso que haya al menos un
valor False en la lista, y False en caso que todos los elementos de la lista fuesen
True.
hayAlgunFalse :: [Bool] -> Bool
hayAlgunFalse [] = True
hayAlgunFalse (x:xs) = x && hayAlgunTrue xs 

--parámetro una lista de enteros y devuelve una lista de String.
--Devuelve una lista de String con las cadenas par o impar según sea par o impar
cada elemento de la lista que se recibe como parámetro.
parImpar :: [Int] -> [String]
parImpar (x) = map paridad x 

--Función que recibe como parámetros un número entero y una lista de números ----
--enteros, y devuelve
--True en caso que el número entero sea igual al tamaño de la lista
--ó False en caso contrario
--mismoTam :: Int [Int] -> Bool
mismoTam tam lista = tam==length lista 
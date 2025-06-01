-- RECURSIVIDAD

{-- Punto 1) Programar una función que 
 permita obtener el factorial de un número.
 ej factorial 0 = 1
 ej factorial 1 = 1
 ej factorial 2 = 2
 ej factorial 3 = 6
 ej factorial 4 = ?
 ej factorial 5 = ? --}
-- factorial::Integer->Integer


-- Punto 2) Programar una función que permita obtener la suma parcial del número 10.
-- ej suma 1 = 1
-- ej suma 2 = 3
-- ej suma 3 = 6
-- ej suma 4 = ?
-- ej suma 5 = ?
-- suma::Integer->Integer


-- sumaLimites::Integer->Integer->Integer


{-- 2a) Realizar una función que permita determinar el resultado de la
siguientes suma parcial de 2n+1, con n= 1...4  --}

-- sumaA::Integer->Integer
-- ej sumaA 1 = 3
-- ej sumaA 2 = 8
-- ej sumaA 3 = 15



{-- 2b) Realizar una función que permita determinar el resultado de la
siguientes suma parcial de i(i+1), con n= 1...4  --}

--sumaB::Integer->Integer
-- ej sumaB 1 = 1
-- ej sumaB 2 = 8
-- ej sumaB 3 = 20



{-- RECURSIVIDAD2 c) Realizar una función 
que permita determinar el resultado de la
siguientes suma parcial de i/(i+1), con n= 3...5  --}

--sumaC::Integer->Integer->Float
--sumaC 1 = 1/2


{-- RECURSIVIDAD 3) Realizar una función que permita generar una lista con los restos de las 
divisiones enteras entre cada elemento y n, 
siendo n un valor entero pasado por Se quiere desarrollar una función que realice el siguiente producto: 34x21 = 714, aplicando el Método Ruso: El método Ruso consiste en la descomposición en base 2 de los factores.
--}

--multiplicacionRusa :: Integer -> Integer -> Integer



-- LISTAS

{-- Generar una lista con los valores: 10,12,45,890 y 25 --}

-- lista::[Integer]
lista = [10,12,45,890,25]


{-- LISTAS Punto 1) Dada una lista de números enteros, determine el porcentaje de valores mayores a x
(siendo x un valor pasado por parámetro--}

--contarMayorA::[Integer]->Integer->Integer

--porcentajeMayorA::[Integer]->Integer->Float
--porcentajeMayorA [] n = 0


{-- LISTAS Punto 2) Dadas dos listas de números enteros, retornar la suma de todos sus valores. 
 --}

--sumaListas::[Integer]->[Integer]->Integer

--OTRA OPCION

--sumaLista::[Integer]->Integer

-- sumaDosListas::[Integer]->[Integer]->Integer



{-- LISTAS: Realizar una función que permita generar una lista con los restos de las 
divisiones enteras entre cada elemento y n, siendo n un valor entero pasado por parámetro --}

-- restosLista::[Integer]->Integer->[Integer]
					 

{-- LISTAS: Realizar una función que a partir de una lista de números enteros, genere una nueva
lista con un valor Bool indicando si cada valor de la lista original esta comprendido
en el intervalo a y b. Siendo a y b, son pasados por parámetro. --}

-- valoresIntervalo::[Integer]->Integer->Integer->[Bool]


{-- LISTAS Punto 3) Realizar una función que dada una lista de números genere una nueva lista con los
 números binarios que representan dichos números pasados por parámetro . --}

--convertirABinario :: Integer -> String

--generarListaBinarios :: [Integer] -> [String]

-- LISTAS POR COMPRENSIÓN



{-- Punto 4) Desarrolle una función que determine la CANTIDAD de números pares de una lista de números enteros --}

--cantidadPares::[Integer]->Integer


{-- Punto 5) Dada una lista de números enteros, devuelva el cubo solo de los valores comprendidos en el intervalo a y b (siendo a y b pasados por parámetro, y no incluidos en el intervalo) --}

--valoresEntre::[Integer]->Integer->Integer->[Integer]



{-- Punto 6) Realizar una función que dada una lista de números genere una nueva lista con los números binarios que representan dichos números pasados por parámetro-} 

--generarListaBinariosv2 :: [Integer] -> [String]


{-- Punto 7) Realizar una función que dada una lista de caracteres genere una nueva lista con los códigos Ascii que representan los caracteres pasados por parámetro-} 

--convertirCadena::[Char]->[Int]


{-- Punto 8) Dada una lista de enteros mostrar sus elementos separados por un guión “-”, usando recursividad --}

--mostrar:: [Int] -> String 

{-- Punto 9) Definir la función palabrasLargas/1, recibe una lista de Strings, y devuelve la sublista de aquellas palabras que tengan al menos 7 letras --}

--palabrasLargas::[String]->[String]

--palabrasLargasPorComprension::[String]->[String]


{--Punto 10: Definir la función longitudesDeNombres/1, recibe una lista de Strings, y devuelve la lista de las longitudes de cada palabra. --}

--longitudesDeNombres::[String]->[Integer]

-- OTRA ALTERNATIVA USANDO map

--longitud::String->Integer

--longitudNombres::[String]->[Integer]



{-- Enunciado
Una empresa que brinda servicios de telefonía celular nos ha solicitado el
desarrollo de un programa que permita cumplir los siguientes requerimientos.
1) Realizar una función que reciba un código de tipo cliente, un monto base
y que retorne el monto final a pagar teniendo en cuenta el descuento
que se detalla en la Tabla 1.
En el caso que el código de tipo de cliente no sea ninguno de los
especificados en la Tabla 1 la función deberá retornar cero.
Tabla 1. Descuentos por tipo de Cliente
Código Tipo Cliente Porcentaje de Descuento
	1	3%
	2	5%
	3	7%
--}

funcion1 codigo monto | (codigo == 1) = monto * 0.97
| (codigo == 2) = monto * 0.95
| (codigo == 3) = monto * 0.93


{--
Provista la siguiente lista de enteros, en la que cada elemento de la misma
representa el número de abonados de la empresa en un periodo, resolver los
requerimientos solicitados en las consignas 2 y 3.--}
--lista :: [Integer]
-- lista = [1808, 2619, 3995, 4428, 2448, 7811]
{--2) Realizar una función que genere una nueva lista tomando como base los
elementos de la lista provista que estén comprendidos entre un valor
desde y hasta (no se incluye los extremos). Estos últimos deben ser
pasados como argumentos a la función.
Ejemplo: [1808, 2619, 3295, 4428, 2448, 7811] , desde=2000 y
hasta=3500, el resultado esperado sería:[ 2619, 3295, 2448]--}
-- funcion2 lista min max = 

funcion2 lista min max = [x | x <- lista, min > x , x < max]

funcion21 [] _ _ = []
funcion21 (x:xs) min max = if x > min && x < max
then x: funcion21 (xs) min max
else funcion21 (xs) min max


{--3) Realizar una función que permita calcular el porcentaje de elementos de
la lista provista que cumplen con estas condiciones:
a. Sea superior a un determinado valor “p”.
b. Y que sea par.
Con respecto a la cantidad total de elementos de esta. Implementar la
consigna usando recursividad en todas las funciones que Ud. considere
necesario realizar
--}

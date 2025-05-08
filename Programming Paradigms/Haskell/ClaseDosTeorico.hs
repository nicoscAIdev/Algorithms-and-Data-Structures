sumar::[Integer] -> Integer
sumar [] = 0
sumar(x:xs)=x + sumar xs


contar::[Integer] -> Integer
contar[]=0
contar(x:xs) = 1 + contar xs

mostrar::[Int] -> String
mostrar[] = []
mostrar(x:xs) = show(x)++mostrar xs

generarLista:: Integer -> [Integer]
generarLista (-1) = []
generarLista num = [num] ++ generarLista (num -1)


factores:: Integer -> [Integer]
factores n = [x | x <- [1..n], n `mod` x ==0]

mapSucesor :: [Integer] -> [Integer]
mapSucesor[] = []
mapSucesor(x:xs) = x+1 : mapSucesor xs

filtraPositivos :: [Integer] -> [Integer]
filtraPositivos [] = []
filtraPositivos (x:xs) |x>=0=x: filtraPositivos xs
|otherwise = filtraPositivos xs

menosUltimo :: [a] -> [a]
menosUltimo [] = []
menosUltimo (x:xs) = x : init xs

lasts :: [a] -> a
lasts [] = error "Lista vacia"
lasts (x:xs) = last xs

ciclo [] = []
ciclo xs = last xs : init xs
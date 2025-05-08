suma:: Integer -> Integer -> Integer
suma a b = a + b

suc:: Integer -> Integer
suc x = x + 1


sumacua :: Int -> Int -> Int
sumacua a b = a*a + b*b

sumaParOrd :: (Int, Int) -> (Int, Int) -> (Int, Int)
sumaParOrd (a, b) (c, d) = (a + c, b + d)

esmult :: Int -> Int -> Bool
esmult a x = (rem a x) == 0

calcpol:: Float -> Float
calcpol x = 7*x^2 + -14 * x + 8
where r = sqrt x

celtofahr :: Float -> Float
celtofahr x = (x + 32) * 1.8

fahrtocel :: Float -> Float
fahrtocel x = (x - 32) * 1.8


maydosv2 a b | a > b = a
| b > a = b
| otherwise = b

mayorMenor (x, y) | x > y = (x, y)
| y < x = (y, x)
|otherwise = (y, x)

indpar :: Int -> String
indpar x = if even (rem x 2) then "Es par" else "Es impar"

maytres x y z | x > y && x > z = x
| y > x && y > z = y
| z > x && z > y= z

signo :: Int -> Int
signo x | (x > 0) = 1
| (x == 0) = 0
| otherwise = -1


evaluarfunc x | (x^2 + 5*x + 0) > 0 = "Mayor a 0"
| (x^2 + 5*x + 0) == 0 = "Igual a 0"
| (x^2 + 5*x + 0) < 0 = "Menor a 0"

--primero [] = "msj"
--primero [x] = x
--primero [x,y] = x
primero (x:xs) = x
ult (x:xs) = xs
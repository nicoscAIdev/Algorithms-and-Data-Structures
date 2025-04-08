def ordenar(n1, n2, ascendent=True): 
# se asume ascendent = True... 
    first, second  = n2, n1 
    if n1 < n2: 
        first, second = n1, n2 
# ... pero si ascendent = False, invertir los valores... 
    if not ascendent: 
        first, second = second, first 
    return first, second 


def test(): 
    a = int(input('Ingrese el primer valor:  ')) 
    b = int(input('Ingrese el segundo valor: ')) 
# orden ascendente… 
    men, may = ordenar(a, b)   
    print('Menor:', men) 
    print('Mayor:', may) 
    c = int(input('Ingrese el primer valor: ')) 
    d = int(input('Ingrese el segundo valor: ')) 
# orden descendente… 
    may, men = ordenar(c, d, False)  
    print('Menor:', men) 
    print('Mayor:', may) 
# script principal... 
test()
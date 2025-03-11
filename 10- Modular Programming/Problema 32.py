def menu():
# titulo general...
    print('Menu de opciones y funciones generalizadas')
    op = 1
    while op != 4:
    # visualizacion de las opciones...
        print('1. Impares multiplos de 3')
        print('2. Primos en un intervalo')
        print('3. Secuencia ordenada')
        print('4. Salir')
        op = int(input('Ingrese el numero de la opcion elegida: '))
    # chequeo de la opcion elegida...
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
    # script principal...
menu()

def validar_mayor_que(inf):
    n = inf - 1
    while n <= inf:
        n = int(input('Valor (mayor que ' + str(inf) + ' por favor...): '))
    if n <= inf:
        print('Error... se pidió > ' + str(inf), '... cargue de nuevo...')
        return n
    
def opcion1():
    n = validar_mayor_que(0)
    res = odd_multiples(n)
    print('Intervalo analizado: [ 1', ',', n, ']')
    print('Impares multiplos de 3 en ese intervalo:', res)

def odd_multiples(n):
    print('Impares y multiplos de 3 en [ 1', ',', n, ']:')
    for i in range(1, n+1):
        if i % 2 == 1 and i % 3 == 0:
            print(i)
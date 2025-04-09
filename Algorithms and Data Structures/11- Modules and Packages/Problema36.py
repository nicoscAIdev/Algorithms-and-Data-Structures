import librerias.numeros.flotantes
import librerias.cadenas.caracteres

"""Funciones generales para manejo de numeros enteros.
Lista de funciones incluidas:
:menor(n1, n2): Retorna el menor entre dos numeros
:factorial(n): Retorna el factorial de un numero entero
:ordenar(n1, n2, ascendent = True): Ordena dos numeros
"""
def menor(n1, n2):
    """Retorna el menor entre dos numeros.
    :param n1: El primer numero a comparar
    :param n2: El segundo numero a comparar
    :return: El menor entre n1 y n2 """
    if n1 < n2:
        return n1
    return 

def factorial(n):
    """Retorna el factorial de un numero.
    :param n: El numero al cual se le calculara el factorial
    :return: El factorial de n, si n>=0. Si n<0, retorna None.
    """
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def ordenar(n1, n2, ascendent = True):
    """Ordena dos numeros.
    :param n1: El primero de los numeros a ordenar
    :param n2: El segundo de los numeros a ordenar
    :param ascendent: True ordena de menor a mayor - False en caso contrario
    :return: Los dos numeros, ordenados segun ascendent
    """
    first, second = n2, n1
    if n1 < n2 :
        first, second = n1, n2
    if not ascendent :
        first, second = second, first
    return first, second

def test():
    p = librerias.numeros.flotantes.promedio(2.34, 4, 5.34)
    print('Promedio:', p)
    if librerias.cadenas.caracteres.caracter_unico('abcde'):
        print('La cadena tiene una o varias repeticiones de un unico caracter...')
    else:
        print('La cadena tiene varios caracteres distintos...')
        print('Contenidos docstring del modulo:')
        print(librerias.cadenas.__doc__)

if __name__ == '__main__':
        test()
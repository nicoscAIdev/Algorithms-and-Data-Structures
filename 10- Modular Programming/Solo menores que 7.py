# Desarrollar un programa en Python que permita cargar por teclado una secuencia de números, uno por uno.
# Siempre se supone que el usuario cargará un 0 (cero) para indicar el final del proceso de carga.
# El cero no debe considerarse un dato a procesar. El programa debe:

# a) Determinar el porcentaje que la cantidad de números pares representa en la cantidad total de números ingresados.

# b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.

# c) Determinar el menor de los números ingresados que sean divisibles por 3.

# d) Determinar si la secuencia estaba formada sólo por números menores o iguales que 7.


# Inicializar una lista vacía por fuera de la def, para no reiniciar la lista...
lista = []

# Cargar la lista
def listaNums():
    while True:
        num = int(input("Ingrese un número (0 para terminar): "))
        if num == 0:
            break
        lista.append(num)
    return lista

def porcentaje(lista, porc):
    for num in lista:
        if num % 2:
            contPar += 1
    # Retorna directamente el calculo
    porc = len(lista) // contPar
    return porc

def num45(lista, cont45):
    for num in lista:
        if int(str(num)[-1]) == 4 or int(str(num)[-1]) == 5:
            cont45 += 1
    return cont45

def menorDiv3(lista, numDiv3):
    while min(lista) % 3 != 0:
        if lista == []:
            print("No habia numeros divisibles por 3 en la lista. ")        
            break
        lista.remove(min(lista))
    
    numDiv3 = min(lista)
    
    return numDiv3
        
def menorIgual7(lista):
    for num in lista:
        if not num <= 7:
            return False
        return True

def test():
    listaNums()
test()
# Desarrollar un programa en Python que permita cargar por teclado una secuencia de números, uno por uno.
# Siempre se supone que el usuario cargará un 0 (cero) para indicar el final del proceso de carga.
# El cero no debe considerarse un dato a procesar. El programa debe:

# a) Determinar el porcentaje que la cantidad de números pares representa en la cantidad total de números ingresados.

# b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.

# c) Determinar el menor de los números ingresados que sean divisibles por 3.

# d) Determinar si la secuencia estaba formada sólo por números menores o iguales que 7.


# Inicializar una lista vacía por fuera de la def, para no reiniciar la lista...


# Cargar la lista
def listaNums():
    lista = []
    while True:
        num = int(input("Ingrese un número (0 para terminar): "))
        if num == 0:
            break
        lista.append(num)  
    return lista # Retornamos la lista en vez de modificar una global


def porcentaje(lista):
    contPar = 0
    if not lista:
        return 0  # Si la lista está vacía, devuelve 0
    
    for num in lista:
        if num % 2 == 0:
            contPar += 1
    # Retorna directamente el calculo
    porc = (contPar / len(lista)) * 100
    return porc

def num45(lista):
    cont45 = 0
    for num in lista:
        if int(str(num)[-1]) == 4 or int(str(num)[-1]) == 5:
            cont45 += 1
    return cont45

def menorDiv3(lista):
    while min(lista) % 3 != 0:
        lista.remove(min(lista))
    numDiv3 = min(lista)
    # Retornamos
    return numDiv3
        
def menorIgual7(lista):
    for num in lista:
        if not num <= 7:
            return False
        return True

def test():
    lista = listaNums()  # Cargamos la lista
    print("\nResultados:")
    print(f"Lista ingresada: {lista}")
    print(f"Porcentaje de números pares: {porcentaje(lista):.2f}%")
    print(f"Números terminados en 4 o 5: {num45(lista)}")
    
    menor_3 = menorDiv3(lista)
    if menor_3 is None:
        print("No hay números divisibles por 3 en la lista.")
    else:
        print(f"Menor número divisible por 3: {menor_3}")

    print(f"¿Todos los números son menores o iguales a 7? {'Sí' if menorIgual7(lista) else 'No'}")
test()
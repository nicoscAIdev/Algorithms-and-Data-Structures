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
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    lista.append(num)
print(lista)

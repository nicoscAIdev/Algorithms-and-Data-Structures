# Modelo Parcial AED - Turno 2 - Enunciado 3 (T2E3)

# Una agencia de empleo desea un programa para procesar los datos de los empleos que tiene disponibles.
# Por cada empleo se registran los siguientes datos:
# - número de identificación del empleo (entero)
# - descripción del empleo (cadena)
# - monto a pagar por ese empleo (float)
# - ciudad en que se ofrece (entero de 0 a 29)
# - tipo de empleo (entero de 0 a 19)

# Se pide definir un tipo registro llamado "Empleo" con los campos mencionados.
# Desarrollar un programa completo con menú de opciones para hacer lo siguiente:

# 1) Cargar los datos en registros de tipo Empleo en un arreglo de registros (por teclado o aleatoriamente).
#    Si se hace carga manual, Todo debe ser manual. Si es automática, Todo automático.
#    Validar todos los campos que sean necesarios.
#    El arreglo debe quedar ordenado por número de identificación (id_empleo) de menor a mayor,
#    usando el algoritmo de inserción ordenada con búsqueda binaria.
#    Es incorrecto cargar todo el arreglo y luego ordenarlo: se debe insertar ordenado.

# 2) Mostrar el vector completo (una línea por registro), solo aquellos cuyo sueldo esté entre 10 y 10000 inclusive.

# 3) Usando el arreglo, determinar la cantidad de empleos por ciudad y por tipo (matriz 30 x 20),
#    mostrar solo los valores mayores a 0.

# 4) A partir del vector, crear un archivo con los empleos cuyo sueldo es mayor a un valor v dado por teclado.

# 5) Mostrar el archivo creado en el punto 4, una línea por registro, y al final mostrar la cantidad de registros leídos.

# El programa debe tener al menos dos módulos: uno para la definición del tipo de registro (Empleo)
# y otro para la lógica principal del programa con funciones para cada caso del menú.

from Registro import Agencia
import random

def mostrar_menu():
    print("1- Cargar el arreglo para n registros: ")
    print("2- Mostrar el vector completo para aquellos sueldos entre 10 y 10.000. ")
    print("3- Mostrar la cantidad de empleos por ciudad y por tipo. ")
    print("4- Crear un archivo con los empleos cuyo sueldo es mayor a un valor n. ")
    print("5- Mostrar el archivo creado. ")
    print("6- Salir. ")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


def validar_empleos(n):
    while n < 0:
        n = int(input("Ingrese una cantidad de trabajos mayores a cero: "))
    return n


def cargar_vector(vector):
    d0 = ("da", "de", "di", "do", "du")
    d1 = ("da", "de", "di", "do", "du")
    d2 = ("da", "de", "di", "do", "du")
    n = len(vector)
    for i in range(n):
        id = random.randint(80000,90000)
        desc = f"{random.choice(d0)}{random.choice(d1)}{random.choice(d2)}" 
        monto = random.uniform(200, 500)
        ciudad = random.randint(1,30)
        tipo = random.randint(1,20)
        empleo = Agencia(id, desc, monto, ciudad, tipo)
        vector[i] = empleo
        add_in_order(vector, empleo)


def add_in_order(vector, empleo):
    izq, der = 0, len(vector) - 1
    pos = 0
    print(vector)
    while izq <= der:
        c = (izq + der) // 2
        if empleo.id == vector[c].id:
            pos = c
            break
        if empleo.id > vector[c].id:
            izq = c + 1
        else:
            der = c - 1
    pos = izq
    vector.insert(pos, empleo)


def mostrar_vector(vector):
    n = len(vector)
    for i in range(n):
        print(vector[i])


def principal(): 
    opcion = -1
    while opcion != 6:
        opcion = mostrar_menu()
 
        if opcion == 1:   
            n = int(input("Ingrese la cantidad de empleos a cargar: "))
            v = validar_empleos(n)
            vector = [None] * v
            cargar_vector(vector)
            mostrar_vector(vector)

        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass


if __name__ == "__main__":
    principal()
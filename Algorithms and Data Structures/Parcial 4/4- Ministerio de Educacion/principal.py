# Ya desarrollado:
# ✔️ Módulo soporte.py con la clase Beca, con constructor y __str__.
# ✔️ Módulo principal.py con la función main() y el menú ya armado y funcional.
# ✔️ Opción 1: Generar arreglo de objetos Beca con datos aleatorios (n leído por teclado).
#              El arreglo se ordena por nombre del estudiante y reemplaza el contenido anterior.
# ✔️ Opción 2: Mostrar todos los datos del arreglo, uno por línea.
#
# SU TAREA:
# Desarrollar las siguientes funciones (máximo 4 puntos por convención de estilo y estructura):
#
# ➤ Opción 3 del menú:
#   Buscar si existe en el arreglo un objeto cuyo dni sea igual al cargado (sin validación).
#   Si existe:
#       - Mostrar todos sus datos originales
#       - Leer un nuevo monto desde teclado (sin validación)
#       - Reemplazar el campo monto
#       - Mostrar el objeto modificado
#   Si no existe:
#       - Informar que no fue encontrado
#   La búsqueda debe detenerse con la primera coincidencia.
#
# ➤ Opción 4 del menú:
#   Crear una matriz [10][5] para acumular la cantidad de becas por combinación de tipo de beca y tipo de carrera.
#   Mostrar solo los contadores mayores a un valor leído desde teclado (sin validación).
#
# ➤ Opción 5 del menú:
#   Grabar en un archivo binario los objetos del arreglo cuyo monto sea mayor a un valor leído (sin validación).
#   El archivo se crea en el momento, NO debe usarse un arreglo auxiliar.
#
# ➤ Opción 6 del menú:
#   Leer el archivo generado en el punto 5 y mostrar:
#     - Cada beca en una línea
#     - Una línea final con la cantidad total de becas, suma total de montos y el promedio.
#   Validar si el archivo existe antes de leer.
from soporte import Beca
import random, os, pickle



def mostrar_menu():
    print("1- Generar arreglo de objetos Beca con datos aleatorios (n leído por teclado)")
    print("2- Mostrar todos los datos del arreglo, uno por línea.")
    print("3- Buscar si existe en el arreglo un objeto cuyo dni sea igual al cargado (sin validación)")
    print("4- Crear una matriz [10][5] para acumular la cantidad de becas por combinación de tipo de beca y tipo de carrera.")
    print("5- Grabar en un archivo binario los objetos del arreglo cuyo monto sea mayor a un valor leído (sin validación)")
    print("6- Leer el archivo generado en el punto 5")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        n = int(input(mensaje))
    return n


def generar_vector(vector, n):
    for i in range(n):
        nombres = ("a", "b", "c", "d")
        dni = random.randint(40000,45000)
        nom = random.choice(nombres) + str(i)
        tipo_beca = random.randint(0, 9)
        tipo_carrera = random.randint(0, 4)
        monto = round(random.uniform(200, 500), 2)
        estudiante = Beca(dni, nom, tipo_beca, tipo_carrera, monto)
        add_in_order(estudiante, vector)


def add_in_order(estudiante, vector):
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if estudiante.nom == vector[c].nom:
            pos = c
            break
        elif estudiante.nom < vector[c].nom:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [estudiante]


def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])


def buscar_estudiante(dni_input, vector):
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if dni_input == vector[c].dni:
            return c
        elif dni_input < vector[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return -1


def crear_matriz(vector):
    matriz = [[0]*5 for i in range(10)]
    for estudiante in vector:
        tbeca = estudiante.tipo_beca
        tcarrera = estudiante.tipo_carrera
        matriz[tbeca][tcarrera] += 1
    return matriz


def mostrar_matriz(matriz, n):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > n:
                print(matriz[fila][columna])


def crear_archivo(fd, monto_minimo, vector):
    archivo = open(fd, "wb")
    for estudiante in vector:
        if estudiante.monto > monto_minimo:
            pickle.dump(estudiante, archivo)
    archivo.close()


def mostrar_archivo(fd, monto_minimo, vector):
    if os.path.exists(fd):
        cant = suma = 0
        archivo = open(fd, "rb")
        tam = os.path.getsize(fd)
        while archivo.tell() < tam:
            estudiante = pickle.load(archivo)
            print(estudiante)
            cant += 1
            suma += estudiante.monto
        archivo.close()
        calcular_promedio(suma, cant)
    else:
        print("El archivo no existe...")


def calcular_promedio(suma, cant):
    if cant > 0:
        prom = suma / cant
        print(f"La cantidad de estudiantes en el archivo es de {cant} y el promedio es de {round(prom, 2)}")
    else:
        print("No se encontraron estudiantes en el archivo. ")


def principal():
    opcion = -1
    vector = []
    while opcion != 0:
        opcion = mostrar_menu()

        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de n elementos que tendra el vector (debe ser mayor a cero): ")
            generar_vector(vector, n)

        if opcion == 2:
            mostrar_vector(vector)

        if opcion == 3:
            dni = int(input("Ingrese el DNI del estudiante a buscar: "))
            estudiante_dni = buscar_estudiante(dni, vector)
            if not estudiante_dni == -1:
                print(vector[estudiante_dni])
                monto_input = int(input("Ingrese el valor a reemplazar del monto"))
                vector[estudiante_dni].monto = monto_input
                print(vector[estudiante_dni])

            else:
                print("Estudiante no encontado. ")

        if opcion == 4:
            matriz = crear_matriz(vector)
            n = int(input("Ingrese el valor minimo de los contadores a mostrar: "))
            mostrar_matriz(matriz, n)

        if opcion == 5:
            fd = "archiBecas.dat"
            n = int(input("Ingrese el valor minimo del monto de los estudiantes a grabar en el archivo: "))
            crear_archivo(fd, n, vector)

        if opcion == 6:
            mostrar_archivo(fd, n, vector)


if __name__ == "__main__":
    principal()

# Tareas a desarrollar:

# [1] Generar un arreglo de registros de tipo Proyecto cargando n elementos (dato validado).
#     Puede ser aleatorio o manual.
#     El vector debe estar ordenado por número de proyecto en todo momento.
#     Cada ejecución de esta opción genera un nuevo arreglo desde cero.

# [2] Mostrar todos los datos del arreglo generado en el punto 1, uno por línea.
#     Al final del listado, mostrar una línea con el monto total acumulado de todos los proyectos.

# [3] Buscar un proyecto por título exacto (cadena ingresada por teclado, sin validación).
#     Si existe, mostrar todos sus datos; si no, mostrar mensaje.
#     La búsqueda se detiene al encontrar la primera coincidencia.

# [4] Generar una matriz de conteo [20][10] para contar cuántos proyectos hay para cada combinación
#     de tipo de proyecto (filas) y nivel de confidencialidad (columnas).
#     Mostrar solo los contadores distintos de cero.

# [5] Buscar si existe un proyecto con número (id) igual a uno leído por teclado (validado).
#     Si existe, mostrar todos sus datos. Si no, mostrar mensaje.
#     La búsqueda se detiene al encontrar la primera coincidencia.

# [6] Generar un archivo binario con los proyectos cuyo monto sea mayor a 50000.
#     El archivo se genera al seleccionar la opción (sin acumulación previa).

# [7] Mostrar el contenido del archivo generado en el punto 6.

# principal.py

import random, os, pickle
from registro import Proyecto


def mostrar_menu():
    print("1. Cargar arreglo de proyectos")
    print("2. Mostrar proyectos y total acumulado")
    print("3. Buscar proyecto por titulo")
    print("4. Crear y mostrar matriz de conteo [20][10]")
    print("5. Buscar proyecto por ID")
    print("6. Grabar proyectos con monto > 50000 en archivo")
    print("7. Mostrar contenido del archivo")
    print("0. Salir")
    return int(input("Ingrese opcion: "))


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n <= inf:
        n = int(input(mensaje))
    return n


def add_in_order(vec, proyecto):
    izq, der = 0, len(vec) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if proyecto.idp == vec[c].idp:
            pos = c
            break
        if proyecto.idp < vec[c].idp:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [proyecto]


def cargar_vector(vec, n):
    titulos = ["Medicina", "Quimica", "Fisica", "Historia", "Ingenieria"]
    for i in range(n):
        idp = random.randint(1000, 9999)
        titulo = random.choice(titulos) + str(i)
        tipo = random.randint(0, 19)
        monto = round(random.uniform(10000, 100000), 2)
        confidencialidad = random.randint(0, 9)
        p = Proyecto(idp, titulo, tipo, monto, confidencialidad)
        add_in_order(vec, p)


def mostrar_vector(vec):
    total = 0
    for proyecto in vec:
        print(proyecto)
        total += proyecto.monto
    print(f"Monto total acumulado: ${total:.2f}")


def buscar_titulo(vector):
    titulo = input(("Ingrese el nombre del titulo a buscar: "))
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if titulo == vector[c].titulo:
            return c
        if titulo < vector[c].titulo:
            der = c - 1
        else:
            izq = c + 1
    return -1


def crear_matriz(vector):
#   [20][10] para contar cuántos proyectos hay para cada combinación
#     de tipo de proyecto (filas) y nivel de confidencialidad (columnas).
#     Mostrar solo los contadores distintos de cero.
    matriz = [[0] * 10 for i in range(20)]
    for p in vector:
        tipo_proyecto = p.tipo
        nivel_conf = p.confidencialidad
        matriz[tipo_proyecto][nivel_conf] += 1
    return matriz


def mostrar_matriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] != 0:
                print(matriz[fila][columna])


def buscar_id(vector):
    id_input = validar_id()
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if id_input == vector[c].idp:
            return c
        if id_input < vector[c].idp:
            der = c - 1
        else:
            izq = c + 1
    return -1


def validar_id():
    id = input("Ingrese el ID del proyecto (solo números enteros > 0): ")
    while not id.isdigit() or int(id) <= 0:
        id = input("ID inválido. Ingrese un número entero mayor a 0: ")
    return int(id)

# [6] Generar un archivo binario con los proyectos cuyo monto sea mayor a 50000.
#     El archivo se genera al seleccionar la opción (sin acumulación previa).
def crear_archivo(fd, vector):
    archivo = open(fd, "wb")
    for py in vector:
        if py.monto > 50000:
            pickle.dump(py, archivo)
    archivo.close()


def mostrar_archivo(fd):
    if os.path.exists(fd):
        archivo = open(fd, "rb")
        tam = os.path.getsize(fd)
        while archivo.tell() < tam:
            proyecto = pickle.load(archivo)
            print(proyecto)
        archivo.close()


def principal():
    vector = []
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()

        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese cantidad de proyectos: ")
            vector = []
            cargar_vector(vector, n)

        elif opcion == 2:
            if vector:
                mostrar_vector(vector)
            else:
                print("El vector está vacío. Use la opción 1 para cargar datos.")

        elif opcion == 3:
            indice_titulo= buscar_titulo(vector)
            if not indice_titulo == -1:
                print(vector[indice_titulo])
            else:
                print("No existe ningun proyecto con ese nombre")

        elif opcion == 4:

            matriz = crear_matriz(vector)
            mostrar_matriz(matriz)

        elif opcion ==5:

            indice_id = buscar_id(vector)
            if not indice_id == -1:
                print(vector[indice_id])
            else:
                print("Proyecto no encontrado")

        elif opcion == 6:
# [6] Generar un archivo binario con los proyectos cuyo monto sea mayor a 50000.
#     El archivo se genera al seleccionar la opción (sin acumulación previa).
            fd = "proyectos.dat"
            crear_archivo(fd, vector)

        elif opcion == 7:
            mostrar_archivo(fd)

if __name__ == "__main__":
    principal()

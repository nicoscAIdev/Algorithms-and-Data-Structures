# Tu tarea:
# Desarrollar las siguientes funciones (máximo 4 puntos cada una):

# Archivos proporcionados:
# - soporte.py: contiene la clase Beca con __init__ y __str__ definidos.
# - principal.py: contiene el menú con opciones ya implementadas:
#   - Opción 1: cargar vector de objetos Beca ordenado por nombre (con add_in_order).
#   - Opción 2: mostrar todos los datos del vector.


# Opción 3:
# Buscar si existe un objeto con dni igual a d (leído por teclado, con validación).
# Si existe, mostrar sus datos, pedir nuevo monto y reemplazar el anterior. Luego mostrar el objeto actualizado.
# Si no existe, mostrar mensaje.
# La búsqueda se detiene al encontrar la primera coincidencia.

# Opción 4:
# Crear una matriz [10][5] (tipos de beca x tipos de carrera) y contar la cantidad de objetos para cada combinación.
# Mostrar solo los contadores mayores a un valor v leído por teclado.

# Opción 5:
# Grabar en un archivo binario los objetos cuya beca sea mayor a un valor m leído por teclado.
# El archivo debe generarse al ejecutar la opción, sin acumulación previa.

# Opción 6:
# Mostrar los datos del archivo generado en la opción 5.
# Mostrar además la línea con el monto total y el promedio de las becas del archivo.
from soporte import Beca
import os, random, pickle


def mostrar_menu():
    print("1- Cargar vector de objetos Beca ordenado por nombre (con add_in_order). ")
    print("2- Mostrar todos los datos del vector")
    print("3- Agencia de Investiacion Buscar si existe un objeto con dni igual a d (leído por teclado, con validación)")
    print("4- Crear una matriz [10][5] (tipos de beca x tipos de carrera)")
    print("5- Grabar en un archivo binario los objetos cuya beca sea mayor a un valor m leído por teclado.")
    print("6- Mostrar los datos del archivo generado en la opción 5.")
    opcion = int(input("Ingrese una opcion: "))
    return opcion


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        n = int(input(mensaje))
    return n


def cargar_vector(vector, n):
    nombres = ("a", "b", "c", "d")
    for i in range(n):
        dni = random.randint(40000,45000)
        nombre = random.choice(nombres) + str(i)
        tipo_beca = random.randint(0,9)
        tipo_carrera = random.randint(0,4)
        monto = round(random.uniform(200,500),2)
        estudiante = Beca(dni, nombre, tipo_beca, tipo_carrera, monto)
        add_in_order(estudiante, vector)

#ordenado por nombre
def add_in_order(estudiante, vector):
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if estudiante.nombre == vector[c].nombre:
            pos = c
            break
        elif estudiante.nombre < vector[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [estudiante]


def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])


def validar_dni():
    dni = input("Ingrese DNI (solo números, mayor a 0): ")
    while not dni.isdigit() or int(dni) <= 9999:
        dni = input("DNI inválido. Ingrese solo números, mayor a 0: ")
    return int(dni)


def buscar_dni(vector, dni_input):
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


def cambiar_monto(vector, indice):
    print(vector[indice])
    monto_input = validar_mayor_que(-1.0, "Ingrese el nuevo monto: ")
    vector[indice].monto = monto_input
    print(vector[indice])


def crear_matriz(vector):
# Crear una matriz [10][5] (tipos de beca x tipos de carrera) y contar la cantidad de objetos para cada combinación.
# Mostrar solo los contadores mayores a un valor v leído por teclado.
    matriz = [[0] * 5 for i in range(10)]
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


def generar_archivo(fd, valor_beca, vector):
    archivo = open(fd, "wb")
    for estudiante in vector:
        if vector[estudiante].monto > valor_beca:
            pickle.dump(estudiante, archivo)
    archivo.close()


def mostrar_archivo(fd):
# Mostrar los datos del archivo generado en la opción 5.
# Mostrar además la línea con el monto total y el promedio de las becas del archivo.
    if os.path.exists(fd):
        archivo = open(fd, "rb")
        tam = os.path.getsize(archivo)
        while archivo.tell() < tam:
            pickle.load(archivo)
        archivo.close()

def principal():
    opcion = -1
    vector = []
    while opcion != 0:
        opcion = mostrar_menu()

        if opcion == 1:
            n = validar_mayor_que(0, "Cargar un arreglo de n Estudiantes (n mayor a cero): ")
            cargar_vector(vector, n)

        if opcion == 2:
            mostrar_vector(vector)

        if opcion == 3:
            dni = validar_dni()
            indice = buscar_dni(vector, dni)
            if not indice == -1:
                cambiar_monto(vector, indice)
            else:
                print("No existe estudiante con el DNI ingresado. ")

        if opcion == 4:
            matriz = crear_matriz(vector)
            v = validar_mayor_que(-1, "Mostrar solo los contadores mayores a un valor v (positivo): ")
            mostrar_matriz(matriz, v)

        if opcion == 5:
            fd = "becas.dat"
            valor_beca = validar_mayor_que(-1.0, "Ingrese el monto mínimo de beca para guardar en archivo (positivo): ")
            generar_archivo(fd, valor_beca, vector)

        if opcion == 6:
            mostrar_archivo(fd)


if __name__ == "__main__":
    principal()

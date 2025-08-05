# Enunciado - Centro Deportivo de Alto Rendimiento

# 1. Cargar un arreglo de n deportistas (n leído por teclado). Permitir carga manual o aleatoria.
#    El arreglo debe mantenerse ordenado por nombre de los deportistas.
#    Puede invocarse varias veces sin eliminar datos ya cargados.

# 2. Mostrar todos los datos del arreglo, uno por renglón.

# 3. Crear un vector de conteo con el monto acumulado de pago por beca a los deportistas, 
#    para cada uno de los 10 tipos de beca (índices 0 a 9). Mostrar solo los valores distintos de cero.

# 4. Crear una matriz de conteo [50 deportes][10 tipos de beca] con la cantidad de deportistas por combinación.
#    Mostrar solo los contadores distintos de cero.

# 5. Buscar un deportista por nombre (ingresado por teclado). La búsqueda debe detenerse al encontrar el primero con coincidencia exacta.
#    Mostrar sus datos si existe, sino mostrar mensaje de no encontrado.

# 6. Grabar en un archivo binario los datos de los deportistas con tipo de beca diferente de 0.

# 7. Mostrar el contenido del archivo generado en el punto 6 y calcular el monto promedio pagado por beca.

from registro import Centro_Deportivo
import random, os, pickle


def mostrar_menu():
    print("1- Cargar un arreglo de n deportistas (n leído por teclado) ")
    print("2- Mostrar todos los datos del arreglo, uno por renglón: ")
    print("3- Agencia de Investiacion Crear un vector de conteo con el monto acumulado de pago por beca a los deportistas.")
    print("4- Crear una matriz de conteo [50 deportes][10 tipos de beca].")
    print("5- Buscar un deportista por nombre (ingresado por teclado).")
    print("6- Grabar en un archivo binario los datos de los deportistas con tipo de beca diferente de 0.")
    print("7- Mostrar el contenido del archivo. ")
    print("0- Salir. ")
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
        id = random.randint(40000, 90000)
        nombre = random.choice(nombres) + str(i)
        deporte = random.randint(0,49)
        codigo = random.randint(0,9)
        monto = round(random.uniform(2000,5000),2)
        deportista = Centro_Deportivo(id, nombre, deporte, codigo, monto)
        add_in_order(vector, deportista)


def add_in_order(vector, deportista):
    #ordenado por nombre de los deportistas
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if deportista.nombre == vector[c].nombre:
            pos = c
            break
        elif deportista.nombre < vector[c].nombre:
            der = c - 1
        else: 
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [deportista]


def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])


def vector_acumulador(vector):
    conteo = [0] * 10
    for i in range(len(vector)):
        tipo_beca = vector[i].codigo # guardamos el tipo beca en la variable
        monto = vector[i].monto # guardamos el monto en la variable
        conteo[tipo_beca] += monto # guardamos en el arreglo en el indice tipo beca
    for j in range(len(conteo)):
        if conteo[j] != 0:
            print(conteo[j])


def crear_matriz(vector):
    # Matriz de 50 deportes x 10 tipos de beca
    matriz = [[0] * 10 for i in range(50)]
    for deportista in vector:
        deporte = deportista.deporte       
        tipo_beca = deportista.codigo
        matriz[deporte][tipo_beca] += 1
    return matriz


def mostrar_matriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] != 0:
                print(matriz[fila][columna])
    

def buscar_deportista(vector, nombre):
#   Buscar un deportista por nombre (ingresado por teclado). La búsqueda debe detenerse al encontrar el primero con coincidencia exacta.
#   Mostrar sus datos si existe, sino mostrar mensaje de no encontrado.
    izq, der = 0, len(vector) - 1
    while izq <= der:
        c = (izq + der) // 2
        if nombre == vector[c].nombre:
            return c
        elif nombre < vector[c].nombre:
            der = c - 1
        else: 
            izq = c + 1
    return -1


def crear_archivo(fd, vector):
#   Grabar en un archivo binario los datos de los deportistas con tipo de beca diferente de 0.
    archivo = open(fd, "wb")
    for deportista in vector:
        if deportista.codigo != 0:
            pickle.dump(deportista, archivo)
    archivo.close()


def mostrar_archivo(fd):
    suma, cant = 0, 0
    if os.path.exists(fd):
        archivo = open(fd,"rb")
        tam = os.path.getsize(fd)
        while archivo.tell() < tam:
            deportista = pickle.load(archivo)
            print(deportista)
            suma += deportista.monto
            cant += 1
        calcular_promedio(suma, cant)
        archivo.close()
    else:
        print("El archivo no existe. ")


def calcular_promedio(suma, cant):
    if cant != 0:
        prom = suma / cant
        print("El promedio es: ", round((prom),2))
    else:
        print("No hay deportistas con un tipo de beca diferente a 0. ")


def principal():
    vector = []
    opcion = -1
    while opcion != 0 :    
        opcion = mostrar_menu()
        
        if opcion == 1:
            n = validar_mayor_que(0, "Cargar un arreglo de n deportistas (n mayor a cero): ")
            cargar_vector(vector, n)

        if opcion == 2:
            mostrar_vector(vector)

        if opcion == 3:
            vector_acumulador(vector)

        if opcion == 4:
            matriz = crear_matriz(vector)
            mostrar_matriz(matriz)

        if opcion == 5:
            nombre = input("Ingrese el nombre del deportista a buscar: ")
            posicion = buscar_deportista(vector, nombre)
            if not posicion == -1:
                print(vector[posicion])
            else: 
                print("No se encontro deportista con ese nombre. ")

        if opcion == 6:
            fd = "DatosDeportistas.dat"
            crear_archivo(fd, vector)

        if opcion == 7:
            mostrar_archivo(fd)


if __name__ == "__main__":
    principal()

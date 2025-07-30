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
    print("3- Crear un vector de conteo con el monto acumulado de pago por beca a los deportistas.")
    print("4- Crear una matriz de conteo [50 deportes][10 tipos de beca].")
    print("5- Buscar un deportista por nombre (ingresado por teclado).")
    print("6- Grabar en un archivo binario los datos de los deportistas con tipo de beca diferente de 0.")
    print("7- Mostrar el contenido del archivo. ")
    opcion = int(input("Ingrese una opcion: "))
    return opcion


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        n = int(input(mensaje))
    return n


def cargar_vector(vector, n):
    nombres = ("a", "b", "c", "d") 
    for i in range(len(vector)):
        id = random.randint(40000, 90000)
        nombre = random.choice(nombres) + str[i]
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
        elif deportista.nombre > vector[c].nombre:
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
    conteo = [] * 10
    for i in range(len(vector)):
        tipo_beca = vector[i].codigo #guardamos el nro del tipo beca en la variable
        conteo[tipo_beca] += vector[i].monto # guardamos en el arreglo en el indice tipo beca
    for j in range(len(conteo)):
        if conteo[j] != 0:
            print(conteo[j])



def principal():
    vector = []
    opcion = -1
    while opcion !=0 :    
        opcion = mostrar_menu()
        
        if opcion == 1:
            
            n = validar_mayor_que(0, "Cargar un arreglo de n deportistas (n mayor a cero): ")
            cargar_vector(vector, n)

        if opcion == 2:
            mostrar_vector(vector)

        if opcion == 3:
            vector_acumulador(vector)

        if opcion == 4:
            pass

        if opcion == 5:
            pass

        if opcion == 6:
            pass

        if opcion == 7:
            pass

    pass


if __name__ == "__main__":
    principal()
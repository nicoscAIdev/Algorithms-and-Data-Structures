








# Enunciado:
# Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos.
# Por cada trabajo se tienen los siguientes datos:
# - Número de identificación (entero positivo)
# - Descripción del trabajo
# - Tipo de trabajo (un número entero entre 0 y 19). Ejemplos: 0: siembra, 1: control de plagas, 2: cosecha, etc.
# - Importe a cobrar por ese trabajo
# - Cantidad de personal afectado al mismo

# La información referida a estos trabajos debe almacenarse en un arreglo de registros de tipo Trabajo.
# (Definir el tipo Trabajo y cargar n trabajos por teclado o de forma automática)

# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos,
# que permita gestionar las siguientes tareas:

# 1. Cargar el arreglo pedido con los datos de los n trabajos.
#    Valide que el número identificador del trabajo sea positivo y que el tipo del servicio esté entre 0 y 19.
#    Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios),
#    o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

# 2. Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3,
#    en un listado ordenado de mayor a menor según los números de identificación de esos trabajos.
#    Al final del listado, mostrar además la suma de los importes de todos los registros mostrados.

# 3. Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible (de 0 a 19).
#    Use un contador por cada tipo (20 en total). Muestre solo los resultados mayores a cero.

# 4. Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los trabajos del arreglo.


from Registro import Trabajo
import random


def mostrar_menu():
    print("1- Cargar el arreglo pedido con los datos de los n trabajos. ")
    print("2- Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado ordenado de mayor a menor según los números de identificación de esos trabajos. ")
    print("3- Agencia de Investiacion Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible.")
    print("4- Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los trabajos del arreglo. ")
    print("5- Salir. ")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


def validar_trabajos(n):
    while n < 0:
        n = int(input("Ingrese un numero de trabajos positivo: "))
    return n        


def generar_vector(vector):
    for i in range(len(vector)):
#   trabajo = f"Trabajo {str(i)}."
#   id, desc, tipo_trabajo, cobro_importe, cant_personal
        id = random.randint(1,50)
        desc = f"Trabajo {str(i)}."
        tipo = random.randint(0,19)
        cobro = round(random.uniform(200,899),2)
        personal = random.randint(2,30)
        vector[i] = Trabajo(id,desc,tipo,cobro,personal)


def cant_personal(vector):
    array_personal = []
    for i in range(len(vector)):
        if vector[i].personal > 3:
            array_personal.append(vector[i])
    return array_personal
 


def ordenar_personal(array_personal):
    for i in range(len(array_personal)):
        for j in range(len(array_personal) - 1):
            if array_personal[i].id < array_personal[j].id: 
                array_personal[i], array_personal[j] = array_personal[j], array_personal[i]
    return array_personal


def mostrar_datos(personal_ordenado):
    for i in range(len(personal_ordenado)):
        print(personal_ordenado[i])


def trabajo_por_tipo(vector):
    lista_contador = [0] * 20 
    for i in range(len(vector)): 
        j = vector[i].tipo
        lista_contador[j] += 1
    return lista_contador


def mostrar_no_nulos(lista_contador):
    for i in range(len(lista_contador)):
        if lista_contador[i] != 0:
            print(f" Para el trabajo tipo {i}, hay {lista_contador[i]} trabajos. ")


def sumador_importe(vector):
    sumador = 0
    for i in range(len(vector)):
        importe = vector[i].cobro
        sumador += importe
    return sumador


def calcular_promedio(sumador, vector):
        cant = len(vector)
        if not vector == []:
            return sumador/cant
        else:
            return 0


def mostrar_mayor_al_promedio(promedio, vector):
    print(f"El promedio es: {promedio}. ")
    for i in range(len(vector)):
        if vector[i].cobro > promedio:
            print(vector[i])


def principal():
    opcion = -1
    while opcion != 5:
        opcion = mostrar_menu()
        if opcion == 1:
            n = int(input("Ingrese la cantidad de trabajos: "))
            v = validar_trabajos(n)
            vector = [None] * v
            generar_vector(vector)
    
        if opcion == 2:
            array_personal = cant_personal(vector)
            if not array_personal == []:
                personal_ordenado = ordenar_personal(array_personal)
                mostrar_datos(personal_ordenado)
            else: 
                print("No se encontraron trabajos con personal mayor a 3. ")

        if opcion == 3:
            lista_contador = trabajo_por_tipo(vector) 
            mostrar_no_nulos(lista_contador)
            
        if opcion == 4:
            
            sumador = sumador_importe(vector)
            promedio = calcular_promedio(sumador, vector)
            mostrar_mayor_al_promedio(promedio, vector)



if __name__ == "__main__":
    principal()

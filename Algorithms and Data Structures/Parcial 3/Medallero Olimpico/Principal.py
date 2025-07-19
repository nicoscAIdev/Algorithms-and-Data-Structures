# 14. Medallero Olímpico
# El Comité Olímpico desea un programa para presentar los resultados de Tokio 2020.
# Por cada país participante, se conoce: nombre, continente (0: América / 1: Europa / 2: Asia / 3: África / 4: Oceanía),
# medallas de oro, plata y bronce.
#
# Cargar en forma manual o automática los datos de un conjunto de n países (n se ingresa por teclado)
# y luego implementar un menú con las siguientes opciones:
#
# 1. Presentar un listado ordenado por cantidad de medallas, de mayor a menor,
#    conteniendo nombre del país, nombre del continente, medallas de oro, medallas de plata,
#    medallas de bronce y total de medallas.
#
# 2. Calcular el promedio de medallas de oro para los países de un continente que se ingresa por teclado.
#
# 3. Informar los datos del país que obtuvo la mayor cantidad de medallas de plata.
#    Si varios países tienen esa cantidad, mostrar todos.
#
# 4. Determinar cuántos países obtuvieron solo medallas de bronce,
#    y qué porcentaje representan sobre el total.
#
# 5. Mostrar la cantidad de países por cada continente que participaron (5 totales).
#    Informar además a qué continente corresponde la mayor cantidad de países.
#    (Si hubiera varios con la misma cantidad, puede mostrar solo uno).


from Registro import Pais
import random

def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        print("Error! El num debe ser mayor a: ", inf)
        n = int(input(mensaje))
    return n

def cargar_vector(v):# v = Arreglo (listado) None
    for i in range(len(v)):
        pais = 'Pais: ' + str(i)
        continente = random.randint(0,4)
        cant_medallas_oro = random.randint(0,50)
        cant_medallas_plata = random.randint(0,50)
        cant_medallas_bronce = random.randint(0,50)
        v[i] = Pais(pais, continente, cant_medallas_oro, cant_medallas_plata, cant_medallas_bronce)


def ordenar_vector(v):
    for i in range(len(v) - 1):
        for j in range(i+ 1, len(v)):
            if v[i].total < v[j].total: #Listado de mayor a menor
                v[i], v[j] = v[j], v[i]


def mostrar_listado(v):
    ordenar_vector(v)
    for i in range(len(v)):
        print(v[i])
    

def validar_entre(inf, sup, mensaje):
    n = int(input(mensaje))
    while n < inf or n > sup:
        print("Error! El numero debe estar dentro de: ", inf, " y ", sup)
        n = int(input(mensaje))
    else:
        return n


def promedio_oro(v, continente):
    suma, cant = 0, 0
    
    for i in range(len(v)):
        if continente == v[i].continente:
            suma += v[i].cant_medallas_oro
            cant += 1
    return calcular_promedio(suma, cant)


def calcular_promedio(suma, cant):
    if cant != 0:
        return suma/cant
    else: 
        return 0


def buscar_mayor_plata(v):
    may = v[0]
    for i in range(1, len(v)):
        if v[i].plata > may.plata:
            may = v[i]
    return may      


def contar_solo_bronce(v):
    solo_bronce = 0    
    for i in range(len(v)):
        if v[i].cant_medallas_oro == 0 and v[i].cant_medallas_plata == 0 and v[i].cant_medallas_bronce > 0:
            solo_bronce += 1
    return solo_bronce


def calcular_porcentaje(cant, total):
    if cant == 0:
        return 0
    else:
        return cant * 100 / total


def mostrar_menu():
    print("1. Generar listado ordenado por cantidad de medallas. ")
    print("2. Calcular el promedio de medallas de oro. ")
    print("3. Generar informe de mayor cantidad de medallas de plata. ")
    print("4. Solo medallas de bronce. ")
    print("5. Mostrar la cantidad de países por cada continente que participaron. ")
    print("0. Salir. ")
    opcion = int(input("Ingrese su opcion: "))
    return opcion


def principal():
    print("Medallero Olimpico")
    n = validar_mayor_que(0, "Ingrese una cantidad de paises: ")
    v = [None] * n
    cargar_vector(v)
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            mostrar_listado(v)

        elif opcion == 2:
            continente = validar_entre(0, 4, 'Ingrese continenete: ')
            promedio = promedio_oro(v, continente)
            print(promedio)

        elif opcion == 3:
            mayor_plata = mayor_plata(v)
            print(mayor_plata)

        elif opcion == 4:
            cant = contar_solo_bronce(v)
            porc = calcular_porcentaje(cant, len(v))
            print(f"El porcentaje es: {porc}%")

if __name__ == "__main__":
    principal()
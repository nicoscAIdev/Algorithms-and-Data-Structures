# Programa con menú de opciones para gestionar distintas tareas

# Se pide desarrollar un programa en Python controlado por un menú de opciones.
# Ese menú debe permitir gestionar las siguientes tareas, siempre usando funciones que acepten parámetros 
# y/o retornen valores en cada situación en que se considere apropiado:

# a) Cargar una sucesión de números enteros y positivos (validar que efectivamente cada número que se cargue 
#    sea mayor a cero). La carga finaliza cuando se ingresa un cero.
#    Mostrar la cantidad de números de la sucesión cargada que son múltiplos del primer número de la secuencia.

# b) Ingresar por teclado dos números p y q que definen los límites de un intervalo [p, q] 
#    (validar que 0 < p < q) y una sucesión de n números (también cargando n por teclado y validando que n > 0). 
#    Determinar cuántos de los números de la sucesión cargada están fuera del intervalo y cuántos están dentro del intervalo, 
#    e indicar también cuántos de los números cargados eran pares y estaban dentro del intervalo dado.

# c) Cargar una secuencia de números enteros positivos (validar que efectivamente cada número que se cargue sea 
#    mayor a cero). La carga debe terminar cuando se ingrese un número mayor a 100.
#    Determinar si en la secuencia se ingresaron dos números contiguos que sean pares. 
#    Si es así, mostrar el promedio de todos los números pares que se hayan ingresado. 
#    Si no, informar que no se ingresaron números contiguos pares. 
#    Ejemplo:
#    - En la secuencia {1, 2, 3, 6, 4, 7, 8} hay al menos dos números contiguos que son pares (el 6 y el 4), 
#      y en este caso, el promedio de todos los pares de la secuencia es (2 + 6 + 4 + 8) / 4 = 20 / 4 = 5.
#    - Pero en esta secuencia: {1, 2, 5, 7, 8, 9, 3, 6, 1} no hay números contiguos pares.

def carga_numeros():
    pass

def intervalos():
    pass

def calcular_contiguos_promedios()
    pass

def principal():
    while True:
        print("-"*10)
        print("1. Cargar secuencia y contar múltiplos")
        print("2. Analizar números en un intervalo")
        print("3. Detectar pares contiguos y calcular promedio")
        print("4. Salir")
        print("-"*10)
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            carga_numeros()

        elif opcion == 2:
            intervalos()

        elif opcion == 3:
            calcular_contiguos_promedios()

principal()
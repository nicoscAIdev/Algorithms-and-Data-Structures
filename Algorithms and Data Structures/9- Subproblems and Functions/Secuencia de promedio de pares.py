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


def multiplo():
    vueltas = cont_multiplo = 0
    primer_num = None  # Inicializamos sin valor para asignarlo después
    lista_numeros = []

    while True:
        num = int(input("Ingrese un número positivo, ingrese 0 para terminar: "))

        if num < 0:
            print("El número ingresado debe ser positivo.")
            continue  # Pedir otro número sin terminar el programa

        if num == 0:
            break  # Finaliza la carga

        if vueltas == 0:  # Guardamos el primer número ingresado
            primer_num = num
        
        lista_numeros.append(num)
        vueltas += 1

    # Verificamos que haya al menos un número ingresado antes de calcular los múltiplos
    if primer_num is not None:
        for n in lista_numeros:
            if n % primer_num == 0:
                cont_multiplo += 1
         #Salida       
        print("La cantidad de números múltiplos de ", primer_num, "son: ", cont_multiplo, ".")
    else:
        print("No se ingresaron números válidos.")



def intervalos():
    cont_dentro_pq = cont_fuera_pq = cont_pares = 0

    while True:
        p = int(input("Ingrese el valor del intervalo 'p' (debe ser mayor que 0): "))
        q = int(input("Ingrese el valor del intervalo 'q' (debe ser mayor que 'p'): "))

        if 0 < p < q:
            break #Si se cumple, sale del while
        else: 
            print("Los valores deben ser 0 < p < q.")

    while True:
        
        num = int(input("Ingrese el valor del valor de 'n', debe ser positivo: "))
        
        if num < 0:
            print("El número ingresado debe ser positivo.")
            continue #pide otro num

        if num == 0:
            break  # Finaliza la carga

        if p <= num <= q:
            cont_dentro_pq += 1
            if num % 2 == 0:
                cont_pares += 1
        else:
            cont_fuera_pq += 1
        
    print("Los numeros dentro de p y q son: ", cont_dentro_pq, " y dentro de estos, son pares: ", cont_pares, ". La cantidad de numeros fuera de p y q son: ", cont_fuera_pq)



def calcular_contiguos_promedios():
    es_par = dos_pares = sucesion = False
    cont_pares = cant_pares = 0

    while True: #Mientas sea verdadero se ejecutara todas las opciones que esten dentro del while
        num = int(input("Ingrese el valor del valor de 'n', debe ser positivo: "))
        
        if num < 0:
            continue #Vuelve a pedir un numero, no puede ser negativo

        if num > 100:
            break    #Sale del while
        
        if es_par == True: 
            dos_pares = True #Hubo par

        if dos_pares == True:
            sucesion = True #Hubo dos pares

        if num % 2 == 0: #Comprueba si el numero es par y ejecuta
            cant_pares += 1
            cont_pares += num
            es_par = True
        else: 
            es_par = False


    if sucesion == True: #Fuera del while evalua
        print("El promedio de numeros pares ingresados es de: ", (cont_pares/cant_pares, "%"))
    else:
        print("No se ingresaron dos numeros pares contiguos. ")



def principal():
    while True:
        print("-" * 10)
        print("1. Cargar secuencia y contar múltiplos")
        print("2. Analizar números en un intervalo")
        print("3. Detectar pares contiguos y calcular promedio")
        print("4. Salir")
        print("-" * 10)
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            multiplo()
        elif opcion == 2:
            intervalos()
        elif opcion == 3:
            calcular_contiguos_promedios()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

principal()
# Desarrollar un programa controlado por menú de opciones, que permita:

# a) Tablas:
#    - Ingresar por teclado un valor positivo entre 1 y 10 (validarlo).
#    - Mostrar la tabla de multiplicar correspondiente a dicho número.
#    - Ejemplo: si se ingresa 3, mostrar:
#      3 x 1 = 3
#      3 x 2 = 6
#      ...
#      3 x 10 = 30

# b) Mayor y menor:
#    - Ingresar por teclado una sucesión de números positivos (validar).
#    - La entrada termina cuando se ingresa 0.
#    - Informar el mayor y el menor valor de la sucesión.

# c) Múltiplos:
#    - Ingresar por teclado dos valores a y b.
#    - Validar que 'a' sea positivo y que 'b' sea mayor que 'a'.
#    - Sumar todos los múltiplos de 'a' comprendidos en el intervalo [a, b].

# d) Texto:
#    - Ingresar por teclado un texto terminado en un punto (validar esto).
#    - Las palabras deben estar separadas por un único espacio.
#    - Informar cuántas palabras terminan en vocal.
#    - Calcular y mostrar qué porcentaje representan sobre el total de palabras del texto.

def tabla():
    num = int(input("Ingrese un numero de 1 al 10: "))
    vuelta = 0
    if 1 <= num <= 10:
        for i in range (1, 11):
            vuelta += 1
            print(num, "*", vuelta, "=", num * vuelta)
    else: return False


def pedir_numero():
    num = int(input("Ingrese un número positivo (0 para terminar): "))
    while num < 0:
        num = int(input("Error: Ingrese un número positivo (0 para terminar): "))
    return num

def comparar_AB():
    a = int(input("Ingrese el un valor positivo para A: "))
    b = int(input("Ingrese el un valor positivo para B mayor que A: "))
    multiplo = a

    if a > b:
        print("El valor de B debe ser mayor que el de A.")
        return
    else:
        while multiplo < b:
            if b % multiplo == 0:
                print(multiplo)
                multiplo += 1
            else: multiplo += 1

def buscar_mayor_menor():

    num = pedir_numero()
    if num == 0:
        print("No se ingresaron números.")
        return

    may = men = num  # Inicializar con el primer número válido

    while num != 0:
        if num > may:
            may = num
        if num < men:
            men = num
        num = pedir_numero()  # Pedir el siguiente número

    print(f"El número mayor de la sucesión es: {may}, y el menor es: {men}")

def listaMayMen():
    buscar_mayor_menor()


def principal():
    while True:
        print("-"*10)
        print("1. Tablas")
        print("2. Mayor y menor")
        print("3. Múltiplos")
        print("4. Texto")
        print("5. Salir")
        print("-"*10)
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            tabla()

        elif opcion == 2:
            listaMayMen()

        elif opcion == 3:
            comparar_AB()

        elif opcion == 4:
            texto =input("Ingresa un texto terminado con un punto: ")
        else: print("Volver a ingresara: ")
principal()
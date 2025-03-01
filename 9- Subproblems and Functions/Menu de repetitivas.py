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
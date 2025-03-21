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
    vuelta = 0
    #La var num sera verdadera 
    num = int(input("Ingrese un numero de 1 al 10: "))
    while not (1 <= num <= 10):
        num = int(input("El numero ingresado debe estar dentro del rango de 1 al 10: "))
    if 1 <= num <= 10:
        for i in range (1, 11):
            vuelta += 1
            print(num, "*", vuelta, "=", num * vuelta)
    else: 
        return False 


def pedir_numero():
    num = int(input("Ingrese un número positivo (0 para terminar): "))
    while num < 0:
        num = int(input("Error: Ingrese un número positivo (0 para terminar): "))
    return num

#Se utiliza la func 'pedir_numero()'
def buscar_mayor_menor():
    num = pedir_numero()
    if num == 0:
        print("No se ingresaron números.")
        return

    # Inicializar con el primer número válido
    may = men = num  
  
    #Evalua  quien es el may y men 
    #Cuando ingresa 0 corta
    while num != 0:
        if num > may:
            may = num
        if num < men:
            men = num
        # Pide el siguiente número a la func
        num = pedir_numero()  
    #Ingreso de 0 y salida
    print(f"El número mayor de la sucesión es: {may}, y el menor es: {men}")

def listaMayMen():
    buscar_mayor_menor()

def comparar_AB():
    a = int(input("Ingrese un valor positivo para A: "))
    while a <= 0:
        a = int(input("Error: Ingrese un valor positivo para A: "))

    b = int(input("Ingrese un valor mayor que A para B: "))
    while b <= a:
        b = int(input("Error: B debe ser mayor que A. Ingrese B nuevamente: "))

    sumador = 0
    for multiplo in range(a, b + 1, a):
        sumador += multiplo
        print(multiplo)

    print(f"Suma de múltiplos de {a} en el rango [{a}, {b}]: {sumador}")

# d) Texto:
def texto_ingresado():
    #Instanciamos las variables
    palabra = contVocal = contCaracter = 0
    caracterAnterior = "" 
    texto = input("Ingrese el texto y finalice con un punto: ")
    for i in texto: #Iteramos en el texto
        contCaracter += 1 

        if i == "." or i == " ":  #Si es un punto o espacio evaluamos
                                                           
            if not contCaracter == 1 and caracterAnterior == " ": #Que no sean dos espacios seguidos
                return print("Las palabras deben estar separaedas por solo un espacio.")

            #Como no es doble espacio, seguimos evaluando    
            palabra += 1 
            if caracterAnterior in "aeiouAEIOU": #Evaluamos que el caracter anterior sea vocal
                    contVocal += 1
            
            #Si es un punto terminamos
            if i == ".":
                break

        #Actualizamos el valor del caracter anterior
        caracterAnterior = i

    #Salida:
    print("La cantidad de palabras ingresadas que terminan en vocal son: ", contVocal)
    
    if palabra == 0:
        print("No se ingresaron palabras válidas.")
    else: 
        print("El porcentaje entre la cantidad de caracteres y palabras que finalizan con una vocal es de: ", (contVocal / palabra) * 100, "%")


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
            texto_ingresado()
principal()
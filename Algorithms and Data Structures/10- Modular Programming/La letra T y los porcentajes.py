# Desarrollar un programa en Python que permita cargar por teclado un texto completo.
# Se supone que el usuario ingresará un punto (".") para indicar el final del texto, 
# y que cada palabra del texto está separada de las demás por un espacio en blanco.

# El programa debe realizar las siguientes tareas:

# a) Determinar la cantidad de palabras en las que solo aparece una única vez la letra “t”.

# b) Determinar la cantidad de palabras cuya cantidad de letras es mayor a la cantidad de letras de la palabra anterior.

# c) Determinar la cantidad de palabras con una cantidad de letras par y que comiencen con la letra “c”.

# d) Determinar el porcentaje que representa el primer punto sobre el total de las palabras del texto procesado.


def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def porc(cantidad, total):
    return ((cantidad * 100) / total)


def principal():
    contCar = contWord = cantT = contPalabraAnterior = parYc = porcentaje = contPalabrasT = anteriorMayor = 0
    comienzaConC = False

    texto = input("Ingrese el texto y finalice con un punto: ")

#   Recorremos el input.
    for car in texto:
        if car != " " and car != ".":
            contCar += 1
        
        #   Evaluamos posibles errores
            if contCar == 1: 
                if car == " ":
                    contCar = 0
                    continue
                elif car == ".":
                    print("Error... El primer caracter no debe ser un punto.")
                    break
                
                elif car.lower() == "c":
                    comienzaConC = True

        #   Evaluamos que el caracter sea una igual a una "t"
            if car == "t":
                cantT += 1 
        
        else:
            contWord += 1

        #   Punto 1
            if cantT == 1:
                contPalabrasT += 1

        #   Punto 2
            if contPalabraAnterior < contCar:
                anteriorMayor += 1

        #   Punto 3
            if esPar(contCar) and comienzaConC == True:
                parYc += 1

        #   Punto 4
            porcentaje = porc(contPalabrasT, contWord)

        #   Reiniciamos
            contPalabraAnterior = contCar
            comienzaConC = False
            contCar = cantT = 0

    #   Salida: 
    print(f"La cantidad de palabras que solo aparece la letra T es de: {contPalabrasT}")
    print(f"La cantidad de palabras que sus letras son en mayot cantidad que la anterior es de: {anteriorMayor}")
    print(f"La cantidad de palabras que su cant. de palabras es par y comienza con la letra C, es de: {parYc}")
    print(f"El porcentaje entre la cantidad de palabras que solo tenia una letra T por sobre las demas palabras es de: {porcentaje}")

principal()
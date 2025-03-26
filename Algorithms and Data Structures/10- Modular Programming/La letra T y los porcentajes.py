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

def porc(num):
    return num


def principal():
    contCar = contWord = cantT = contPalabraAnterior = parYc = 0
    comienzaConC = False

    texto = input("Ingrese el texto y finalice con un punto: ")

#   Recorremos el input.
    for car in texto:
        if car != " " or car != ".":
            contCar += 1
        
        #   Evaluamos posibles errores
            if contCar == 1: 
                if car == " ":
                    contCar = 0
                    continue
                elif car == ".":
                    print("Error... El primer caracter no debe ser un punto.")
                    break
                
                elif car == "c":
                    comienzaConC = True

        #   Evaluamos que el caracter sea una igual a una "t"
            if car.lower() == "t":
                cantT += 1 
        else:
            contWord += 1
            contPalabraAnterior = contCar
        
        #   Punto 1
            if cantT == 1:
                contPalabrasT += 1

        #   Punto 2
            if contPalabraAnterior > contCar:
                anteriorMayor += 1
            
        #   Reiniciamos
            contPalabraAnterior = contCar

        #   Punto 3
            if esPar(contCar) and comienzaConC == True:
                parYc += 1
            else: 
                comienzaConC = False
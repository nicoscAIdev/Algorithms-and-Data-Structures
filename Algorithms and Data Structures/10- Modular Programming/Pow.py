"""
Desarrollar un programa en Python que permita cargar por teclado un texto completo. 
Se supone que el usuario cargará un punto para indicar el final del texto, 
y que cada palabra de ese texto está separada de las demás por un espacio en blanco. 

El programa debe:

1 Determinar la cantidad de palabras que tuvieron exactamente 3 vocales.

2 Determinar el porcentaje de palabras que tuvieron algún dígito ('0' al '9') y más de 4 letras.

3 De las palabras que terminan con la primera letra de todo el texto, 
    determinar el orden de la que tiene menor cantidad de caracteres.
    Ejemplo: en el texto "Ana está en la casa":
    - La primera letra del texto es 'A'.
    - Las palabras que terminan con 'A' son: 'Ana', 'está', 'la', 'casa'.
    - La palabra más corta es "la", que es la cuarta palabra del texto.
    - El orden de la palabra más corta es 4.

4 Determinar la cantidad de palabras que contienen "men" en la primera mitad de la palabra.
"""


def contar_palabras_con_vocales(text):
    cont_palabras_vocal = cont_vocal = cant_palabra = 0

    for car in text:
        if car in "aeiouAEIOU":
            cont_vocal += 1
        elif car == " " or car == ".":  # Fin de palabra
            cant_palabra += 1

            if cont_vocal == 3:
                cont_palabras_vocal += 1
            
            cont_vocal = 0  # Reiniciar contador para la siguiente palabra

    return cont_palabras_vocal, cant_palabra



def proces_text(text):
    cont_letras = digito_y_cuatro = 0
    num_exist = False

    for car in text:

        if car in "123456789":
            num_exist = True
       
        if car.isalpha():
            cont_letras += 1

        elif car == " " or car == ".":  # Fin de palabra
            if num_exist == True and cont_letras >= 4:
                digito_y_cuatro += 1

            cont_letras = 0  # Reiniciar contador para la siguiente palabra
            num_exist = False

    return digito_y_cuatro


def porcentaje(cantidad, base):
    return (cantidad * 100) / base


def principal():
    text = input("Ingrese texto: ")

    cont_palabras_vocal, cant_palabra = contar_palabras_con_vocales(text)
    digito_y_cuatro = proces_text(text)

    porc = porcentaje(digito_y_cuatro, cant_palabra)

    print(cont_palabras_vocal)
    print(f"{porc:.2f}%")

principal()
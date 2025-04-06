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


def es_vocal(car):
    if car.lower() in  "aeiou": 
        return True


def es_digt(car):
    if car in "1234567890":
        return True


def fin_de_palabra(car):
    if car == " " or car == ".":
        return True


def porcentaje(cantidad, base):
    return (cantidad * 100) / base


def punto1_palabras_con_vocales(text):
    cont_palabras_vocal = cont_vocal = cant_palabra = 0

    for car in text:
        if es_vocal(car):
            cont_vocal += 1

        elif fin_de_palabra(car):  # Fin de palabra
            cant_palabra += 1

            if cont_vocal == 3:
                cont_palabras_vocal += 1
            
            cont_vocal = 0  # Reiniciar contador para la siguiente palabra

    return cont_palabras_vocal, cant_palabra


def punto2_digito_Y_cuatro(text):
    cont_letras = digito_y_cuatro = 0
    num_exist = False

    for car in text:

        if es_digt(car):
            num_exist = True
       
        if car.isalpha():
            cont_letras += 1

        elif fin_de_palabra(car):  # Fin de palabra
            if num_exist == True and cont_letras > 4:
                digito_y_cuatro += 1

            cont_letras = 0  # Reiniciar contador para la siguiente palabra
            num_exist = False

    return digito_y_cuatro


def punto3_first_car_small_word(text):
    cont_word = word_most_short = word_position = 0
    primer_car = word = word_condition =  ""

    for car in text:
        primer_car = text[0]
        word += car

        if fin_de_palabra(car):

            if primer_car ==  word[0]:
                cont_word += 1

                if len(word) < word_most_short or cont_word == 1:
                    word_most_short = len(word)
                    word_condition = word
                    word_position = cont_word
        
        word = ""

    return word_condition, word_position


def principal():
    text = input("Ingrese texto: ")

#   Igualamos a una Var local las salidas de las funciones
    cont_palabras_vocal, cant_palabra = punto1_palabras_con_vocales(text) 
    digito_y_cuatro = punto2_digito_Y_cuatro(text)
    porc = porcentaje(digito_y_cuatro, cant_palabra)
    palabra_mas_corta, posicion_de_palabra = punto3_first_car_small_word(text)

#   Salida
    print(f"La cantidad de palabras que tuvieron exactamente 3 vocales fueron: {cont_palabras_vocal}")
    print(f"El porcentaje de palabras que tuvieron algún dígito ('0' al '9') y más de 4 letras fueron: {porc:.2f} %")
    print(palabra_mas_corta, posicion_de_palabra)


principal()
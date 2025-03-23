"""
Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en
punto. En base al texto ingresado, determinar:

a) Cuál es la longitud de la palabra más larga.
b) Cuántas palabras tienen la 'a' como única vocal.
c) Qué porcentaje representan las que sólo tienen la vocal 'a' sobre el total de palabras.

Ejemplo: "el agua clara salta por las piedras."
La longitud de la palabra más larga es 7 letras.
Las palabras cuya única vocal es la 'a' son: 3.
El porcentaje de estas palabras sobre el total es 43%.
"""

def enterText():
    words = input("Ingresar palabras por teclado, separadas por un espacio y terminado en punto: ")
    return words

def calcPorc(contWord, wordWhithA):
    return (wordWhithA*100/contWord)


def processText(words):
    contCar = wordWhithA = 0
    formWord = mostLarge = ""
    contWord = 0
    contA = 0

    for car in words:
        
        if contCar == 1 and car == " " :
            contCar = 0
            continue
       
        formWord += car

        # Identificamos una palabra     
        if car == " " or car == ".":
        #   La conotamos
            contWord += 1

        #   Evaluamos si es la palabra mas larga
            if len(mostLarge) < len(formWord):
                mostLarge = formWord

            # Verificamos si la palabra solo tiene la vocal 'a'
            tiene_a = False
            tiene_otra_vocal = False

            for letra in formWord:
                if letra in "aeiou":  # Si es una vocal
                    if letra == "a":
                        tiene_a = True
                    else:
                        tiene_otra_vocal = True  # Tiene otra vocal
                
            if tiene_a and not tiene_otra_vocal:  # Solo tiene 'a'
                wordWhithA += 1

            # Reiniciamos variables
            formWord = ""
            contCar = 0


    return mostLarge, contWord, wordWhithA


    

def test():    
    words = enterText()
    mostLarge, contWord, wordWhithA = processText(words)
    print("\nResultados:")
    print(words)
    print(mostLarge)
    print(wordWhithA)
    print(calcPorc(contWord, wordWhithA))
test()
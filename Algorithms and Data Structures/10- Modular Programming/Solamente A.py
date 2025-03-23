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
    contCar = wordWhithA = contWord = 0
    formWord = mostLarge = ""

    for car in words:
        
        if contCar == 1 and car == " " :
            contCar = 0
            continue
       
        formWord += car

        # Identificamos una palabra     
        if car == " " or car == ".":
        #   La contamos
            contWord += 1

        #   Evaluamos si es la palabra mas larga
            if len(mostLarge) < len(formWord):
                mostLarge = formWord

        #   Verificamos si la palabra solo tiene la vocal 'a'
            tiene_a = False
            tiene_otra_vocal = False

        #   Recorremos dentro de las palabras formadas
            for letra in formWord.lower():
                if letra in "aeiou":    #Si es una vocal
                    if letra == "a":
                        tiene_a = True
                    else:
                        tiene_otra_vocal = True    #Tiene otra vocal
        
        #   Evaluamos si la palabra solo tiene una vocal 'a'    
            if tiene_a and not tiene_otra_vocal: 
                wordWhithA += 1

        #   Reiniciamos la variable
            formWord = ""
            contCar = 0

#   Retornamos 
    return mostLarge, contWord, wordWhithA


    

def test():    
    words = enterText()
    mostLarge, contWord, wordWhithA = processText(words)
    print("\nResultados:")
    print(f"El texto Ingresado fue: {words}")
    print(f"La palabra mas larga fue: {mostLarge}")
    print(f"La cantidad de palabras que contenian solo la vocal 'a' fueron: {wordWhithA}")
    print(f"El porcentaje de palabras que solo contenian la vocal 'a', por sobre las demas palabras es de: {calcPorc(contWord, wordWhithA):.2f}%")
test()
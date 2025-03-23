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

def processText(words):
    contCar = 0
    formWord = mostLarge = ""
    for car in words:
        contCar += 1
        
        if contCar == 1 and car == " ":
            contCar = 0
            break
       
        formWord += car
       
        if car == " " or car == ".":
            if len(mostLarge) < len(formWord):
                mostLarge = formWord
                
            # Reiniciamos variables
            formWord = ""
            contCar = 0
        
    return mostLarge
    
def test():    
    words = enterText()
    print("\nResultados:")
    print(words)
    print(processText(words))

test()
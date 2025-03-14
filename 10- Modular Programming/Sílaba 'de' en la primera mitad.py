"""
Desarrollar un programa en Python que permita cargar por teclado un texto completo. 
Se supone que el usuario ingresará un punto (".") para indicar el final del texto, 
y que cada palabra del texto está separada por un espacio en blanco.

El programa debe realizar las siguientes tareas:

a) Determinar cuántas palabras contenían al menos un carácter que era un dígito 
   (un carácter entre '0' y '9').

b) Determinar cuántas palabras tenían:
   - 3 o menos letras.
   - Entre 4 y 6 letras.
   - Más de 6 letras.

c) Determinar la longitud de la palabra más larga del texto.

d) Determinar cuántas palabras contenían la expresión "de", pero solo si aparecía 
   en la primera mitad de la palabra.

"""

def is_digit(car):
   if car in "0123456789":
      return True
   else:
      return False



def enter_text():
   
   wordCont = digitCont = 0      # Inicializamos las variables
   word = ""

   text = input("Ingrese un texto y finalice con un punto: ")
   for car in text:
    word += car  # Construye la palabra

    if car == " " or car == ".":  # Si llega al final de una palabra
        wordCont += 1  # Aumenta el contador de palabras
        
        # Verifica si la palabra tiene algún número
        for car in word:
            if is_digit(car):
                digitCont += 1
                break  # Basta encontrar un número, no hace falta seguir

        word = ""  # Reinicia la palabra

   print(f"El contador de palabras es: {wordCont}, y la cantidad de palabras que contenian digitos es de: {digitCont}.")



def test():
    enter_text()
test()


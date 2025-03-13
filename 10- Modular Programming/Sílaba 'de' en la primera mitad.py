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
   wordCont = carCont = 0
   text = input("Ingrese un texto y finalice con un punto: ")
   for car in text:
      carCont += 1
      if car == " " or car == ".":
         wordCont += 1
         if carCont != 0 and is_digit(car): 
            print("Contiene digitos")

      if car == ".":
         break



def test():
    enter_text()
test()


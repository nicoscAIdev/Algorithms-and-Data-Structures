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

# Detectamos si es digito
def is_digit(car):
    return car in "0123456789"

# Detectamos si la palabra tiene digito
def has_digit(word):
    for car in word:
        if is_digit(car):
            return True
    return False
# Contamos cuantas palabras tienen digito
def count_words_with_digits(text):
    digit_count = 0
    word = ""

    for car in text:
        word += car
        if car == " " or car == ".":
            if has_digit(word):
                digit_count += 1
            word = ""

    return digit_count

#  Funcion principal
def enter_text():
    text = input("Ingrese un texto y finalice con un punto: ") #Ingresamos el texto
    digit_count = count_words_with_digits(text) #Usamos el input 'text' como parametro en la def count_words_with_digits
    print(f"Cantidad de palabras con al menos un dígito: {digit_count}") #salida

def test():
    enter_text()

test()



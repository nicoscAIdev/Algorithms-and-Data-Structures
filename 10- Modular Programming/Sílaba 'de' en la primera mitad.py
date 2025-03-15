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


def car_count(word, small, medium, large, max):
    length = len(word)
    if length <= 4:
        small += 1
    elif length <= 6:
        medium += 1
    else:
        large += 1

    if length > max:
        max = length

    # Retornamos
    return small, medium, large, max



def de_expression(word, countDe):
    contVuelta = 0
    huboD = False
    mediumWord = len(word) // 2
    for car in word[:mediumWord]:
        contVuelta += 1
        if car == "d" and contVuelta == 1:
            huboD = True
        if car == "e" and contVuelta == 2 and huboD == True:
            countDe += 1
    return countDe  # Retorna el nuevo valor actualizado


# Contamos cuantas palabras tienen digito
def process_text(text):
    small = medium = large = max = countDe = 0
    digit_count = 0
    word = ""

    for car in text:
        word += car
        if car == " " or car == ".":
            if has_digit(word):
                digit_count += 1
            # b)
            small, medium, large, max = car_count(word, small, medium, large, max) 

            # c)
            countDe = de_expression(word, countDe)
            
            # Reiniciamos la var word
            word = ""
    # Retornamos
    return digit_count, small, medium, large, max, countDe


def enter_text(): #  Funcion principal
    
    #Ingresamos el texto
    text = input("Ingrese un texto y finalice con un punto: ")

    #Usamos el input 'text' como parametro en la def 'process_text()'
    digit_count, small, medium, large, max, countDe = process_text(text)
    
    # Salida
    print(f"Cantidad de palabras con al menos un dígito: {digit_count}") 
    print(f"Palabras pequeñas (≤4 letras): {small}") 
    print(f"Palabras medianas (5-6 letras): {medium}") 
    print(f"Palabras grandes (>6 letras): {large}")
    print(f"La palabra mas larga del texto contenia: {max} caracteres")
    print(f"Palabras con De al principio de la palabra: {countDe}")

def test():
    enter_text()
test()
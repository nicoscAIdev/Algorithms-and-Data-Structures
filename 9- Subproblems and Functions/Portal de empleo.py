# Un conocido portal de empleo requiere un programa para validar las búsquedas que se cargan en su página.
# Por cada búsqueda se requiere:

# 1. CUIT:
#    - Validar que sea un texto compuesto por 13 caracteres.
#    - Debe contener solo números y guiones con el formato: 00-00000000-0.

# 2. Descripción de la búsqueda:
#    - Debe ser un texto donde cada palabra se separe con un espacio y termine con un punto.
#    - La descripción debe tener un máximo de 60 caracteres.
#    - Debe contener al menos 3 palabras.
#    - Ninguna palabra debe contener dos mayúsculas seguidas.

# 3. Salario ofrecido:
#    - Debe ser un valor mayor a 0.

# 4. Validación y salida:
#    - Si todos los datos son válidos, mostrar el aviso completo.
#    - En caso contrario, informar que no es posible mostrarlo.

# 5. Control de flujo:
#    - Preguntar al usuario si desea cargar otro aviso o salir del programa.


def validar_cuit(cuit):
    digito = 0
    valido = False
    if len(cuit) == 13:
        if cuit[2] == "-" and cuit[11] == "-":
             for car in cuit:
                 if car in "0123456789":
                    digito += 1
             if digito == 11:
                valido = True
                return valido
             else: print("El cuit ingresado no contiene 11 digitos.")
        else: print("El CUIT ingresado no presenta los guiones '-' en las posiciones 3 y 12.")
    else: print("El CUIT ingresado no contiene 13 caracteres.")

def es_mayuscula(letra):
    if letra >= 'A' and letra <= 'Z':
       return True
    else:
         return False

def validar_desc(desc):
    anterior = " "
    cant_palabras = 0
    if len(desc) <= 60:
        for letra in desc:
            if letra == ' ' or letra == '.':
                cant_palabras += 1

            elif es_mayuscula(letra) and es_mayuscula(anterior):
                print("El texto ingresado no debe contener dos mayusculas seguidas. ")
                return False

            anterior = letra

        if cant_palabras >= 3:
            return True
        else:
            print("La descripcion debe contener al menos 3 palabras. ")


    else: return False


def validar_salario(salario):

    if salario > 0:
        return True
    else:
        print("El salario debe ser mayor a 0! ")
        return False


def principal():
    print("PORTAL DE EMPLEO")
    # datos
    cuit = input("Ingrese numero de CUIT: ")
    desc = input("Ingrese descripcion: ")
    salario = float(input("Ingrese salario: "))

    #proceso
    cuit_valido = validar_cuit(cuit)
    desc_valido = validar_desc(desc)
    salario_valido = validar_salario(salario)

    # Salida
    if cuit_valido and desc_valido and salario_valido:
        print("El cuit: ", cuit)
        print("Realiza la siguiente busqueda: ", desc)
        print("Con un salario de: $", salario)

    else: print("Consulta fallida. ")
principal()
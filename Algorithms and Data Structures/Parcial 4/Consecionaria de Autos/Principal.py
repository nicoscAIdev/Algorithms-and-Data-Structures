# Una concesionaria de autos solicita un programa para gestionar sus ventas.
# Por cada venta se conoce:
# - El nombre del cliente
# - El tipo de venta (valor entre 0 y 3 inclusive)
# - La marca de auto (valor entre 1 y 15)
# - La cantidad de cuotas pagas
# - El monto total del plan

# A través de un menú de opciones, realizar los siguientes puntos:

# 1. Cargar un vector con n ventas, creando todas las validaciones necesarias.
#    La carga puede ser manual, automática o ambas.
#    El arreglo debe generarse de tal manera que siempre esté ordenado por el nombre del cliente.

# 2. Mostrar el contenido del arreglo por consola, un registro por línea.

# 3. Buscar un cliente con el nombre 'nom' (se pasa como parámetro).
#    Si existe, incrementar la cantidad de cuotas en un valor x (leído desde teclado) y mostrar los datos.
#    Si no existe, mostrar un mensaje indicando que no existe.

# 4. A partir del arreglo, generar una matriz [tipo de venta][marca de auto],
#    cada celda debe contener el monto total acumulado.
#    (Total: 4 filas por 15 columnas = 60 contadores).
#    Mostrar solo los valores mayores a cero.

# 5. A partir del arreglo, generar un archivo binario con todas las ventas cuyo monto total facturado sea mayor a un valor 'num' (ingresado por teclado)
#    y que el tipo de venta no sea 2.
#    Mostrar el archivo binario por consola, una venta por línea.
#    Al final del listado mostrar el monto promedio facturado para esos clientes.

# 6. A partir del arreglo, para un rango de marcas de auto (ingresado por teclado),
#    determinar:
#    - Cuántas cuotas pagas se tienen
#    - Qué porcentaje representan dichas cuotas sobre el total de cuotas pagas en general.

from Registro import Consecionaria
import random


def mostrar_menu():
    print("1- Cargar el vector")
    print("2- Mostrar el contenido del arreglo por consola")
    print("3- Buscar un cliente con el nombre 'nom'")
    print("4- Generar una matriz [tipo de venta][marca de auto]")
    print("5- Generar un archivo binario con todas las ventas cuyo monto total facturado sea mayor a un valor ingresado por teclado")
    print("6- Determinar Cuántas cuotas pagas se tienen y qué porcentaje representan dichas cuotas sobre el total de cuotas pagas en general.")
    print("0- Salir")
    opcion = int(input("Ingrese opcion: "))
    return opcion


def validar_mayor():
    n = int(input("Ingrese el valor"))


def principal():
    vector = []
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()

        if opcion == 1:
            n = validar_mayor()
            
            pass
        
        elif opcion == 2:
            pass

        elif opcion == 3:
            pass

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass
     
    pass


if __name__ == "__main__":
    principal()



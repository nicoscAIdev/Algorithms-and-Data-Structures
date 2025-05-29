"""
Turno 2 - Ficha 24 - AED

Se debe desarrollar un programa en Python con al menos DOS módulos:
- Un módulo para la definición del tipo de registro y funciones para gestionarlo.
- Otro módulo con el menú de opciones y control principal del programa.

El programa debe:
1. Cargar un arreglo de registros con los datos de los vehículos, ordenado por identificador.
   - Se debe aplicar el algoritmo de INSERCIÓN ORDENADA CON BÚSQUEDA BINARIA.
   - Se puede hacer carga manual (validando datos) o automática (aleatoria).
   - Si se hace carga manual, toda la carga debe ser manual.
   - Si se hace carga automática, toda la carga debe ser automática.

2. Mostrar todos los vehículos del arreglo, uno por línea.
   - Reemplazar el código de 'tamaño' y 'tipo de motor' por su descripción textual.

3. Buscar un vehículo por identificador.
   - Si el tipo de motor es GNC, Eléctrico o Hidrógeno, mostrar el mensaje: "Opción ecológica".

4. Crear un archivo binario que contenga los vehículos de tamaño MEDIANO o GRANDE.

5. Mostrar el archivo creado y calcular el costo promedio de alquiler de los vehículos ELÉCTRICOS contenidos en el archivo.

Requisitos adicionales:
- El programa debe estar controlado por un MENÚ DE OPCIONES.
- El módulo principal debe incluir el control de ejecución con: if __name__ == "__main__"
- Debe comprimirse la carpeta del proyecto antes de subirla a Aula Virtual.
"""

import pickle
import os

class Vehiculo:
    def __init__(self, ident, tam, motor, costo):
        self.identificador = ident
        self.tam = tam
        self.motor = motor
        self.costo = costo

    def __str__(self):
        tamanios = ['Subcompacto', 'Compacto', 'Mediano', 'Grande']
        motores = ['Nafta', 'Gasoil', 'GNC', 'Eléctrico', 'Hidrógeno']
        return (f"ID: {self.identificador:<5} | Tamaño: {tamanios[self.tam]:<12} | "
                f"Motor: {motores[self.motor]:<10} | Costo x día: ${self.costo:.2f}")

def add_in_order_bin(vec, veh):
    izq, der = 0, len(vec) - 1
    pos = len(vec)
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].identificador == veh.identificador:
            pos = c
            break
        elif veh.identificador < vec[c].identificador:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [veh]

def validar_entre(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        try:
            n = int(input(mensaje))
        except:
            n = inf - 1
        if n < inf or n > sup:
            print("Valor fuera de rango. Intente de nuevo.")
    return n

def validar_mayor_a(lim, mensaje):
    n = lim
    while n <= lim:
        try:
            n = int(input(mensaje))
        except:
            n = lim
        if n <= lim:
            print("Debe ser mayor a", lim)
    return n

def mostrar_vehiculos(vec):
    for v in vec:
        print(v)

def buscar_vehiculo(vec, x):
    izq, der = 0, len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].identificador == x:
            return vec[c]
        elif x < vec[c].identificador:
            der = c - 1
        else:
            izq = c + 1
    return None

def crear_archivo_binario(vec, nombre_archivo):
    with open(nombre_archivo, 'wb') as f:
        for v in vec:
            if v.tam >= 2:  # Mediano o Grande
                pickle.dump(v, f)

def mostrar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("El archivo no existe.")
        return
    with open(nombre_archivo, 'rb') as f:
        print("Vehículos almacenados en archivo:")
        while True:
            try:
                v = pickle.load(f)
                print(v)
            except EOFError:
                break

def costo_promedio_electricos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return 0
    total, cantidad = 0, 0
    with open(nombre_archivo, 'rb') as f:
        while True:
            try:
                v = pickle.load(f)
                if v.motor == 3:  # Eléctrico
                    total += v.costo
                    cantidad += 1
            except EOFError:
                break
    return total / cantidad if cantidad > 0 else 0


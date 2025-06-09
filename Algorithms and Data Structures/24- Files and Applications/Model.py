# EJERCICIO: Gestión ordenada de pacientes en un arreglo y archivo

import pickle

class Paciente:
    def __init__(self, hc, nombre, dias, cod):
        self.hist_clinica = hc
        self.nombre = nombre
        self.fecha = dias
        self.cod_problema = cod

def insertar_ordenado(vector, paciente):
    pos = 0
    while pos < len(vector) and vector[pos].hist_clinica < paciente.hist_clinica:
        pos += 1
    vector.insert(pos, paciente)

def guardar_archivo(vector, nombre_archivo):
    with open(nombre_archivo, 'wb') as arch:
        for pac in vector:
            pickle.dump(pac, arch)

# Carga manual de ejemplo
v = []
insertar_ordenado(v, Paciente(2, "Ana", 10, 7))
insertar_ordenado(v, Paciente(1, "Luis", 5, 8))
guardar_archivo(v, 'pacientes.dat')

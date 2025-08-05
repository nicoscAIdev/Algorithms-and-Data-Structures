# Enunciado: Gestión de Proyectos de una Agencia de Investigación

# Una agencia de investigación requiere un programa para gestionar los proyectos que tiene asignados.
# Por cada proyecto se registran los siguientes datos:
# - número de identificación (entero),
# - nombre descriptivo (cadena),
# - tipo de proyecto (entero de 0 a 19),
# - monto asignado (float),
# - nivel de confidencialidad (entero de 0 a 9).

# Requisitos:
# ✔️ Módulo 1: clase Proyecto con constructor y __str__ definidos.
# ✔️ Módulo 2: programa principal con menú, carga, procesamiento y validaciones.
class Proyecto:
    def __init__(self, idp, titulo, tipo, monto, confidencialidad):
        self.idp = idp                # int
        self.titulo = titulo                          # str
        self.tipo = tipo                              # int de 0 a 19
        self.monto = monto                            # float
        self.confidencialidad = confidencialidad      # int de 0 a 9

    def __str__(self):
        return (f"ID: {self.idp} | Titulo: {self.titulo} | Tipo: {self.tipo} | "
                f"Monto: ${self.monto:.2f} | Confidencialidad: {self.confidencialidad}")

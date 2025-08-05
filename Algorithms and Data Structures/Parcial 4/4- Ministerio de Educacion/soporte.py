# Algoritmos y Estructuras de Datos - Examen Final 22/02/2024 – Regulares
#
# Enunciado General:
# El Ministerio de Educación requiere un programa para gestionar los datos de las becas para estudiantes universitarios
# que se han otorgado. Por cada beca se registran:
# - número de dni (entero) del estudiante,
# - nombre del estudiante (cadena),
# - número entero entre 1 y 10 para el tipo de beca (1: completa, 2: parcial, etc.),
# - número entero entre 1 y 5 para el tipo de carrera (1: ingenierías, 2: sociales, etc.),
# - número en coma flotante para el monto mensual que se pagará por la beca.

class Beca:

    def __init__(self, dni, nom, tipo_beca, tipo_carrera, monto):
        self.dni = dni
        self.nom = nom
        self.tipo_beca = tipo_beca
        self.tipo_carrera = tipo_carrera
        self.monto = monto

    def __str__(self):
        cad = "| ID {:>3} | Nombre {:>10} | TBeca {:>3} | TCarerra {:>3} | Monto {:>3} | "
        return cad.format(self.dni, self.nom, self.tipo_beca, self.tipo_carrera, self.monto)

def test():
    e1 = Beca(200, "aa", 10, 5, 24.4)
    e2 = Beca(100, "bb", 5, 1, 20.0)
    print(e1)
    print(e2)

if __name__ == "__main__":
    test()

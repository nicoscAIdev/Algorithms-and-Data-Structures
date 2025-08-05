# Enunciado General:
# El Ministerio de Educación necesita un programa para gestionar becas otorgadas a estudiantes universitarios.
# Por cada beca se registran:
# - DNI del estudiante (entero)
# - Nombre del estudiante (cadena)
# - Tipo de beca (entero entre 1 y 10)
# - Tipo de carrera (entero entre 1 y 5)
# - Monto mensual que se pagará por esa beca (float)


class Beca:
    
    def __init__(self,dni, nombre, tipo_beca, tipo_carrera, monto):
        self.dni = dni
        self.nombre = nombre
        self.tipo_beca = tipo_beca
        self.tipo_carrera = tipo_carrera
        self.monto = monto

    def __str__(self):
        cad = "DNI: {:>10} | Nombre: {:>10} | tipo Beca: {:>3} | tipo Carrera: {:>3} | monto: {:>3} | "
        return cad.format(self.dni, self.nombre, self.tipo_beca, self.tipo_carrera, self.monto) 
    



def prueba():
    e1 = Beca(44672972, "aaaaa", 1, 5, 210.5)
    e2 = Beca(1000000, "bbbbb", 9, 1, 225.0)
    print(e1)
    print(e2)

if __name__ == "__main__":
    prueba()
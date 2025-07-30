# Enunciado - Centro Deportivo de Alto Rendimiento

# Se registran los datos de los distintos deportistas que se entrenan en el centro.
# De cada deportista se tiene:
# - número identificador (int)
# - nombre (str)
# - número para indicar el deporte (int de 0 a 49)
# - código de tipo de beca (int: 0 completa, 1 media beca, 2 solo cobertura de gastos)
# - monto que se paga por la beca o cobertura (float)


class Centro_Deportivo:
    
    def __init__(self, id, nombre, deporte, codigo, monto):
        self.id = id
        self.nombre = nombre
        self.deporte = deporte
        self.codigo = codigo
        self.monto = monto
        
    def __str__(self):
        cad = "id: {:>3} | nombre: {:>10} | deporte: {:>3} | codigo: {:>3} | monto: {:>3} | "
        return cad.format(self.id, self.nombre, self.deporte, self.codigo, self.monto)
        
def prueba():
    deportista_1= Centro_Deportivo(1, "aaaaaaa", 10, 0, 2.5)
    deportista_2= Centro_Deportivo(1, "bbbbbbb", 20, 2, 1.4)
    print(deportista_1)
    print(deportista_2)


if __name__ =="__main__":
    prueba() 
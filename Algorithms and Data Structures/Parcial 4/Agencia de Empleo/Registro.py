# Modelo Parcial AED - Turno 2 - Enunciado 3 (T2E3)

# Una agencia de empleo desea un programa para procesar los datos de los empleos que tiene disponibles.
# Por cada empleo se registran los siguientes datos:
# - número de identificación del empleo (entero)
# - descripción del empleo (cadena)
# - monto a pagar por ese empleo (float)
# - ciudad en que se ofrece (entero de 0 a 29)
# - tipo de empleo (entero de 0 a 19)



class Agencia:
    

    def __init__(self, id, desc, monto, ciudad, tipo):
        self.id = id
        self.desc = desc
        self.monto = monto
        self.ciudad = ciudad
        self.tipo = tipo
        

    def __str__(self): 
        cadena = "ID: {:>3} | DESC: {:>3} | MONTO: {:>3} | CIUDAD: {:>10} | TIPO: {:>3} |"
        return cadena.format(self.id, self.desc, self.monto, self.ciudad, self.tipo)


def prueba():
    e1 = Agencia(1132, 200, 1500, "San Martin", 2)
    e2 = Agencia(5432, 300, 1200, "Moron", 1)
    print(e1)
    print(e2)


if __name__ == "__main__":
    prueba()
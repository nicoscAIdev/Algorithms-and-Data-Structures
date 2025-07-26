# Una concesionaria de autos solicita un programa para gestionar sus ventas.
# Por cada venta se conoce:
# - El nombre del cliente
# - El tipo de venta (valor entre 0 y 3 inclusive)
# - La marca de auto (valor entre 1 y 15)
# - La cantidad de cuotas pagas
# - El monto total del plan


class Consecionaria:

    def __init__(self, nombre_cliente, id_tipo, id_marca, cant_cuotas, monto_total):
        
        self.nombre_cliente = nombre_cliente
        self.id_tipo = id_tipo
        self.id_marca = id_marca
        self.cant_cuotas = cant_cuotas
        self.monto_total = monto_total
    
    def __str__(self):
        cad = "Nombre: {:>3} | Tipo: {:>3} | Marca: {:>3} | Cuotas: {:>3} | Total: {:>3} |"
        return cad.format(self.nombre_cliente, self.id_tipo, self.id_marca, self.cant_cuotas, self.monto_total)
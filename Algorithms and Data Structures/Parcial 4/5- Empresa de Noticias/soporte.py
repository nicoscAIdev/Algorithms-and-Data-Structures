class Evento:

    def __init__(self, codigo, titulo, descripcion, costo, tipo_evento, segmento):
        self.codigo = codigo
        self.titulo = titulo
        self.descripcion = descripcion
        self.costo = costo
        self.tipo_evento = tipo_evento
        self.segmento = segmento

    def __str__(self):
        cad = "Codigo: {:>10} | titulo: {:>6} | Desc: {:>10} | Costo: {:>3} | Tipo: {:>3} | Segmento: {:>3} | "
        return cad.format(self.codigo, self.titulo, self.descripcion, self.costo, self.tipo_evento, self.segmento)


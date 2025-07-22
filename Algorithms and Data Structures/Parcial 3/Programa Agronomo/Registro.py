

class Trabajo:
    
    def __init__(self, id, desc, tipo, cobro, personal):
        self.id = id
        self.desc = desc
        self.tipo = tipo
        self.cobro = cobro
        self.personal = personal

    def __str__(self):

        cad = 'id: {:>3} | desc: {:>5} | tipo trabajo: {:>5} | cobro importe {:>5} | cant personal {:>5} |'
        return cad.format(self.id, self.desc, self.tipo, self.cobro, self.personal)
    

def prueba():
    t1 = Trabajo(2,"asdasd", 2,1200,30)
    t2 = Trabajo(3,"sadasdsd", 3,1200,30)
    print(t1)
    print(t2)


if __name__ == "__main__":
    prueba()
    
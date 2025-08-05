from soporte import Evento
import random, os, pickle



def mostrar_menu():
    print("1. Generar un arreglo de n Eventos. ")
    print("2. Mostrar el arreglo generado en el punto 1. ")
    print("3. Generar un archivo binario. ")
    print("4. Mostrar el contenido del archivo generado en el punto 3. ")
    print("5. Generar un arreglo unidimensional a partir del archivo generado en el punto 3. ")
    print("6. Determinar si existe un valor del vector generado en el punto 1 que coincida con el valor ingresado por teclado. ")
    print("7. Generar una matriz entre tipos de evento y segmentos. ")
    print("0. Salir. ")
    opcion = int(input("Ingrese una opcion. "))
    return opcion


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        n = int(input(mensaje))
    return n


def generar_vector(n, vector):
    for i in range(n):
        nombres = ("ab", "be", "ci", "do")
        nombres2 = ("na", "ne", "ni", "no")
        codigo = random.choice(nombres) + str(i)
        titulo = random.choice(nombres) + random.choice(nombres) + random.choice(nombres)  
        descripcion = random.choice(nombres2) + random.choice(nombres2) + random.choice(nombres2)
        costo = round(random.uniform(200, 400),2)
        tipo_evento = random.randint(0,19)
        segmento = random.randint(0,9)
        evento = Evento(codigo, titulo, descripcion, costo, tipo_evento, segmento)
        add_in_order(evento, vector)


def add_in_order(evento, vector):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq < der:
        c = (izq + der) // 2
        if evento.codigo == vector[c].codigo:
            pos = c
            break
        elif evento.codigo <= vector[c].codigo:
            der = c - 1
        else:
            izq = c + 1  
    if izq > der:
        pos = izq   
    vector[pos:pos] = [evento]
    

def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])



def crear_archivo(fd, costo_minimo, vector):
    archivo = open(fd, "wb")
    for evento in vector:
        if evento.costo > costo_minimo:
            pickle.dump(evento, archivo)
    archivo.close()


def mostrar_archivo(fd):
    if os.path.exists(fd):
        archivo = open(fd, "rb")
        tam = os.path.getsize(fd)
        while archivo.tell() < tam:
            evento = pickle.load(archivo)
            print(evento)
        archivo.close()
    else:
        print("El archivo no existe. ")


def busqueda_por_codigo(codigo_input, vector):
    for evento in vector:
        if codigo_input == evento.codigo:
            print(evento)
            return evento.descripcion
    print("No existe Evento con el Codigo ingresado. ")


def generar_contador(fd):
    if not os.path.exists(fd):
        print("El archivo no existe.")
        return

    arreglo_costo = []
    with open(fd, "rb") as archivo:
        tam = os.path.getsize(fd)
        while archivo.tell() < tam:
            evento = pickle.load(archivo)
            if evento.tipo_evento >= 5:
                arreglo_costo.append(evento.costo)

    if arreglo_costo:
        for costo in arreglo_costo:
            print(f"${costo}")
        promedio = sum(arreglo_costo) / len(arreglo_costo)
        print(f"\nPromedio de los costos: ${round(promedio,2)}")
    else:
        print("No se encontraron eventos con tipo_evento >= 5.")




def principal():
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
    
        if opcion == 1:
            vector = []
            n = validar_mayor_que(0, "Ingrese la cantidad de Eventos que tendra el portal de noticias. (Debe ser un numero Mayor a 0): ")
            generar_vector(n, vector)

        if opcion == 2:
            mostrar_vector(vector)

        if opcion == 3:
            fd = "eventos.dat"
            costo_minimo = validar_mayor_que(-1.0, "Ingrese el valor minimo del Costo a guardar en el archivo. (Debe ser positivo): ")
            crear_archivo(fd, costo_minimo, vector)
        
        if opcion ==4:
            mostrar_archivo(fd)


        if opcion == 5:
            
            generar_contador(fd, vector)



        if opcion == 6:
            codigo_input = input("Ingrese el codigo de un Evento a buscar: ")
            desc_busqueda = busqueda_por_codigo(codigo_input, vector)


if __name__ == "__main__":
    principal()
def listado_por_dias(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    d = int(input('Días a comprobar desde la última visita: '))
    print('Pacientes con', d, 'o más días desde la última visita')
    for paciente in p:
        if paciente.fecha >= d:
            print(to_string(paciente))
    print()


def mostrar_arreglo(p, mensaje='Contenido:'):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    print(mensaje)
    for paciente in p:
        print(to_string(paciente))
    print()


def buscar(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    x = int(input('Número de historia clínica a buscar: '))
    n = len(p)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].hist_clinica == x:
            print('Paciente encontrado...')
            print(to_string(p[c]))
            print()
            return
        if x < p[c].hist_clinica:
            der = c - 1
        else:
            izq = c + 1
    print('No hay un paciente con ese número de historia clínica')
    print()


def crear_archivo(p):
    global FD
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    print('Grabando todos los datos en el archivo', FD, '...')
    m = open(FD, 'wb')
    for paciente in p:
        pickle.dump(paciente, m)
    m.close()
    print('... hecho')
    print()


def mostrar_archivo():
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')
    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        print(to_string(pac))
    m.close()
    print()


def crear_segundo_arreglo():
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    p2 = []
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')
    print('Creando el segundo vector desde el archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        if pac.cod_problema in [8, 9]:
            p2.append(pac)
    m.close()
    print('... hecho')
    print()
    return p2

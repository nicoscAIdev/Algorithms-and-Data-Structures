def datos(nombre, pais='Argentina', sexo='Varon', trabaja=True, estado='Soltero'):
    print('Datos recibidos: ')
    print('Nombre:', nombre)
    print('Pais:', pais)
    print('Sexo:', sexo)
    print('Tiene trabajo?:', trabaja)
    print('Estado civil:', estado)


def test():
    # ok...
    datos('Luigi', pais='Italia')
    # ok... el parámetro "nombre" tambien puede accederse asi...
    datos(nombre='Luigi', pais='Italia')
    # ok... uno sin palabra clave, otro con palabra clave, y el resto default...
    datos('Camila', 'Argentina', sexo='Mujer')
    # ok... el orden de palabras clave no importa...
    datos('Bruno', sexo='Varon', pais='Italia')
    # error: luego de una palabra clave, no puede seguir explícito...
    # datos('Mary', pais='Inglaterra', 'Mujer')
    # error: no se puede asignar dos veces el mismo parametro...
    # datos('Federico', pais='Argentina', pais='Italia')
    # error: no puede usar un parametro que no existe...
    # datos('Conrado', colegio='Lasalle')
test()
"""
Problema 31:

Una empresa de turismo que vende viajes para egresados de colegios secundarios ofrece 
a tres cursos distintos la siguiente promoción:

- El costo del viaje por persona es de $1360.
- Si el grupo excede las 40 personas, la empresa aplica un descuento del 5% sobre el costo total del viaje para el curso.

Se debe desarrollar un programa que permita determinar:

1. El curso más numeroso.
2. El monto total del viaje para cada curso.
3. El porcentaje que representa el monto del viaje del curso más numeroso sobre el total de la ganancia de la empresa.
"""

def mayor(c1, m1, c2, m2, c3, m3):
    if c1 > c2 and c1 > c3:
        may = m1
        may_cur = 'Primero'
    else:
        if c2 > c3:
            may = m2
            may_cur = 'Segundo'
        else:
            may = m3
            may_cur = 'Tercero'
        return may_cur, may
    

def montos(c1, c2, c3):
    m1 = c1 * 1360
    m2 = c2 * 1360
    m3 = c3 * 1360
    if c1 > 40:
        m1 = m1 - m1/100*5
    if c2 > 40:
        m2 = m2 - m2/100*5
    if c3 > 40:
        m3 = m3 - m3/100*5
    return m1, m2, m3


def porcentaje(m1, m2, m3, may):
    mtot = m1 + m2 + m3
    if mtot != 0:
        porc = may / mtot * 100
    else:
        porc = 0
    return porc


def test():
# título general y carga de datos...
    print('Cálculo de los montos de un viaje de estudios...')
    c1 = int(input('Ingrese la cantidad de alumnos del primer curso: '))
    c2 = int(input('Ingrese la cantidad de alumnos del segundo curso: '))
    c3 = int(input('Ingrese la cantidad de alumnos del tercer curso: '))

# procesos... invocar a las funciones en el orden correcto...
    m1, m2, m3 = montos(c1, c2, c3)
    may_cur, may = mayor(c1, m1, c2, m2, c3, m3)
    porc = porcentaje(m1, m2, m3, may)

# visualización de resultados
    print('El curso mas numeroso es el', may_cur)
    print('El monto del viaje del primer curso es:', m1)
    print('El monto del viaje del segundo curso es:', m2)
    print('El monto del viaje del tercer curso es:', m3)
    print('El porcentaje del monto del mas numeroso en el total es:', porc)

# script principal: sólo invocar a test()...
test()
# Modificacion de la variable sys.path para incluir una subcarpeta de modulos
import sys
sys.path.append('.\\modulos')
# Importacion del modulo "orden" que está en la carpeta "modulos"...
import orden
# función de entrada a modo de prueba...
def test():
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese otro: '))
    men = orden.menor(a, b)
    print('El menor es:', men)
    
# control de solicitud de ejecucion del modulo...
if __name__ == '__main__':
    test()
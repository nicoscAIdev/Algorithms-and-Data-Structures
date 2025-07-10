from vehiculo import *

def main():
    vehiculos = []
    archivo = 'vehiculos.dat'

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Cargar vehículos ordenados por identificador")
        print("2. Mostrar todos los vehículos")
        print("3. Buscar vehículo por identificador")
        print("4. Crear archivo con vehículos medianos o grandes")
        print("5. Mostrar archivo")
        print("6. Costo promedio de alquiler de vehículos eléctricos")
        print("7. Salir")

        op = input("Opción: ")
        if op == '1':
            n = validar_mayor_a(0, "Cantidad de vehículos a registrar: ")
            for i in range(n):
                print(f"\nVehículo #{i+1}")
                ident = validar_mayor_a(0, "Identificador: ")
                tam = validar_entre(0, 4, "Tamaño (0:Subcompacto - 4:Grande): ")
                motor = validar_entre(0, 4, "Motor (0:Nafta - 4:Hidrógeno): ")
                costo = validar_mayor_a(0, "Costo por día: $")
                v = Vehiculo(ident, tam, motor, costo)
                add_in_order_bin(vehiculos, v)

        elif op == '2':
            if len(vehiculos) == 0:
                print("No hay vehículos cargados.")
            else:
                mostrar_vehiculos(vehiculos)

        elif op == '3':
            if len(vehiculos) == 0:
                print("No hay vehículos cargados.")
            else:
                x = int(input("Identificador a buscar: "))
                v = buscar_vehiculo(vehiculos, x)
                if v:
                    print("Vehículo encontrado:")
                    print(v)
                    if v.motor in [3, 4]:
                        print("Opción ecológica!")
                else:
                    print("No se encontró el vehículo.")

        elif op == '4':
            crear_archivo_binario(vehiculos, archivo)
            print("Archivo creado correctamente.")

        elif op == '5':
            mostrar_archivo(archivo)

        elif op == '6':
            promedio = costo_promedio_electricos(archivo)
            if promedio > 0:
                print(f"El costo promedio de vehículos eléctricos es: ${promedio:.2f}")
            else:
                print("No hay vehículos eléctricos en el archivo.")

        elif op == '7':
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

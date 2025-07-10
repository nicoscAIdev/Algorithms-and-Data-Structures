# 📘 Parcial 4 - Gestión de Inscripciones Deportivas en un Colegio

Este proyecto simula un sistema de inscripción de alumnos a actividades deportivas, desarrollado como ejercicio tipo parcial para la cátedra de Algoritmos y Estructuras de Datos (AED).

## 📝 Enunciado

Un colegio secundario requiere un sistema para registrar a los estudiantes que se inscriben a actividades deportivas. Cada alumno se identifica con:
- Un legajo (entero positivo),
- Un nombre (string),
- Un año de cursado (entre 1 y 7),
- Un código de deporte (0 a 9).

Los deportes están codificados de la siguiente forma:
0: Básquet
1: Rugby Seven
2: Tenis
3-9: Otros deportes

## ✅ Funcionalidades del programa

El sistema está controlado por un menú y permite:

1. **Cargar datos de alumnos**
   - Ingreso manual o generación aleatoria.
   - Inserción ordenada por nombre (no se permite cargar todo y ordenar al final).

2. **Buscar alumno por nombre**
   - Si se encuentra, se muestran sus datos. Si no, se informa con un mensaje.

3. **Generar una matriz de conteo**
   - Cuenta la cantidad de alumnos por deporte y año de cursado.
   - Muestra toda la matriz, incluso con contadores en 0.

4. **Crear un archivo binario**
   - Guarda alumnos de un año específico cargado por teclado.
   - Si el archivo ya existe, lo reemplaza.

5. **Mostrar archivo**
   - Muestra el contenido del archivo generado en el punto anterior.

## 🛠️ Tecnologías usadas

- Python 3.x
- Manejo de archivos binarios (`pickle`)
- Módulos: separación del modelo de datos y del controlador principal

## 📂 Estructura del proyecto

📁 parcial4/
├── main.py
├── funciones.py
├── alumno.py
└── README.md

## 🧑‍💻 Autor

Desarrollado por [Nico] para la materia **Algoritmos y Estructuras de Datos** - UTN FRC.

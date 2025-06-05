# Simulacro 1: Segundo Parcial - Paradigmas de Programación

Este repositorio contiene la resolución del Simulacro del Segundo Parcial correspondiente a la materia **Paradigmas de Programación** de la UTN - Facultad Regional Córdoba.

El examen está dividido en dos secciones: **Programación Lógica (Prolog)** y **Programación Funcional (Haskell)**.

---

## 📁 Archivos

- `90049_Sabena_Nicolas.pl`: Resolución de la parte lógica (Prolog)
- `90049_Sabena_Nicolas.hs`: Resolución de la parte funcional (Haskell)

---

## 🧠 Enunciado

### 🧩 Parte 1: Programación Lógica - Prolog

#### 📝 Caso de estudio

Una empresa de streaming de canciones necesita un programa en Prolog que brinde información sobre el contenido de su plataforma. Se proporcionan los siguientes datos:

#### 📋 Tabla 1: Canciones

| Código de pista | Título de la canción             | Fecha de incorporación | Géneros             | Código de discográfica |
|------------------|----------------------------------|-------------------------|---------------------|-------------------------|
| 1                | 'De Música Ligera'              | 31/08/2023              | ['A', 'B', 'C']     | 1                       |
| 2                | 'El Matador'                    | 01/09/2023              | ['B', 'E']          | 2                       |
| 3                | 'Demoliendo hoteles'            | 10/09/2023              | ['A', 'C', 'E']     | 3                       |
| 4                | 'Muchacha (Ojos de papel)'      | 20/09/2023              | ['A']               | 1                       |
| 5                | 'El Amor Después del Amor'      | 01/10/2023              | ['C', 'D', 'E']     | 4                       |

---

#### 🎤 Tabla 2: Intérpretes y Autores de canciones

| Título de la canción             | Intérpretes                  | Autores                             |
|----------------------------------|-------------------------------|--------------------------------------|
| 'De Música Ligera'              | 'Soda Stereo'                | 'Gustavo Cerati y Zeta Bosio'       |
| 'El Matador'                    | 'Los Fabulosos Cadillacs'    | 'Flavio Cianciarulo'                |
| 'Demoliendo hoteles'            | 'Charly García'              | 'Charly García'                     |
| 'Muchacha (Ojos de papel)'      | 'Almendra'                   | 'Luis Alberto Spinetta'             |
| 'El Amor Después del Amor'      | 'Fito Páez'                  | 'Fito Páez'                          |

---

#### 💿 Tabla 3: Discográficas

| Código de discográfica | Nombre de la discográfica |
|------------------------|----------------------------|
| 1                      | 'CBS Discos'               |
| 2                      | 'Sony Music'               |
| 3                      | 'Interdisc'                |
| 4                      | 'Warner Music'             |

---

#### 📌 Reglas a implementar

- **`regla1/6`**: Dados los hechos, obtener para un código de discográfica el código de pista, título de canción, intérprete, año y nombre de la discográfica.
- **`regla2/1`**: Determinar si existen autores que tengan una canción en un determinado mes y cuya discográfica sea la número 1.

---

### 💻 Parte 2: Programación Funcional - Haskell

La empresa también solicita un sistema funcional para las siguientes tareas:

#### 🧮 Funciones requeridas

1. **`funcion1 :: Int -> String`**  
   Devuelve el nombre de la discográfica según el código. Si el código es inválido, retorna `"Código Invalido"`.

##### 📋 Tabla de códigos de discográficas

| Código | Nombre de la discográfica |
|--------|----------------------------|
| 1      | "CBS Discos"               |
| 2      | "Sony Music"               |
| 3      | "Interdisc"                |
| 4      | "Warner Music"             |

---

2. **`funcion2 :: [Int] -> Int -> Int`**  
   Recibe una lista con las reproducciones de canciones y un valor de referencia. Devuelve la cantidad de elementos de la lista menores al valor dado.

Ejemplo:
```haskell
Main> funcion2 [4, 5, 2, 8] 3
Resultado = 1


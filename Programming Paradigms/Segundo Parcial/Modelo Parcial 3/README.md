# 📚 Segundo Parcial – Paradigmas de Programación (Turno 4)

Este repositorio contiene la resolución del Segundo Parcial Turno 4 de la materia **Paradigmas de Programación**, abordando los paradigmas **Funcional (Haskell)** y **Lógico (Prolog)**.

---

## 📁 Estructura del repositorio

- `Legajo_ApellidoNombre.hs`: desarrollo en Haskell.
- `Legajo_ApellidoNombre.pl`: desarrollo en Prolog.
- `README.md`: este archivo con consignas y estructura del parcial.

---

## 🔷 Parte A – Programación Funcional (Haskell)

### 📋 Tabla: Tipos de libros

| Código | Descripción           | Precio unitario |
|--------|------------------------|------------------|
| "NF"   | novela de ficción      | 12.5             |
| "NA"   | novela de aventuras    | 15.0             |
| "CF"   | ciencia ficción        | 18.0             |
| "T"    | teatro                 | 10.0             |

### ✏️ Consignas

1. **`funcion1`**  
   Recibe el código de un libro y devuelve su precio de venta.  
   Si el código no está en la tabla, retorna `0.0`.

2. **`funcion2`**  
   Recibe una lista de precios y dos valores (`min`, `max`).  
   Devuelve una lista con los precios que están en ese rango (inclusive).

3. **`funcion3`**  
   Recibe una lista de precios y un valor de referencia `ref`.  
   Devuelve la suma de los precios **mayores** a `ref`.  
   Debe utilizar recursividad.

---

## 🔷 Parte B – Programación Lógica (Prolog)

### 📋 Tablas incluidas

#### 🧪 Tabla 1: Fármacos

| Código | Nombre       | Stock | Costo Unitario | Sucursal | Categorías                      |
|--------|--------------|-------|----------------|----------|---------------------------------|
| '0001' | Paracetamol  | 200   | 200            | 1        | ['Libre', 'Antifebril']         |
| '0002' | Ibuprofeno   | 300   | 400            | 2        | ['Libre']                       |
| '0003' | Salbutamol   | 150   | 800            | 1        | ['Recetado', 'Broncodilatador'] |
| '0004' | Decidex      | 50    | 500            | 3        | ['Recetado', 'Antihistamínico'] |

#### 📦 Tabla 2: Órdenes de distribución

| Código | Fármaco | Responsable   | Fecha           | Cantidad | Cant. por paquete |
|--------|---------|----------------|------------------|----------|--------------------|
| 'R001' | '0002'  | López Maria    | 15/07/2024       | 50       | 10                 |
| 'R002' | '0003'  | Gómez Pedro    | 02/08/2024       | 80       | 5                  |
| 'R003' | '0001'  | Díaz Ana       | 10/08/2024       | 100      | 20                 |
| 'R004' | '0004'  | Pérez Juan     | 22/08/2024       | 60       | 10                 |

#### 🏢 Tabla 3: Sucursales

| Código | Descripción |
|--------|-------------|
| 1      | Central     |
| 2      | Norte       |
| 3      | Sur         |

---

### ✏️ Consignas

1. **`regla1/6`**  
   Para todas las órdenes de distribución de fármacos cuyo **stock > 200**, retornar:
   - Código del fármaco
   - Denominación
   - Descripción de la sucursal
   - Costo unitario
   - Cantidad total de paquetes  
   (Cantidad total de paquetes = cantidad distribuida / cantidad por paquete)

2. **`regla2/2`**  
   Recibe una **categoría** como argumento.  
   Devuelve una **lista de nombres de fármacos** que:
   - tengan `costo_unitario >= 200`
   - **no** pertenezcan a la sucursal `'Central'`
   - incluyan la categoría especificada

---

## 🛠️ Ejemplos de uso

### En Haskell (GHCi)

```haskell
:l Legajo_ApellidoNombre.hs

funcion1 "CF"         -- 18.0
funcion2 [12.5, 18.0] 12.0 16.0  -- [12.5]
funcion3 [10.0, 15.0, 18.0] 15.0 -- 18.0

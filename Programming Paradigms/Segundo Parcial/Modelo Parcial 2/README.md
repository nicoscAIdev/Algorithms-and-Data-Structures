# 🧪 Segundo Parcial – Paradigmas de Programación (Turno 3)

Este repositorio contiene la resolución del Segundo Parcial correspondiente al Turno 3 de la materia **Paradigmas de Programación**, abordando tanto el paradigma **Funcional (Haskell)** como el **Lógico (Prolog)**.

---

## 📁 Estructura del Repositorio

- `Legajo_ApellidoNombre.hs`: contiene la resolución de los ejercicios en Haskell.
- `Legajo_ApellidoNombre.pl`: contiene la resolución de los ejercicios en Prolog.
- `README.md`: archivo actual con consignas y descripción.

---

## 🔷 Parte A: Programación Funcional (Haskell)

**Contexto:** Una librería vende diferentes tipos de libros. Se trabaja con el código, descripción y número de páginas.

### ✅ Tabla de libros

| Código | Descripción            | Páginas |
|--------|------------------------|---------|
| "NF"   | Novela de ficción      | 350     |
| "NA"   | Novela de aventuras    | 420     |
| "CF"   | Ciencia ficción        | 280     |
| "T"    | Teatro                 | 120     |

### 📌 Consignas

1. **`funcion1`**  
   Recibe el código de un tipo de libro y retorna el número de páginas.  
   Si el código no figura en la tabla, debe devolver 0.

2. **`funcion2`**  
   Recibe una lista de números de páginas y un valor de referencia `ref`.  
   Devuelve una lista con los números mayores o iguales a `ref`.

3. **`funcion3`**  
   Recibe una lista de códigos y un código de tipo de libro.  
   Retorna cuántos elementos de la lista son iguales al valor recibido.  
   Debe resolverse con recursividad.

---

## 🔷 Parte B: Programación Lógica (Prolog)

**Contexto:** Una empresa distribuye fármacos y desea consultar sobre sus órdenes, fármacos y sucursales.

### ✅ Tablas de ejemplo (hechos ya definidos)

- `farmaco/6`
- `orden_distribucion/6`
- `sucursal/2`

### 📌 Consignas

1. **`regla1/6`**  
   Para una orden dada, retornar:  
   Código del fármaco, denominación, mes de la orden, cantidad por paquete y costo total.  
   `CostoTotal = cantidad * costo_unitario`.

2. **`regla2/2`**  
   Dado un valor mínimo de stock, retornar la lista de descripciones de sucursales que:
   - tengan fármacos con stock mayor al valor
   - cuya orden fue en el mes 8
   - y su categoría incluye `'Recetado'`

---

## ✅ Instrucciones de ejecución

### En Haskell (GHCi)
```haskell
:l Legajo_ApellidoNombre.hs
funcion1 "NF"
funcion2 [280, 420, 120] 300
funcion3 ["CF", "CF", "T"] "CF"

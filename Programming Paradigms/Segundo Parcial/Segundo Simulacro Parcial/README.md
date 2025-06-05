# Simulacro del Segundo Parcial - Paradigmas de Programación

Este repositorio contiene la resolución del Simulacro del Segundo Parcial correspondiente a la materia **Paradigmas de Programación** de la UTN - Facultad Regional Córdoba.

El examen está dividido en dos partes: **Programación Lógica (Prolog)** y **Programación Funcional (Haskell)**.

---

## 📁 Archivos

- `90049_Sabena_Nicolas.pl`: Resolución de la parte lógica (Prolog)
- `90049_Sabena_Nicolas.hs`: Resolución de la parte funcional (Haskell)

---

## 🧠 Enunciado

### 🧩 Parte 1: Programación Lógica - Prolog

#### 📝 Caso de estudio

Una farmacia que vende productos online necesita un sistema que brinde información sobre ventas y productos registrados.

---

### 📋 Tabla 1: Productos

| Código Prod. | Denominación        | Stock | Precio Unitario | Código Categoría | Proveedores           |
|--------------|---------------------|-------|------------------|------------------|------------------------|
| '00001'      | 'Shampoo niños'     | 300   | 250              | 1                | ['A', 'B', 'C']        |
| '00002'      | 'Jabón líquido'     | 500   | 425              | 1                | ['A', 'B']             |
| '00003'      | 'Fragancia floral'  | 400   | 4800             | 3                | ['C']                  |
| '00004'      | 'Crema hidratante'  | 550   | 4500             | 2                | ['A', 'C']             |

---

### 🧾 Tabla 2: Venta de Productos

| Código Venta | Código Producto | Cliente             | Fecha Venta | Cantidad Pedida | Descuento (%) |
|--------------|------------------|----------------------|-------------|------------------|----------------|
| '11111'      | '00002'          | 'Pérez Juan'         | 11/05/2022  | 30               | 0              |
| '22222'      | '00003'          | 'Sarmiento Tomás'    | 05/04/2022  | 150              | 5              |
| '33333'      | '00001'          | 'Trotta Paola'       | 12/05/2022  | 260              | 5              |
| '44444'      | '00004'          | 'Altamirano Noé'     | 16/05/2022  | 50               | 0              |

---

### 🏷️ Tabla 3: Categorías

| Código Categoría | Descripción Categoría       |
|------------------|-----------------------------|
| 1                | 'Cuidado personal'          |
| 2                | 'Dermocosmética'            |
| 3                | 'Perfumes y fragancias'     |

---

### 📌 Reglas a implementar

1. **`regla1/5`**: Dado un código de venta, retornar: cliente, cantidad pedida, denominación del producto y su precio unitario.  
   Ejemplo:
   ```prolog
   regla1('22222', Cli, Cant, Denom, Pre).
   Cli = 'Sarmiento Tomás'
   Cant = 150
   Denom = 'Fragancia floral'
   Pre = 4800

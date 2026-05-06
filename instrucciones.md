# Guía Completa de Instrucciones - Finanzas CLI 💰

Bienvenido a la guía oficial de usuario. Este programa está diseñado para darte control total sobre tus finanzas personales desde la terminal, permitiéndote gestionar periodos mensuales, ingresos, egresos y gastos recurrentes.

---

## 1. Conceptos Fundamentales

### Periodos
La información se organiza por **Mes** y **Año**. Cada movimiento pertenece a un periodo específico. Si intentas agregar un movimiento a un periodo que no existe, el programa te preguntará si deseas crearlo.

### Egresos vs Ingresos
- **Ingreso**: Dinero que entra (Salario, ventas, etc.).
- **Egreso**: Dinero que sale (Renta, comida, servicios). **Nota**: Hemos eliminado el término "Gasto" para estandarizar a "Egreso".

### Conceptos Recurrentes (Plantillas)
Si marcas un egreso como **Recurrente**, se convertirá en una plantilla. Cada vez que crees un mes nuevo (ej. pasas de Enero a Febrero), el programa copiará automáticamente todos tus egresos recurrentes al nuevo mes con un valor inicial de $0.0 para que solo tengas que actualizarlos.

---

## 2. Comandos Disponibles

### `dashboard`
Muestra el resumen visual de tus finanzas.
- **Uso**: `python main.py dashboard`
- **Parámetros**:
    - `--mes [1-12]`: Ver un mes específico.
    - `--año [AAAA]`: Ver un año específico.
- **Ejemplo**: `python main.py dashboard --mes 12 --año 2025`

### `add`
Registra una nueva transacción.
- **Uso**: `python main.py add [tipo] [monto] "[nombre]"`
- **Parámetros**:
    - `tipo`: Debe ser `ingreso` o `egreso`.
    - `monto`: Un número positivo.
    - `nombre`: Descripción del concepto (debe empezar con una letra).
    - `--mes` / `--año`: (Opcional) Indica el periodo.
    - `--recurrente`: (Opcional) Activa esta opción para gastos fijos mensuales.
- **Ejemplo**: `python main.py add egreso 1200 "Renta" --recurrente`

### `list`
Muestra todos los movimientos de un periodo en una tabla con sus **IDs**.
- **Uso**: `python main.py list`
- **Parámetros**: `--mes`, `--año`.
- **Ejemplo**: `python main.py list --mes 5`

### `delete`
Elimina un registro de forma inteligente.
- **Uso**: `python main.py delete [ID]`
- **Comportamiento**:
    - Si el registro es único, se borra definitivamente.
    - Si es un concepto recurrente con historial, se desactiva para el futuro pero se mantiene en los registros pasados.

### `set-meta`
Define tu objetivo de ahorro total.
- **Uso**: `python main.py set-meta [monto]`
- **Ejemplo**: `python main.py set-meta 20000`

### `balance`
Muestra rápidamente tu saldo acumulado histórico sin entrar al dashboard completo.
- **Uso**: `python main.py balance`

---

## 3. Reglas de Validación

Para mantener tus datos limpios, el programa aplica las siguientes reglas:
1. **Nombres**: Todo concepto debe iniciar con una letra (no números ni símbolos al inicio).
2. **Montos**: No se permiten valores negativos.
3. **IDs**: Las operaciones de modificación o borrado requieren el ID numérico exacto que aparece al ejecutar el comando `list`.

---

## 4. Soporte Técnico y Datos

- **Base de Datos**: Se utiliza SQLite. El archivo se encuentra en `~/.Finanzas_3/finanzas/finanzas.db`. No lo borres si quieres conservar tu historial.
- **Dependencias**: Requiere la librería `rich` para la interfaz visual.

---
*Fin de las instrucciones.*

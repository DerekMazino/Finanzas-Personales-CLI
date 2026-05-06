## Context

La aplicación actual tiene una estructura modular básica pero incompleta. El manejo de la base de datos utiliza SQL crudo y no soporta conceptos avanzados como la recurrencia o la protección de historial. Además, existe una inconsistencia terminológica entre "Gasto" y "Egreso".

## Goals / Non-Goals

**Goals:**
- Implementar un esquema de base de datos relacional robusto (Opción B: Plantillas vs Transacciones).
- Estandarizar la terminología a "Egreso".
- Implementar validaciones de datos en la entrada del CLI.
- Asegurar que la creación de periodos sea un proceso que incluya la propagación de gastos recurrentes.
- Proteger el historial financiero mediante eliminaciones lógicas (soft-delete).

**Non-Goals:**
- No se implementará autenticación de usuarios.
- No se incluirán reportes gráficos complejos (fuera de tablas en consola).
- No se manejarán múltiples divisas.

## Decisions

### 1. Modelo de Datos (Esquema Separado)
Se crearán tablas separadas para plantillas recurrentes y registros individuales:
- `periodos`: (id, mes, año)
- `plantillas_recurrentes`: (id, nombre, tipo, activo)
- `transacciones`: (id, periodo_id, plantilla_id [NULLABLE], nombre, monto, tipo, fecha_creacion)

### 2. Query Builder
Para mantener el código "Junior Friendly" pero evitar errores de SQL crudo, se implementará un Query Builder liviano interno que genere las sentencias básicas (SELECT, INSERT, UPDATE, DELETE).

### 3. Lógica de Recurrencia
Al crear un nuevo periodo (F1), el sistema buscará todas las `plantillas_recurrentes` con `activo = 1` y creará registros correspondientes en la tabla `transacciones` para ese nuevo periodo.

### 4. Borrado Inteligente (ID-Based)
La eliminación de conceptos se basará en su **ID**. 
- Si un concepto (plantilla) tiene transacciones asociadas en otros periodos, el borrado será lógico (`activo = 0`).
- Si es un concepto recién creado sin historial, se podrá realizar un borrado físico.

## Risks / Trade-offs

- **Complejidad de la base de datos**: Separar plantillas de transacciones añade una tabla extra y joins, pero asegura la integridad a largo plazo.
- **Sincronización de nombres**: Cambiar el nombre de una plantilla solo afectará a transacciones futuras para no alterar el pasado, lo cual requiere una lógica clara en el servicio.

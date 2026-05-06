## Context

El proyecto consiste en una herramienta CLI para gestionar finanzas personales. Actualmente no existe una base de código, por lo que este diseño establece la arquitectura inicial. Se requiere persistencia local, una interfaz visual amigable en terminal y una lógica clara para el cálculo de ahorros.

## Goals / Non-Goals

**Goals:**
- Implementar una arquitectura modular (Capa de datos, Capa de negocio, Capa de UI).
- Garantizar la integridad de los datos mediante el uso correcto de SQLite.
- Crear una interfaz CLI intuitiva usando comandos directos y una vista de dashboard.
- Seguir principios de POO y código limpio (PEP8).

**Non-Goals:**
- No se implementará autenticación de usuarios.
- No se integrará con APIs externas o servicios en la nube.
- No se soportarán múltiples divisas simultáneamente (se asume una divisa base).
- No se requiere una interfaz gráfica de usuario (GUI).

## Decisions

### 1. Arquitectura del Sistema
Se utilizará un enfoque de capas simplificado para mantener la mantenibilidad:
- **Entidades**: Clases puras para `Periodo`, `Transaccion` y `Meta`.
- **Repositorios**: Manejo de la persistencia usando `sqlite3`.
- **Servicios**: Lógica de cálculo (balance, progreso de ahorro).
- **CLI/UI**: Gestión de argumentos y renderizado con `rich`.

### 2. Esquema de Base de Datos
Se utilizarán tres tablas principales:
- `periodos`: (id, mes, año) - Índice único en (mes, año).
- `transacciones`: (id, periodo_id, tipo, monto, descripcion, fecha).
- `configuracion`: (clave, valor) - Para almacenar la meta de ahorro global de forma persistente.

### 3. Interfaz de Usuario
Se optará por el uso de la librería `rich` para:
- Renderizar el dashboard en tablas legibles.
- Usar paneles para separar el resumen mensual del ahorro acumulado.
- Proporcionar feedback visual (colores) para saldos positivos (verde) y negativos (rojo).

### 4. Gestión de Periodos
El sistema detectará automáticamente el mes y año actual al iniciar. Las transacciones se vincularán al periodo correspondiente. Si un periodo no existe al agregar una transacción, se creará automáticamente.

## Risks / Trade-offs

- **[Riesgo] Corrupción de base de datos** → **[Mitigación]** Realizar commits atómicos en SQLite y validar que el directorio exista antes de escribir.
- **[Riesgo] Complejidad en la navegación** → **[Mitigación]** Mantener comandos directos simples (`add`, `list`, `delete`) y un comando `dashboard` central.
- **[Trade-off] SQLite vs JSON** → Se elige SQLite por su capacidad de consulta SQL y escalabilidad futura, a pesar de requerir un poco más de código inicial que un archivo JSON.

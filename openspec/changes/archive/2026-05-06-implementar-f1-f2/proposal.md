## Why

Implementar las funcionalidades principales del CLI de Finanzas Personales. Actualmente tenemos una base mínima, pero necesitamos formalizar la gestión de periodos (F1) y la gestión de ingresos/egresos (F2) con lógica de recurrencia y protección de historial.

## What Changes

- Implementación de la lógica de negocio para la creación y listado de periodos mensuales.
- Implementación de la gestión de transacciones (ingresos y egresos) con identificadores únicos (ID).
- Inclusión de validaciones de datos (nombres que empiecen por letra, montos positivos).
- Lógica de recurrencia: los conceptos marcados como recurrentes se propagan a nuevos periodos.
- Lógica de eliminación inteligente: borrado físico si no hay historial, o lógico (inactivación) si el concepto ya ha sido usado.
- Actualización de la arquitectura para usar un Query Builder liviano y separar Plantillas de Transacciones.

## Capabilities

### New Capabilities
- `gestion-periodos`: Creación y listado de periodos mensuales (Mes/Año) con sugerencia de creación automática.
- `gestion-egresos-ingresos`: CRUD de transacciones con validaciones, IDs únicos y manejo de recurrencia lógica.

### Modified Capabilities
- Ninguna.

## Impact

- Base de Datos: Nuevas tablas (`plantillas_recurrentes`, `periodos`, `transacciones` actualizadas).
- Repositorios: Nuevos métodos para manejar la lógica de "borrado inteligente" y copia de recurrentes.
- CLI: Nuevos comandos y mejora de los existentes para soportar IDs y flujo interactivo.

## Why

Este proyecto surge de la necesidad de contar con una herramienta CLI simple y efectiva para la gestión de finanzas personales. El objetivo es permitir a los usuarios rastrear sus ingresos y gastos mensualmente, calcular su ahorro real (ingresos - egresos) y visualizar el progreso hacia metas de ahorro acumuladas. Además, sirve como un caso de estudio para la definición de sistemas usando OpenSpec y generación de código asistida por IA.

## What Changes

- **Nueva CLI de Finanzas**: Implementación de una interfaz de línea de comandos en Python.
- **Persistencia con SQLite**: Creación de una base de datos local para almacenar transacciones, periodos y metas.
- **Gestión de Periodos**: Sistema de organización basado estrictamente en meses naturales (Mes/Año).
- **Seguimiento de Ahorro**: Lógica para calcular el balance mensual y el ahorro acumulado histórico.
- **Dashboard Interactivo**: Visualización resumida del estado financiero actual y progreso de metas.

## Capabilities

### New Capabilities
- `period-management`: Lógica para crear, listar y seleccionar periodos mensuales (Mes/Año).
- `transaction-management`: Funcionalidades para agregar, modificar, eliminar y listar ingresos y gastos vinculados a periodos.
- `savings-tracking`: Cálculo de balance mensual, ahorro acumulado total y seguimiento de metas globales opcionales.

### Modified Capabilities
- Ninguna (proyecto nuevo).

## Impact

- **Código**: Creación de una nueva estructura de proyecto Python siguiendo principios de POO.
- **Datos**: Creación de una base de datos SQLite en `~/.Finanzas_3/finanzas/finanzas.db`.
- **Dependencias**: Se utilizará `sqlite3` (nativo) y potencialmente `rich` para la interfaz visual.

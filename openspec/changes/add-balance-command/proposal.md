## Why

A veces el usuario solo quiere saber cuánto dinero tiene en total de forma rápida, sin necesidad de ver todo el desglose del dashboard mensual. Este comando proporciona esa información de manera inmediata.

## What Changes

- **Nuevo comando `balance`**: Se añade un comando a la CLI que muestra únicamente el ahorro acumulado total y el estatus de la meta (si existe).

## Capabilities

### New Capabilities
- Ninguna.

### Modified Capabilities
- `savings-tracking`: Se añade el requerimiento de acceso rápido al balance global mediante un comando específico.

## Impact

- **CLI**: Modificación de `main.py` para incluir el nuevo subcomando.
- **UI**: Nueva función simple en `cli.py` para mostrar solo el balance.

## Context

La infraestructura actual ya cuenta con la lógica para calcular el ahorro acumulado en `FinanzasService`. Solo falta exponer esta información a través de un comando dedicado en el punto de entrada de la aplicación.

## Goals / Non-Goals

**Goals:**
- Proporcionar una respuesta rápida y minimalista con el saldo total.
- Reutilizar la lógica de negocio existente.

**Non-Goals:**
- No mostrar transacciones ni detalles del mes actual en este comando.

## Decisions

### 1. Reutilización de Lógica
Se utilizará el método `service.get_global_savings()` ya implementado para obtener los datos de ahorro acumulado y meta.

### 2. Interfaz Minimalista
Se añadirá un método `show_balance_only` en `CLIInterface` que use un estilo simple de `rich` (quizás un solo panel o texto formateado) para mostrar el dato.

## Risks / Trade-offs

- **[Trade-off] Redundancia** → Aunque el dashboard ya muestra esta información, el comando `balance` ahorra tiempo al usuario y espacio en el terminal.

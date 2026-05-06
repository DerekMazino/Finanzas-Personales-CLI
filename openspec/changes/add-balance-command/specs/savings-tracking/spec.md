## ADDED Requirements

### Requirement: Comando de balance rápido
El sistema DEBE (SHALL) proporcionar un comando específico para visualizar únicamente el ahorro acumulado total y el estatus de la meta global.

#### Scenario: Consulta de balance rápido
- **WHEN** el usuario ejecuta el comando `balance`
- **THEN** el sistema MUESTRA el ahorro acumulado total de forma prominente y el porcentaje de meta si está configurada

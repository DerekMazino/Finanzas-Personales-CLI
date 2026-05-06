# transaction-management Specification

## Purpose
TBD - created by archiving change finanzas-personales-cli. Update Purpose after archive.
## Requirements
### Requirement: Registro de ingresos y gastos
El sistema DEBE (SHALL) permitir registrar transacciones especificando descripción, monto y tipo (ingreso o gasto).

#### Scenario: Agregar transacción exitosa
- **WHEN** el usuario ingresa un comando para agregar un ingreso de 100 con la descripción "Venta"
- **THEN** el sistema GUARDA la transacción en la base de datos vinculada al periodo actual

### Requirement: Eliminación de transacciones
El sistema DEBE (SHALL) permitir eliminar transacciones existentes mediante su ID único.

#### Scenario: Eliminar transacción por ID
- **WHEN** el usuario ingresa el comando de eliminar indicando un ID válido
- **THEN** el sistema ELIMINA el registro correspondiente de la base de datos y confirma la acción

### Requirement: Listado de transacciones por periodo
El sistema DEBE (SHALL) permitir visualizar todas las transacciones de un periodo específico.

#### Scenario: Listar transacciones del mes
- **WHEN** el usuario solicita ver las transacciones de Mayo 2024
- **THEN** el sistema MUESTRA una tabla detallada con descripción, monto y tipo de cada movimiento en ese mes


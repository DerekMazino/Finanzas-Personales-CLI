# period-management Specification

## Purpose
TBD - created by archiving change finanzas-personales-cli. Update Purpose after archive.
## Requirements
### Requirement: Mes y Año como clave de periodo
El sistema DEBE (SHALL) organizar toda la información financiera en periodos mensuales definidos por un mes (1-12) y un año.

#### Scenario: Creación automática de periodo
- **WHEN** el usuario agrega una transacción para un mes/año que no existe en la base de datos
- **THEN** el sistema CREA automáticamente el registro del periodo antes de guardar la transacción

### Requirement: Listado de periodos
El sistema DEBE (SHALL) permitir listar todos los periodos que contienen transacciones.

#### Scenario: Mostrar periodos existentes
- **WHEN** el usuario solicita el comando de listar periodos
- **THEN** el sistema MUESTRA una tabla con los periodos registrados, ordenados cronológicamente


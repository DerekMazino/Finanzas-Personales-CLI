## ADDED Requirements

### Requirement: Cálculo de balance mensual
El sistema DEBE (SHALL) calcular automáticamente el balance de cada periodo restando los gastos de los ingresos.

#### Scenario: Balance positivo
- **WHEN** un periodo tiene $2000 en ingresos y $1500 en gastos
- **THEN** el sistema CALCULA un balance (ahorro del mes) de $500

### Requirement: Ahorro acumulado global
El sistema DEBE (SHALL) calcular la suma de todos los balances de todos los periodos registrados para obtener el ahorro acumulado total.

#### Scenario: Visualización de ahorro histórico
- **WHEN** el usuario abre el dashboard
- **THEN** el sistema MUESTRA el total acumulado ahorrado desde el inicio del registro

### Requirement: Meta de ahorro opcional
El sistema DEBE (SHALL) permitir definir una meta de ahorro global y mostrar el progreso hacia ella.

#### Scenario: Progreso con meta definida
- **WHEN** hay una meta de $10,000 y el ahorro acumulado es de $2,500
- **THEN** el sistema MUESTRA que el progreso es del 25% y faltan $7,500

#### Scenario: Sin meta definida
- **WHEN** no existe una meta configurada
- **THEN** el sistema MUESTRA el ahorro acumulado pero no indica porcentajes ni faltantes de meta

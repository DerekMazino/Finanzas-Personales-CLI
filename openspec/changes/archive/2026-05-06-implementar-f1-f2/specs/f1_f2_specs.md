## ADDED Requirements

### Requirement: Gestión de Periodos (F1)
El sistema debe permitir administrar los periodos mensuales de manera robusta.

#### Scenario: Creación interactiva de periodo actual
- **WHEN** El usuario intenta agregar un concepto a un periodo que no existe (ej. el mes actual).
- **THEN** El sistema pregunta si desea crearlo. Si acepta, se crea el periodo y se copian los conceptos recurrentes.

### Requirement: Gestión de Conceptos con IDs (F2)
El sistema debe permitir CRUD de ingresos y egresos usando identificadores numéricos.

#### Scenario: Validación de nombre
- **WHEN** El usuario ingresa un nombre que no comienza con una letra del alfabeto.
- **THEN** El sistema rechaza la entrada con un mensaje de error.

### Requirement: Recurrencia Inteligente
Los conceptos marcados como recurrentes deben automatizar la carga de datos futura.

#### Scenario: Modificación de nombre diferida
- **WHEN** El usuario modifica el nombre de un concepto recurrente.
- **THEN** El cambio se refleja en la plantilla para periodos futuros, pero se mantiene el nombre original en el historial pasado.

#### Scenario: Eliminación inteligente
- **WHEN** El usuario elimina un concepto.
- **THEN** Si el concepto tiene historial en otros meses, se marca como inactivo (eliminación lógica). Si es nuevo sin historial, se elimina físicamente.

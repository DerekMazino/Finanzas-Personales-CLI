## 1. Base de Datos y Modelos

- [x] 1.1 Actualizar `DatabaseManager` para crear las tablas `periodos`, `plantillas_recurrentes` y `transacciones` (con el nuevo esquema de la Opción B).
- [x] 1.2 Implementar un `QueryBuilder` liviano en `proyecto/database/utils.py`.
- [x] 1.3 Actualizar las entidades en `proyecto/models/entities.py` para incluir los nuevos campos (`activo`, `plantilla_id`, `fecha_creacion`).

## 2. Capa de Repositorios

- [x] 2.1 Crear `PlantillaRepository` para gestionar los conceptos recurrentes.
- [x] 2.2 Implementar la lógica de "Eliminación Inteligente" en los repositorios (física vs lógica).
- [x] 2.3 Adaptar `TransaccionRepository` para usar el Query Builder y trabajar con IDs numéricos.

## 3. Lógica de Negocio (Servicios)

- [x] 3.1 Implementar en `FinanzasService` la lógica de propagación de recurrentes al crear un nuevo periodo.
- [x] 3.2 Añadir validaciones de negocio (nombre que inicie con letra, monto positivo) en la capa de servicio.
- [x] 3.3 Estandarizar toda la lógica interna para usar el término "Egreso".

## 4. Interfaz de Usuario (CLI)

- [x] 4.1 Actualizar `main.py` para soportar comandos basados en ID (`delete <id>`, `edit <id>`).
- [x] 4.2 Implementar el flujo interactivo: si el periodo no existe al agregar un egreso, preguntar si se desea crear.
- [x] 4.3 Mejorar la visualización de tablas en `proyecto/ui/cli.py` usando `Rich`.

## 5. Verificación y Pruebas

- [x] 5.1 Crear tests unitarios con `pytest` para validar la copia de recurrentes y la eliminación lógica.
- [x] 5.2 Realizar pruebas manuales de los flujos críticos (E2E).

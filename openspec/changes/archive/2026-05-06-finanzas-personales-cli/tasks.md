## 1. Inicialización y Entorno

- [x] 1.1 Crear la estructura de directorios del proyecto (`proyecto/`, `proyecto/database/`, `proyecto/ui/`, etc.)
- [x] 1.2 Configurar el entorno virtual e instalar dependencias iniciales (`rich`)
- [x] 1.3 Implementar la clase `DatabaseManager` para gestionar la conexión y creación de tablas en SQLite

## 2. Capa de Datos (Modelos y Repositorios)

- [x] 2.1 Definir las entidades `Periodo`, `Transaccion` y `Meta` como clases Python
- [x] 2.2 Implementar el repositorio de Periodos (Creación, búsqueda por mes/año)
- [x] 2.3 Implementar el repositorio de Transacciones (CRUD)
- [x] 2.4 Implementar la gestión de configuración para la Meta de Ahorro

## 3. Lógica de Negocio (Servicios)

- [x] 3.1 Implementar `FinanzasService` para el cálculo de balance mensual
- [x] 3.2 Implementar la lógica de cálculo de ahorro acumulado global
- [x] 3.3 Implementar la lógica de cálculo de progreso de meta (opcional)

## 4. Interfaz de Usuario (CLI y Dashboard)

- [x] 4.1 Configurar `argparse` para manejar los comandos principales (`add`, `list`, `delete`, `set-meta`, `dashboard`)
- [x] 4.2 Crear los componentes visuales con `rich` (Tablas para transacciones, Paneles para el dashboard)
- [x] 4.3 Implementar el comando `dashboard` con la visualización resumida y progreso de ahorro

## 5. Verificación y Pulido

- [x] 5.1 Realizar pruebas manuales de flujo completo (Crear periodo -> Agregar transacciones -> Ver dashboard)
- [x] 5.2 Validar el manejo de errores (Entradas inválidas, base de datos bloqueada)
- [x] 5.3 Asegurar el cumplimiento de PEP8 y limpieza de código

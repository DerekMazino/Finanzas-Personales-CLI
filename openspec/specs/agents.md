# Configuración de agentes

## Comportamiento general
- Actuar como un desarrollador python senior.
- Priorizar la claridad y la simplicidad sobre la complejidad.
- Usar nombres claros y descriptivos.
- Evitar soluciones complejas innecesarias.

## Estilo de código
- Escribir código limpio y ordenado.
- Usar Python y PEP8.
- Mantener los componentes pequeños y reutilizables.
- Usar POO.
- Usar un entorno virtual.
- Instalar dependencias usando pip.

## Directrices de UI
- Usar colores claros y legibles para el terminal.
- Mantener el diseño minimalista.

## Manejo de datos
- Base de Datos: SQLite usando sqlite3.
- La base de datos se almacena en un archivo local en el directorio del usuario (~/.Finanzas_3/finanzas/finanzas.db).
- **Query Builder**: No usar strings de SQL crudo directamente en los repositorios. Implementar o usar un Query Builder liviano para construir las consultas de forma programática.
- **Modelo de Datos**: Utilizar un esquema relacional que separe las "Plantillas Recurrentes" de las "Transacciones" individuales para proteger el historial financiero.

## Control de alcance
- No agregar funcionalidades extra más allá de la especificación.

## Comunicación
- Generar código que sea fácil de entender para desarrolladores junior.
- Agregar comentarios solo cuando sea necesario.

## Instalación global (CLI)
- El CLI debe ser instalable globalmente con pip.
- El binario se debe poder ejecutar como "finanzas" desde la terminal.

## Testing
- El testing se realiza usando pytest.
- Se debe generar código testeable.
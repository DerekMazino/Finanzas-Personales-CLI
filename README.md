# Finanzas Personales CLI 💰

Una herramienta de línea de comandos potente y minimalista escrita en Python para gestionar tus finanzas personales. Permite rastrear ingresos, egresos y plantillas recurrentes con una interfaz visual moderna basada en IDs.

## 🚀 Características

- **Gestión por Periodos**: Organización automática por Mes/Año con flujo interactivo de creación.
- **Conceptos Recurrentes (Templates)**: Define egresos que se repiten cada mes (ej. Renta, Internet) y se propagarán automáticamente a nuevos periodos.
- **Gestión Basada en IDs**: Modifica y elimina registros de forma precisa mediante identificadores únicos.
- **Eliminación Inteligente**: Preserva el historial financiero mediante eliminaciones lógicas para conceptos con historial.
- **Seguimiento de Ahorro**: Visualiza tu ahorro mensual y el acumulado histórico con barras de progreso.
- **Metas de Ahorro**: Define metas globales y monitorea tu progreso en tiempo real.
- **Interfaz Premium**: Tablas y paneles elegantes gracias a la librería `rich`.
- **Arquitectura Robusta**: Implementación de Repositorios, Servicios y un **Query Builder** personalizado para SQLite.

## 📋 Requisitos

- Python 3.8 o superior.
- Entorno virtual (recomendado).

## 🛠️ Instalación

1. Clona o descarga este repositorio.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - **Windows**: `venv\Scripts\activate`
   - **Unix/macOS**: `source venv/bin/activate`
4. Instala las dependencias:
   ```bash
   pip install rich pytest
   ```

## 💻 Uso

La aplicación se maneja a través de comandos directos.

### 1. Ver el Dashboard
Muestra el resumen del mes actual, egresos y el estatus del ahorro global.
```bash
python main.py dashboard
```

### 2. Agregar Transacciones (Ingresos/Egresos)
Registra movimientos rápidamente. Usa el flag `--recurrente` para conceptos que se repiten mensualmente.
```bash
python main.py add ingreso 5000 "Salario"
python main.py add egreso 1200 "Renta" --recurrente
```

### 3. Listar Movimientos
Muestra una tabla detallada con los IDs necesarios para edición o borrado.
```bash
python main.py list --mes 5 --año 2026
```

### 4. Eliminar un Registro
Usa el ID del listado. Si es un concepto recurrente con historial, el sistema lo desactivará para el futuro sin borrar el pasado.
```bash
python main.py delete 5
```

### 5. Establecer Meta de Ahorro
```bash
python main.py set-meta 15000
```

## 🧪 Pruebas
Para ejecutar la suite de pruebas unitarias:
```bash
set PYTHONPATH=.
pytest tests/
```

## 🗄️ Almacenamiento de Datos
Los datos se guardan en una base de datos SQLite en: `~/.Finanzas_3/finanzas/finanzas.db`.

## 🛠️ Estructura del Proyecto
- `main.py`: Punto de entrada con argparse.
- `proyecto/database/`: `manager.py` (Conexión), `repositories.py` (Lógica de datos), `utils.py` (Query Builder).
- `proyecto/logic/services.py`: Orquestación de reglas de negocio y recurrencia.
- `proyecto/models/entities.py`: Dataclasses de dominio.
- `proyecto/ui/cli.py`: Componentes visuales con Rich.
- `openspec/`: Documentación técnica y especificaciones de diseño.
- `tests/`: Pruebas unitarias con Pytest.

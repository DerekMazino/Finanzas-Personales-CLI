# Finanzas Personales CLI 💰

Una herramienta de línea de comandos potente y minimalista escrita en Python para gestionar tus finanzas personales. Permite rastrear ingresos, gastos y metas de ahorro con una interfaz visual moderna.

## 🚀 Características

- **Gestión por Periodos**: Organización automática por Mes/Año.
- **Seguimiento de Ahorro**: Visualiza tu ahorro mensual y el acumulado histórico.
- **Metas de Ahorro**: Define metas globales y monitorea tu progreso.
- **Interfaz Moderna**: Tablas y paneles coloridos gracias a la librería `rich`.
- **Persistencia Local**: Base de datos SQLite almacenada de forma segura en tu directorio de usuario.

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
   pip install rich
   ```

## 💻 Uso

La aplicación se maneja a través de comandos directos. Si usas el entorno virtual, ejecuta los comandos anteponiendo el ejecutable de python del venv:

### 1. Ver el Dashboard
Muestra el resumen del mes actual y el estatus del ahorro global.
```bash
python main.py dashboard
```
*Opcional: puedes ver otros meses:* `python main.py dashboard --mes 3 --año 2024`

### 2. Agregar Transacciones
Registra ingresos o gastos rápidamente.
```bash
python main.py add ingreso 5000 "Salario Mensual"
python main.py add gasto 150 "Cena Restaurante"
```

### 3. Listar Transacciones
Muestra una tabla detallada de los movimientos del periodo actual.
```bash
python main.py list
```

### 4. Eliminar una Transacción
Usa el ID que aparece en el listado para eliminar un registro.
```bash
python main.py delete 5
```

### 5. Establecer Meta de Ahorro
Define cuánto quieres ahorrar en total. El dashboard te mostrará el porcentaje completado.
```bash
python main.py set-meta 10000
```

## 🗄️ Almacenamiento de Datos

Los datos se guardan en una base de datos SQLite ubicada en:
`~/.Finanzas_3/finanzas/finanzas.db`

## 🛠️ Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación.
- `proyecto/`:
  - `database/`: Gestión de SQLite y repositorios.
  - `logic/`: Servicios y lógica de negocio.
  - `models/`: Definición de entidades (Periodo, Transacción).
  - `ui/`: Interfaz de usuario con la librería `rich`.

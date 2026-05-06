## 1. Interfaz (UI)

- [x] 1.1 Añadir el método `show_balance_only` en `proyecto/ui/cli.py` para mostrar el resumen de ahorro de forma compacta

## 2. Punto de Entrada (CLI)

- [x] 2.1 Configurar el subcomando `balance` en `main.py` usando `argparse`
- [x] 2.2 Implementar la lógica del comando `balance` llamando a `service.get_global_savings()`

## 3. Verificación

- [x] 3.1 Probar el comando `venv\Scripts\python main.py balance` y verificar que el output sea correcto

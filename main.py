import argparse
import sys
from datetime import datetime
from proyecto.database.manager import DatabaseManager
from proyecto.logic.services import FinanzasService
from proyecto.ui.cli import CLIInterface
from proyecto.models.entities import Transaccion

def main():
    db_manager = DatabaseManager()
    db_manager.connect()
    service = FinanzasService(db_manager)
    ui = CLIInterface()

    parser = argparse.ArgumentParser(description="Finanzas Personales CLI")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando: dashboard
    dash_parser = subparsers.add_parser("dashboard", help="Muestra el resumen financiero")
    dash_parser.add_argument("--mes", type=int, default=datetime.now().month)
    dash_parser.add_argument("--año", type=int, default=datetime.now().year)

    # Comando: balance
    subparsers.add_parser("balance", help="Muestra el saldo total acumulado rápidamente")

    # Comando: add
    add_parser = subparsers.add_parser("add", help="Agrega una nueva transacción (ingreso o egreso)")
    add_parser.add_argument("tipo", choices=["ingreso", "egreso"], help="Tipo de transacción")
    add_parser.add_argument("monto", type=float, help="Monto de la transacción")
    add_parser.add_argument("nombre", help="Nombre o concepto de la transacción")
    add_parser.add_argument("--mes", type=int, default=datetime.now().month)
    add_parser.add_argument("--año", type=int, default=datetime.now().year)
    add_parser.add_argument("--recurrente", action="store_true", help="Marcar como concepto recurrente")

    # Comando: list
    list_parser = subparsers.add_parser("list", help="Lista las transacciones de un periodo")
    list_parser.add_argument("--mes", type=int, default=datetime.now().month)
    list_parser.add_argument("--año", type=int, default=datetime.now().year)

    # Comando: delete
    del_parser = subparsers.add_parser("delete", help="Elimina una transacción por ID")
    del_parser.add_argument("id", type=int, help="ID de la transacción a eliminar")

    # Comando: set-meta
    meta_parser = subparsers.add_parser("set-meta", help="Define la meta de ahorro global")
    meta_parser.add_argument("monto", type=float, help="Monto de la meta")

    args = parser.parse_args()

    if args.command == "dashboard":
        summary = service.get_monthly_summary(args.mes, args.año)
        savings = service.get_global_savings()
        ui.show_dashboard(summary, savings)

    elif args.command == "balance":
        savings = service.get_global_savings()
        ui.show_balance_only(savings)

    elif args.command == "add":
        # Flujo Interactivo de Periodo (Tarea 4.2)
        periodo = service.periodos.find(args.mes, args.año)
        if not periodo:
            if ui.ask_confirmation(f"El periodo {args.mes}/{args.año} no existe. ¿Desea crearlo ahora?"):
                periodo = service.crear_periodo_con_recurrentes(args.mes, args.año)
                ui.show_message(f"[bold blue]Info:[/] Periodo {args.mes}/{args.año} creado con conceptos recurrentes.")
            else:
                ui.show_message("[bold yellow]Operación cancelada.[/] No se puede agregar sin un periodo.")
                db_manager.close()
                return
        
        try:
            service.registrar_concepto(
                periodo_id=periodo.id,
                nombre=args.nombre,
                monto=args.monto,
                tipo=args.tipo,
                es_recurrente=args.recurrente
            )
            ui.show_message(f"[bold green]OK[/] {args.tipo.capitalize()} '{args.nombre}' agregado exitosamente.")
        except ValueError as e:
            ui.show_error(str(e))

    elif args.command == "list":
        summary = service.get_monthly_summary(args.mes, args.año)
        ui.show_transactions(summary['transacciones'], title=f"Transacciones {args.mes}/{args.año}")

    elif args.command == "delete":
        service.eliminar_concepto(args.id)
        ui.show_message(f"[bold yellow]OK[/] Concepto {args.id} eliminado.")

    elif args.command == "set-meta":
        service.config.set_meta(args.monto)
        ui.show_message(f"[bold green]OK[/] Meta de ahorro establecida en ${args.monto:,.2f}")

    else:
        parser.print_help()

    db_manager.close()

if __name__ == "__main__":
    main()

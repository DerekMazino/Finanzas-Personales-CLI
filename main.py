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
    add_parser = subparsers.add_parser("add", help="Agrega una nueva transacción")
    add_parser.add_argument("tipo", choices=["ingreso", "gasto"], help="Tipo de transacción")
    add_parser.add_argument("monto", type=float, help="Monto de la transacción")
    add_parser.add_argument("descripcion", help="Descripción de la transacción")
    add_parser.add_argument("--mes", type=int, default=datetime.now().month)
    add_parser.add_argument("--año", type=int, default=datetime.now().year)
    add_parser.add_argument("--fecha", default=datetime.now().strftime("%Y-%m-%d"))

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
        periodo = service.periodos.get_or_create(args.mes, args.año)
        t = Transaccion(id=None, periodo_id=periodo.id, tipo=args.tipo, monto=args.monto, descripcion=args.descripcion, fecha=args.fecha)
        service.transacciones.add(t)
        ui.show_message(f"[OK] {args.tipo.capitalize()} agregado exitosamente.")

    elif args.command == "list":
        summary = service.get_monthly_summary(args.mes, args.año)
        ui.show_transactions(summary['transacciones'], title=f"Transacciones {args.mes}/{args.año}")

    elif args.command == "delete":
        service.transacciones.delete(args.id)
        ui.show_message(f"[OK] Transacción {args.id} eliminada.")

    elif args.command == "set-meta":
        service.config.set_meta(args.monto)
        ui.show_message(f"[OK] Meta de ahorro establecida en ${args.monto:,.2f}")

    else:
        parser.print_help()

    db_manager.close()

if __name__ == "__main__":
    main()

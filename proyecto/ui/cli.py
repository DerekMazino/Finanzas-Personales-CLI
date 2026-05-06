from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.progress import ProgressBar

console = Console()

class CLIInterface:
    @staticmethod
    def show_dashboard(monthly_summary, global_savings):
        # Panel superior: Mes actual
        periodo_str = monthly_summary['periodo']
        ingresos = monthly_summary['ingresos']
        gastos = monthly_summary['gastos']
        balance = monthly_summary['balance']

        balance_color = "green" if balance >= 0 else "red"
        
        month_panel = Panel(
            Text.assemble(
                ("Ingresos: ", "bold"), (f"${ingresos:,.2f}\n", "green"),
                ("Gastos:   ", "bold"), (f"${gastos:,.2f}\n", "red"),
                ("-" * 20 + "\n"),
                ("Balance:  ", "bold"), (f"${balance:,.2f}", f"bold {balance_color}")
            ),
            title=f"[bold blue]Resumen {periodo_str}[/bold blue]",
            expand=False
        )

        # Panel inferior: Ahorro global
        acumulado = global_savings['ahorro_acumulado']
        meta = global_savings['meta']
        progreso = global_savings['progreso_porcentaje']

        savings_content = [
            ("Ahorro Total Acumulado: ", "bold"), (f"${acumulado:,.2f}\n", "cyan")
        ]
        
        if meta:
            savings_content.extend([
                ("Meta Global:           ", "bold"), (f"${meta:,.2f}\n", "yellow"),
                ("Progreso:              ", "bold"), (f"{progreso:.1f}%\n" if progreso is not None else "0%\n", "bold yellow")
            ])
            # Podríamos agregar una barra de progreso aquí
        
        savings_panel = Panel(
            Text.assemble(*savings_content),
            title="[bold cyan]Estatus de Ahorro[/bold cyan]",
            expand=False
        )

        console.print(month_panel)
        console.print(savings_panel)

    @staticmethod
    def show_transactions(transacciones, title="Transacciones"):
        table = Table(title=title)
        table.add_column("ID", justify="right", style="dim")
        table.add_column("Fecha")
        table.add_column("Descripción")
        table.add_column("Tipo")
        table.add_column("Monto", justify="right")

        for t in transacciones:
            color = "green" if t.tipo == 'ingreso' else "red"
            table.add_row(
                str(t.id),
                t.fecha,
                t.descripcion,
                t.tipo.capitalize(),
                f"[bold {color}]${t.monto:,.2f}[/bold {color}]"
            )

        console.print(table)

    @staticmethod
    def show_balance_only(global_savings):
        acumulado = global_savings['ahorro_acumulado']
        meta = global_savings['meta']
        progreso = global_savings['progreso_porcentaje']

        color = "green" if acumulado >= 0 else "red"
        
        content = [
            ("Saldo Total: ", "bold"), (f"${acumulado:,.2f}", f"bold {color}")
        ]

        if meta:
            content.extend([
                ("\nMeta:        ", "bold"), (f"${meta:,.2f}", "yellow"),
                ("\nProgreso:    ", "bold"), (f"{progreso:.1f}%" if progreso is not None else "0%", "bold yellow")
            ])

        console.print(Panel(Text.assemble(*content), title="[bold cyan]Balance Global[/bold cyan]", expand=False))

    @staticmethod
    def show_message(message, style="bold green"):
        console.print(message, style=style)

    @staticmethod
    def show_error(message):
        console.print(f"Error: {message}", style="bold red")

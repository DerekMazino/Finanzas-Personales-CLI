from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.progress import ProgressBar
from rich.prompt import Confirm

console = Console()

class CLIInterface:
    @staticmethod
    def show_dashboard(monthly_summary, global_savings):
        # Panel superior: Mes actual
        periodo_str = monthly_summary['periodo']
        ingresos = monthly_summary['ingresos']
        egresos = monthly_summary['egresos']
        balance = monthly_summary['balance']

        balance_color = "green" if balance >= 0 else "red"
        
        month_panel = Panel(
            Text.assemble(
                ("Ingresos: ", "bold"), (f"${ingresos:,.2f}\n", "green"),
                ("Egresos:  ", "bold"), (f"${egresos:,.2f}\n", "red"),
                ("-" * 25 + "\n"),
                ("Balance:   ", "bold"), (f"${balance:,.2f}", f"bold {balance_color}")
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
        
        savings_panel = Panel(
            Text.assemble(*savings_content),
            title="[bold cyan]Estatus de Ahorro[/bold cyan]",
            expand=False
        )

        console.print(month_panel)
        console.print(savings_panel)

    @staticmethod
    def show_transactions(transacciones, title="Transacciones"):
        table = Table(title=f"[bold blue]{title}[/]")
        table.add_column("ID", justify="right", style="dim")
        table.add_column("Nombre/Concepto")
        table.add_column("Tipo")
        table.add_column("Monto", justify="right")
        table.add_column("Fecha Registro", style="dim")

        for t in transacciones:
            color = "green" if t.tipo == 'ingreso' else "red"
            fecha_str = t.fecha_creacion[:10] if t.fecha_creacion else "-"
            table.add_row(
                str(t.id),
                t.nombre,
                t.tipo.capitalize(),
                f"[bold {color}]${t.monto:,.2f}[/bold {color}]",
                fecha_str
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
    def ask_confirmation(message):
        """Pregunta al usuario una confirmación sí/no."""
        return Confirm.ask(f"[bold yellow]{message}[/]")

    @staticmethod
    def show_message(message):
        console.print(message)

    @staticmethod
    def show_error(message):
        console.print(f"[bold red]Error:[/] {message}")

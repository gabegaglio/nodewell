from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()

def make_table(title, columns, rows):
    table = Table(title=title)

    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*row)
    
    console.print(table)

def display_inventory(hosts):
    rows = [
        (h.get("name", ""), h.get("ip", ""))
        for h in hosts
    ]
    make_table("Nodewell Inventory", ["Name", "IP"], rows)

def display_ping(results):
    table = Table(title="Ping Results")
    table.add_column("Name")
    table.add_column("IP")
    table.add_column("Status")

    with Live(table, console=console, refresh_per_second=4):
        for r in results:
            status = r.get("status", "UNKNOWN")
            colored = f"[green]{status}[/green]" if status == "UP" else f"[red]{status}[/red]"
            table.add_row(r["name"], r["ip"], colored)

def display_services(results):
    return

def display_docker(results):
    return

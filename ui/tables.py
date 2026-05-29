from rich.console import Console
from rich.table import Table

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
    # we use this method because we need to color status
    rows = []
    for r in results:
        status = r.get("status", "UNKNOWN")
        colored = f"[green]{status}[/green]" if status == "UP" else f"[red]{status}[/red]"
        rows.append((r["name"], r["ip"], colored))
    make_table("Ping Results", ["Name", "IP", "Status"], rows)



def display_services(results):
    return

def display_docker(results):
    return

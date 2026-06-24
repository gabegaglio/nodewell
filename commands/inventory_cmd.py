from ui import tables

def run(conf):
    tables.display_inventory(conf.get("hosts", []))

from checks import ping
from ui import tables

def run(conf):
    results = ping.check_hosts(conf.get("hosts", []))
    tables.display_ping(results)

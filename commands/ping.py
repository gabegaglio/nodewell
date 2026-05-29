from checks import ping
from ui import tables

def run(conf):
    results = ping.check_hosts(conf.get("hosts", [])) # results acts as generator
    tables.display_ping(results)

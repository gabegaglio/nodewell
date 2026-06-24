from checks import ping
from ui import tables

def run(conf, print_host):
    results = ping.check_hosts(conf.get("hosts", []), print_host) # results acts as generator
    tables.display_ping(results)

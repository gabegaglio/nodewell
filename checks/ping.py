import subprocess
import platform

platform_flag = "-n" if platform.system() == "Windows" else "-c"

def check_host(host, print_host=False):

    # get name from host
    name = host.get("name")

    if print_host:
        print(f"Pinging {name}...")

    # get ip from host
    ip = host.get("ip")
    # run ping
    result = subprocess.run(["ping", platform_flag, "1", ip], capture_output=True, text=True)
    # determine if up/down
    if result.returncode == 0:
        status = "UP"
    else:
        status = "DOWN"
    
    return {
        "name": name,
        "ip": ip,
        "status": status
    }
    
def check_hosts(hosts, print_host=False):
    # generator: yield each result as it's pinged
    for host in hosts:
        yield check_host(host, print_host)
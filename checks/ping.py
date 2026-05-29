import subprocess
import platform

platform_flag = "-n" if platform.system() == "Windows" else "-c"

def check_host(host):

    # get name from host
    name = host.get("name")

    # get ip from host
    ip = host.get("ip")
    # run ping
    result = subprocess.run(["ping", platform_flag, "1", ip], capture_output=True, text=True)
    # determine up/down
    if result.returncode == 0:
        status = "UP"
    else:
        status = "DOWN"
    
    return {
        "name": name,
        "ip": ip,
        "status": status
    }
    
def check_hosts(hosts):
    # create empty lists for ersults
    results = []

    # loop through hosts
    for host in hosts:
        # call check_host
        result = check_host(host)
        results.append(result)
    # return all results
    return results



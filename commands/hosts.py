from utils import config

def add(conf, name, ip):
    hosts = conf.setdefault("hosts", [])
    if any(h.get("name") == name for h in hosts):
        print(f"Host '{name}' already exists")
        return

    hosts.append({"name": name, "ip": ip})
    config.save(conf)
    print(f"Added host '{name}' ({ip})")

def delete(conf, name):
    hosts = conf.get("hosts", [])
    # removes in place
    target = next((h for h in hosts if h.get("name") == name), None)
    if target is None:
        print(f"Host '{name}' not found")
        return

    hosts.remove(target)
    config.save(conf)
    print(f"Deleted host '{name}'")

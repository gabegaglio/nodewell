import yaml # read yaml config fil

CONFIG_FILE = "config.yaml"

def load_config(): # load and read yaml
    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)

    return config

def show_inventory(config):

    hosts = config.get("hosts", [])

    print("NODEWELL INVENTORY")
    print("-------------------")

    for host in hosts:
        name = host.get("name")
        ip = host.get("ip")

        print(f"{name:<15} {ip}")
    
def main():
    config = load_config()
    show_inventory(config)

if __name__ == "__main__":
    main()
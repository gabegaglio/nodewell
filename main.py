import shutil
from pathlib import Path

import yaml

CONFIG_FILE = Path("config.yaml")
EXAMPLE_FILE = Path("config.yaml.example")


def ensure_config():
    if CONFIG_FILE.exists():
        return

    if not EXAMPLE_FILE.exists():
        print(f"Missing {EXAMPLE_FILE} - cannot create config")
        raise SystemExit(1)

    shutil.copy(EXAMPLE_FILE, CONFIG_FILE)
    print("Created config.yaml - edit as needed")
    raise SystemExit(0)


def load_config():
    with CONFIG_FILE.open("r") as file:
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
    ensure_config()
    config = load_config()
    show_inventory(config)


if __name__ == "__main__":
    main()

import shutil
from pathlib import Path
import yaml

CONFIG_FILE = Path("config.yaml")
EXAMPLE_FILE = Path("config.yaml.example")

def ensure():
    if CONFIG_FILE.exists():
        return

    if not EXAMPLE_FILE.exists():
        print(f"Missing {EXAMPLE_FILE} - cannot create config")
        raise SystemExit(1)

    shutil.copy(EXAMPLE_FILE, CONFIG_FILE)
    print("Created config.yaml - edit as needed")
    raise SystemExit(0)

def load():
    with CONFIG_FILE.open("r") as file:
        config = yaml.safe_load(file)

    return config

def save(config):
    with CONFIG_FILE.open("w") as f:
        yaml.safe_dump(config, f, default_flow_style=False, sort_keys=False)
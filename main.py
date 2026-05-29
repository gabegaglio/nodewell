from commands import hosts, inventory, ping
from utils import config
import argparse

def main():
    # make sure conf loads and is there
    config.ensure()
    # this initiates config
    conf = config.load()

    # 
    parser = argparse.ArgumentParser(prog="nodewell")
    subparsers = parser.add_subparsers(dest="command")

    # simple, one off commands
    subparsers.add_parser("inventory")
    subparsers.add_parser("ping")

    # host command, with own sub commands
    host_parser = subparsers.add_parser("host")
    host_sub = host_parser.add_subparsers(dest="host_command")

    add_p = host_sub.add_parser("add")
    add_p.add_argument("--name", required=True)
    add_p.add_argument("--ip", required=True)

    del_p = host_sub.add_parser("delete")
    del_p.add_argument("--name", required=True)

    edit_p = host_sub.add_parser("edit")
    edit_p.add_argument("--name", required=True)
    edit_p.add_argument("--ip", required=True)

    args = parser.parse_args()

    if args.command == "inventory":
        inventory.run(conf)
    elif args.command == "ping":
        ping.run(conf)
    elif args.command == "host":
        if args.host_command == "add":
            hosts.add(conf, args.name, args.ip)
        elif args.host_command == "delete":
            hosts.delete(conf, args.name)
        elif args.host_command == "edit":
            hosts.edit(conf, args.name, args.ip)

if __name__ == "__main__":
    main()

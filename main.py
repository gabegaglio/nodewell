from commands import hosts_cmd, inventory_cmd, ping_cmd, report_cmd
from utils import config
import argparse

def main():
    # make sure conf loads and is there
    config.ensure()
    # this initiates config, passed into each commands run function
    conf = config.load()

    parser = argparse.ArgumentParser(prog="nodewell")
    subparsers = parser.add_subparsers(dest="command")

    # simple, one off commands
    subparsers.add_parser("inventory")
    subparsers.add_parser("ping")
    subparsers.add_parser("report")

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
        inventory_cmd.run(conf)
    elif args.command == "ping":
        print_host = False
        ping_cmd.run(conf, print_host)
    elif args.command == "report":
        report_cmd.run(conf)
    elif args.command == "host":
        if args.host_command == "add":
            hosts_cmd.add(conf, args.name, args.ip)
        elif args.host_command == "delete":
            hosts_cmd.delete(conf, args.name)
        elif args.host_command == "edit":
            hosts_cmd.edit(conf, args.name, args.ip)

if __name__ == "__main__":
    main()

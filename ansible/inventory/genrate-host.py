"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 22:27:07
Description: generate host for various application
"""
import argparse


def generate_instances():
    with open("wm_inventory_file.ini") as f:
        hosts_starts = False
        hosts = []

        for line in f.readlines():
            line = line.replace("\n", "")

            # no hosts any more
            if hosts_starts:
                if line == "":
                    hosts_starts = False

            # has hosts e.g.: 192.168.0.1
            if hosts_starts:
                hosts.append(line)

            # starts reading hosts
            if line == "[instances]":
                hosts_starts = True

        with open("application_hosts.ini", "w") as file:
            print("[instances]", file=file)
            for host in hosts:
                print(host, file=file)
            print("", file=file)


def generate_hosts_for_application(n_application: int, name: str, reverse=False, n=-1):
    with open("wm_inventory_file.ini") as f:
        hosts_starts = False
        hosts = []

        for line in f.readlines():
            line = line.replace("\n", "")

            # no hosts any more
            if hosts_starts:
                if line == "":
                    hosts_starts = False

            # has hosts e.g.: 192.168.0.1
            if hosts_starts:
                hosts.append(line)

            # starts reading hosts
            if line == "[instances]":
                hosts_starts = True

        if len(hosts) < n_application:
            raise Exception("Too few hosts for number of application required")

        hosts_for_application = hosts
        if reverse:
            hosts_for_application = hosts_for_application[::-1]
        hosts_for_application = hosts_for_application[:n_application]
        if n != -1:
            hosts_for_application = [hosts[n]]

        with open("application_hosts.ini", "a") as file:
            print("[{}]".format(name), file=file)
            for host in hosts_for_application:
                print(host, file=file)
            print("", file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help='n hosts for crawler')
    parser.add_argument('-b', help='n hosts for backend server')
    parser.add_argument('-db', help='n hosts for database server')
    args = parser.parse_args()

    generate_instances()

    if args.c:
        n_crawler = int(args.c)
        generate_hosts_for_application(n_crawler, "crawler")

    if args.b:
        n_backend = int(args.b)
        generate_hosts_for_application(n_backend, "backend", reverse=True, n=2)

    if args.db:
        n_database = int(args.db)
        generate_hosts_for_application(n_database, "database", reverse=True)

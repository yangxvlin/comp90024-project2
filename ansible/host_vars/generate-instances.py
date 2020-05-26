"""
Author:      XuLin Yang
Student id:  904904
Date:        2020-4-22 16:03:55
Description: generate n instances var
"""

import argparse


def create_instances_file(n_instances: int):
    # print("", file=file)

    with open("instances.yaml", 'w') as file:
        print("---", file=file)

        print("# ****************************** Security group ******************************", file=file)
        print("# Create a TCP rule covering all ports", file=file)
        print("security_groups:", file=file)
        for i in range(1, n_instances+1):
            print("  - name: instance{}-security-group".format(i), file=file)
            print("    description: \"security group for instance{} server\"".format(i), file=file)
            print("    protocol: tcp", file=file)
            print("    port_range_min: 1", file=file)
            print("    port_range_max: 65535", file=file)
            print("    remote_ip_prefix: 0.0.0.0/0", file=file)
        print("", file=file)

        print("# ****************************** Volume ******************************", file=file)
        print("volumes:", file=file)
        for i in range(1, n_instances+1):
            print("  - vol_name: instance{}-volume".format(i), file=file)
            print("    vol_size: 60", file=file)
            print("    device: /dev/vdb", file=file)
            print("    mountpoint: /data", file=file)
        print("", file=file)

        print("# ****************************** Instance ******************************", file=file)
        print("instances:", file=file)
        for i in range(1, n_instances + 1):
            print("  - name: instance{}".format(i), file=file)
            print("    security_groups: instance{}-security-group".format(i), file=file)
            print("    volume_ids: '{{ instance{}_volumes|default([]) }}'".format(i), file=file)
            print("    volumes: ['instance{}-volume']".format(i), file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='n instances to be created')
    args = parser.parse_args()

    # n_instances = int(input("How much instances you would like to create?"))
    create_instances_file(int(args.n))

import sys


def ip_addr_valid(iplist: list[str]):
    """check ip address format"""

    # rstrip already performed in ip_file_valid

    for ip in iplist:
        octet_list = ip.split('.')
        octet_list = list(map(int, octet_list))

        if (
                    len(octet_list) == 4    # octets must be 4
                and octet_list[0] >= 1      # first octet must be between 1 and 223
                and octet_list[0] <= 223    # first octet must be between 1 and 223
                and octet_list[0] != 127    # no loopback
                and octet_list[0] != 169    # no dhcp fail
                and (
                        octet_list[0] != 169    # no 169.254.x.x
                    or  octet_list[1] != 254
                )
                and octet_list[1] >= 0      # all remaining octets must be
                and octet_list[1] <= 255    # between 0 and 255
                and octet_list[2] >= 0
                and octet_list[2] <= 255
                and octet_list[3] >= 0
                and octet_list[3] <= 255
        ):
            continue

        else:
            print(f'\n* There was an invalid IP address in the file: {ip} :(\n')
            sys.exit()


if __name__ == '__main__':
    ip_addr_valid(['10.10.10.2'])

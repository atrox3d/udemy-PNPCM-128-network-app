import sys
import subprocess


def ip_reach(iplist: list[str]):
    """check IP reachability"""
    for ip in iplist:
        # rstrip already performed in ip_file_valid
        ping_reply = subprocess.call(
            f'ping {ip} /n 2',
            # stdout=subprocess.DEVNULL,
            # stderr=subprocess.DEVNULL
        )

        if ping_reply == 0:
            print(f"* {ip} is reachable")
        else:
            ####################################################################
            # TODO: fix the ping errorlevel
            ####################################################################
            print(f"* {ip} is not reachable, check connectivity and try again")
            sys.exit()


if __name__ == '__main__':
    ip_reach(['127.0.0.1', '192.168.1.10', '192.168.1.40', '192.168.1.20'])

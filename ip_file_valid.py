import os.path
import sys


def ip_file_valid(ipfile_path=None) -> list[str]:
    """checking IP address file content and validity"""

    # if not passed as parameter
    if not ipfile_path:
        # ask user
        ipfile_path = input('\n# Enter ip file path: ')

    # check if ipfile exists
    if os.path.isfile(ipfile_path):
        print("\n* IP file exists")
    else:
        print(f"file {ipfile_path} does not exist")
        print("please check and try again")
        sys.exit(1)

    # open file and read data
    with open(ipfile_path) as ipfile:
        ipfile.seek(0)
        iplist = ipfile.readlines()

    # remove \n
    iplist = list(map(str.rstrip, iplist))

    return iplist


if __name__ == '__main__':
    iplist = ip_file_valid('data/ipfile')
    print(iplist)

import paramiko
import os.path
import time
import sys
import re


def userfile_valid(userfile_path=None):
    """checking user file validity"""

    # if not passed as parameter
    if not userfile_path:
        # ask user
        userfile_path = input('\n# Enter user file path: ')

    # check if ipfile exists
    if os.path.isfile(userfile_path):
        print("\n* user file exists")
    else:
        print(f"file {userfile_path} does not exist")
        print("please check and try again")
        sys.exit(1)

    # # open file and read data
    # with open(cmdfile_path) as userfile:
    #     userfile.seek(0)
    #     iplist = userfile.readlines()
    #
    # # remove \n
    # iplist = list(map(str.rstrip, iplist))
    #
    # return iplist


def cmdfile_valid(cmdfile_path=None):
    """checking command file validity"""

    # if not passed as parameter
    if not cmdfile_path:
        # ask user
        cmdfile_path = input('\n# Enter cmd file path: ')

    # check if ipfile exists
    if os.path.isfile(cmdfile_path):
        print("\n* cmd file exists")
    else:
        print(f"file {cmdfile_path} does not exist")
        print("please check and try again")
        sys.exit(1)

    # # open file and read data
    # with open(cmdfile_path) as userfile:
    #     userfile.seek(0)
    #     iplist = userfile.readlines()
    #
    # # remove \n
    # iplist = list(map(str.rstrip, iplist))
    #
    # return iplist


def ssh_connection(ip, userfile_path, cmdfile_path):
    try:
        with open(userfile_path) as userfile:
            userfile.seek(0)
            # username,password
            username, password = userfile.readline().rstrip().split(',')
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(
            ip,
            username=username,
            password=password
        )
        connection = session.invoke_shell()

        #
        #   arista - set terminal length, disable pagination
        #
        connection.send("enable\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        #
        #   arista - global config mode
        #
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        with open(cmdfile_path) as cmdfile:
            cmdfile.seek(0)
            for line in cmdfile:
                connection.send(line)
                time.sleep(2)

        output = connection.recv(65535)
        #
        #   https://www.udemy.com/course/python-programming-for-real-life-networking-use/learn/#questions/6537078
        #
        #   The b represents an instance of the bytes type,
        #   because the network device does not return plain text
        #   (type string) when querying it via SSH.
        #
        if re.search(b"% Invalid input", output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))

        else:
            print("\nDONE for device {} :)\n".format(ip))

        # Test for reading command output
        print(str(output) + "\n")

        # Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print("* Invalid username or password \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")


# if __name__ == '__main__':
#     iplist = ip_file_valid('data/ipfile')
#     print(iplist)

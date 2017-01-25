#!/usr/bin/env python

#This script is a copy of challengeconverttoclasses.py that has been converted
#to a class based solution with methods

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

# Define class
class NetworkDevice(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        try:
            self.remote_conn = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")
    def login(remote_conn, username, password):
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output
    def send_command(remote_conn, cmd):
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()
    def login(remote_conn, username, password):
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output
    def disable_paging(remote_conn, paging_cmd='terminal length 0'):
        return send_command(remote_conn, paging_cmd)
    def close():
        remote_conn.close()


def main():
    ip_addr = ('184.105.247.70')
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = '88newclass'
    rtr1 = NetworkDevice(ip_addr, username, password)
    output = rtr1.login()
    time.sleep(1)
    rtr1.read_very_eager()
    rtr1.disable_paging()
    output = rtr1.send_command('show ip int brief')
    print "\n\n"
    print output
    print "\n\n"
    rtr1.close()

if __name__ == "__main__":
    main()

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
    def login(self):
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(password + '\n')
        return output
    def send_command(self, cmd):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()
    def close(self):
        self.remote_conn.close()


def main():
    ip_addr = ('184.105.247.70')
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = '88newclass'
    rtr1 = NetworkDevice(ip_addr, username, password)
    output = rtr1.login()
    time.sleep(1)
    rtr1.read_very_eager()
    output = rtr1.send_command('terminal length 0')
    output = rtr1.send_command('show ip int brief')
    print "\n\n"
    print output
    print "\n\n"
    rtr1.close()

if __name__ == "__main__":
    main()

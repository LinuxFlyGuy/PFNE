#!/usr/bin/env python

import pexpect, sys, re

def main():
    ip = '184.105.247.71'
    user = 'pyclass'
    password = '88newclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user, ip, port))
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 6
    try:
        ssh_conn.expect('ssword:')
        ssh_conn.sendline(password)

        ssh_conn.expect('pynet-rtr2#')

        ssh_conn.sendline('terminal length 0')
        ssh_conn.expect('pynet-rtr2#')

        ssh_conn.sendline('configure terminal')
        ssh_conn.expect('pynet-rtr2(config)#')

        ssh_conn.sendline('logging buffered 5000')
        ssh_conn.expect('pynet-rtr2(config)#')

        ssh_conn.sendline('exit')
        ssh_conn.expect('pynet-rtr2#')

        ssh_conn.sendline('show run')
        ssh_conn.expect('zzz')
        print ssh_conn.before
        print ssh_conn.after
    except pexpect.TIMEOUT as e:
        print "Timed out"

if __name__ == '__main__':
    main()

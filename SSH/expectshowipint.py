#!/usr/bin/env python

import pexpect, sys

def main():
    #ip = '192.168.1.222'
    #user = 'admin'
    #password = 'cubro'
    ip = '184.105.247.71'
    user = 'pyclass'
    password = '88newclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(user, ip, port))
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    try:
        ssh_conn.expect('ssword:')
        ssh_conn.sendline(password)

        #ssh_conn.expect('[root@CubroEX32plus ~]$')
        ssh_conn.expect('#')

        #ssh_conn.sendline('ls')
        #ssh_conn.expect('[root@CubroEX32plus ~]$')
        ssh_conn.sendline('terminal length 0')
        ssh_conn.expect('#')

        #ssh_conn.sendline('ovs-ofctl show br0')
        #ssh_conn.expect('zzz')
        ssh_conn.sendline('show ip int brief')
        ssh_conn.expect('zzz')
        print ssh_conn.before
        print ssh_conn.after
    except pexpect.TIMEOUT as e:
        print "Timed out"

if __name__ == '__main__':
    main()

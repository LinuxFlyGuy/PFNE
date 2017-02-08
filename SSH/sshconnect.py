#!/usr/bin/env python

import paramiko, time
from getpass import getpass

ip = '192.168.1.221'
user = 'admin'
password = getpass()
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.load_system_host_keys()
#remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=user, password=password, look_for_keys=False, allow_agent=False, port=port)
remote_conn = remote_conn_pre.invoke_shell()
remote_conn.settimeout(8.0)
outp = remote_conn.recv(5000)
print outp

def sshinteract(cmd):
    remote_conn.send(cmd + '\n')
    time.sleep(3)
    outp = remote_conn.recv(5000)
    print outp

while True:
    sshinteract(raw_input('>:'))

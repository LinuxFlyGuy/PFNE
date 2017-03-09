#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime


from net_system.models import NetworkDevice, Credentials
import django

from multiprocessing import Process, current_process
import time

def main():
    django.setup()

    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    procs = []
    for device in devices:
        my_proc = Process(target=show_version, args=(device,)) #comma indicates the args is a tuple
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        print a_proc
        a_proc.join()

    execute_time = datetime.now() - start_time
    print "Time to Execute: ", execute_time

def show_version(device):
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type,
                                ip=device.ip_address,
                                username=creds.username,
                                password=creds.password,
                                port=device.port,
                                secret='')
    print
    print '#' * 80

    print remote_conn.send_command("show version")
    print '#' * 80

if __name__ == '__main__':
    main()

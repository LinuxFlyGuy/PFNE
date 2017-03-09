#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime


from net_system.models import NetworkDevice, Credentials
import django

from multiprocessing import Process, current_process, Queue
import time

def main():
    django.setup()

    start_time = datetime.now()
    q = Queue(maxsize=20)
    devices = NetworkDevice.objects.all()

    procs = []
    for device in devices:
        my_proc = Process(target=show_version_queue, args=(device, q)) #comma indicates the args is a tuple
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        print a_proc
        a_proc.join()

    while not q.empty():
        my_dict = q.get()
        for k,v in my_dict.iteritems():
            print k
            print v

    execute_time = datetime.now() - start_time
    print "Time to Execute: ", execute_time

def show_version_queue(device, q):
    output_dict = {}
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type,
                                ip=device.ip_address,
                                username=creds.username,
                                password=creds.password,
                                port=device.port,
                                secret='',
                                verbose=False)
    print
    output = ('#' * 80) + '\n'
    output += remote_conn.send_command("show version") + '\n'
    output += ('#' * 80) + '\n'
    output_dict[device.device_name] = output
    q.put(output_dict)

if __name__ == '__main__':
    main()

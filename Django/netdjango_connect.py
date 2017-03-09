#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    start_time = datetime.now()
    devices = NetworkDevices.objects.all()
    for device in devices:
        print device
        secret = ''
        print device_type, port, ip, username, password
        remote_conn = ConnectHandler(device_type=device.device_type, ip=device.ip_address, username=creds.username, password=creds.password, port=device.port, secret=secret)

        print
        print '#' * 80
        print remote_conn.send("show version")
        print '#' * 80

    execute_time = datetime.now() - start_time
    print execute_time
    
if __name__ == '__main__':
    main()
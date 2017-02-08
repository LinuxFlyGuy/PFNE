#!/usr/bin/env python
import netmiko

def main():
    user = 'pyclass'
    password = '88newclass'
    port = 22
    rtr1 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.70',
        'username': user,
        'password': password
        }
    rtr2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': user,
        'password': password
        }

    pynet_rtr1 = netmiko.ConnectHandler(**rtr1)
    pynet_rtr2 = netmiko.ConnectHandler(**rtr2)

    x = pynet_rtr1.send_config_from_file(config_file='config.txt')
    print x
    x = pynet_rtr2.send_config_from_file(config_file='config.txt')
    print x

if __name__ == '__main__':
    main()

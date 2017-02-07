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
    juni = {
        'device_type': 'juniper',
        'ip': '184.105.247.76',
        'username': user,
        'password': password
        }
    pynet_rtr1 = netmiko.ConnectHandler(**rtr1)
    pynet_rtr2 = netmiko.ConnectHandler(**rtr2)
    juniper = netmiko.ConnectHandler(**juni)

    x = pynet_rtr1.find_prompt()
    print x
    x = pynet_rtr1.send_command('show arp')
    print x
    x = pynet_rtr2.find_prompt()
    print x
    x = pynet_rtr2.send_command('show arp')
    print x
    x = juniper.find_prompt()
    print x
    x = juniper.send_command('show arp')
    print x

if __name__ == '__main__':
    main()

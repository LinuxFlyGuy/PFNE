#!/usr/bin/env python
import netmiko

def main():
    user = 'pyclass'
    password = '88newclass'
    port = 22
    rtr2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': user,
        'password': password
        }
    pynet_rtr2 = netmiko.ConnectHandler(**rtr2)

    x = pynet_rtr2.find_prompt()
    print x
    x = pynet_rtr2.send_command('terminal length 0')
    print x
    x = pynet_rtr2.config_mode()
    print x
    x = pynet_rtr2.send_command('logging buffered 9000')
    print x
    x = pynet_rtr2.exit_config_mode()
    print x
    x = pynet_rtr2.send_command('show logging')
    print x
    
if __name__ == '__main__':
    main()

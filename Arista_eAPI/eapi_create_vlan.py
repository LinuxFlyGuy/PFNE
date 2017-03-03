#!/usr/bin/env python

import pyeapi, sys
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

def usage():
        print '''Usage:
                -a, --add <vlan name> <vlan id> Create VLAN with specified name and ID if it does not exist
                -r, --remove <vlan name> <vlan id> Remove VLAN with specified name and ID if it exists
        '''

if len(sys.argv) <= 2 or len(sys.argv) >=5:
    usage()
elif len(sys.argv) == 4 and str(sys.argv[1]) == '--add' or len(sys.argv) == 4 and str(sys.argv[1]) == '-a':
    name = str(sys.argv[2])
    vid = str(sys.argv[3])
    option1 = 'vlan ' + vid
    option2 = 'name ' + name
    cmd = [option1, option2]
    active_vlans = []
    print 'Checking if %s VLAN %s exists' % (name, vid)
    try:
        check = pynet_sw3.enable("show vlan")
        unlist = check[0]
        for item in unlist['result']['vlans']:
            active_vlans.append(str(item))
        if vid in active_vlans:
            print 'VLAN already exists'
        else:
            print 'Adding %s VLAN %s' % (name, vid)
            pynet_sw3.config(cmd)
            #pynet_sw3.enable("write memory")
    except:
        print 'Unable to communicate with switch'
elif len(sys.argv) == 3 and str(sys.argv[1]) == '--remove' or len(sys.argv) == 3 and str(sys.argv[1]) == '-r':
    vid = str(sys.argv[2])
    option = 'no vlan ' + vid
    cmd = [option]
    active_vlans = []
    print 'Checking if VLAN %s exists' % vid
    try:
        check = pynet_sw3.enable("show vlan")
        unlist = check[0]
        for item in unlist['result']['vlans']:
            active_vlans.append(str(item))
        if vid in active_vlans:
            print 'Removing VLAN %s' % vid
            pynet_sw3.config(cmd)
            #pynet_sw3.enable("write memory")
        else:
            print 'VLAN does not exist'
    except:
        print 'Unable to communicate with switch'
else:
    usage()

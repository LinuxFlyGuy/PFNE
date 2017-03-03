#!/usr/bin/env python

import pyeapi, sys
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

def usage():
        print '''Usage:
                -a, --add <vlan name> <vlan id> Create VLAN with specified name and ID if it does not exist
                -r, --remove <vlan name> <vlan id> Remove VLAN with specified name and ID if it exists
        '''

if len(sys.argv) <= 3 or len(sys.argv) >=5:
    print len(sys.argv)
    usage()
elif len(sys.argv) == 4 and sys.argv[1] != '--add': #or sys.argv[1] != '-a':
    print len(sys.argv)
    usage()
elif len(sys.argv) == 4 and sys.argv[1] != '--remove': #or sys.argv[1] != '-r':
    print len(sys.argv)
    usage()
elif len(sys.argv) == 4 and sys.argv[1] == '--add': #or sys.argv[1] == '-a':
    print len(sys.argv)
    print sys.argv[1]
    name = sys.argv[2]
    vid = sys.argv[3]
    option1 = 'vlan ' + vid
    option2 = 'name ' + name
    cmd = [option1, option2]
    print 'Checking if %s VLAN %s exists' % (name, vid)
    try:
        check = pynet_sw3.enable("show vlan")
        unlist = check[0]
        for item in unlist['result']['vlans']:
            if vid in item:
                print 'VLAN already exists'
            elif vid not in item:
                print 'Adding %s VLAN %s' % (name, vid)
                pynet_sw3.config(cmd)
                #pynet_sw3.enable("write memory")
            else:
                print 'eapi_create_vlan encountered a problem'
    except:
        print 'Unable to communicate with switch'
elif len(sys.argv) == 3 and sys.argv[1] == '--remove': #or sys.argv[1] == '-r':
    print len(sys.argv)
    print sys.argv[1]
    vid = sys.argv[2]
    option = 'no vlan ' + vid
    cmd = [option]
    print 'Checking if VLAN %s exists' % vid
    try:
        check = pynet_sw3.enable("show vlan")
        unlist = check[0]
        for item in unlist['result']['vlans']:
            if vid in item:
                print 'VLAN does not exist'
            elif vid not in item:
                print 'Removing VLAN %s' % vid
                pynet_sw3.config(cmd)
                #pynet_sw3.enable("write memory")
            else:
                print 'eapi_create_vlan encountered a problem'
    except:
        print 'Unable to communicate with switch'
else:
    print 'eapi_create_vlan encountered a problem'

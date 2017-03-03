#!/usr/bin/env python

import pyeapi
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

shinterfaces = pynet_sw3.enable("show interfaces")
unlist = shinterfaces[0]
interfaces = unlist['result']
ethernets = []
for interface in interfaces['interfaces']:
	if 'Ethernet' in interface:
		 ethernets.append(interface)
for item in ethernets:
	print item
	print 'inOctets ' + str(interfaces['interfaces'][item]['interfaceCounters']['inOctets'])
	print 'outOctets ' + str(interfaces['interfaces'][item]['interfaceCounters']['outOctets'])
		

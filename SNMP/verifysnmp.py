#!/usr/bin/env python

try:
	import snmp_helper
	print "Hooray I can import SNMP Helper"
	exit()
except ImportError as e:
	print "I could not import the SNMP Helper"

#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

rtr1 = '184.105.247.70'
rtr2 = '184.105.247.71'
port = 161
comm_string = 'galileo'
device1 = (rtr1, comm_string, port)
device2 = (rtr2, comm_string, port)
sysname = '1.3.6.1.2.1.1.5.0'
sysdescr = '1.3.6.1.2.1.1.1.0'

#Function to retrieve SNMP data at an OID
def retrieveoid(device, oid):
	r = snmp_get_oid(device, oid)
	info = snmp_extract(r)
	print info + '\n'


#function call for rtr1 to get sysName
retrieveoid(device1, sysname)
#function call for rtr1 to get sysDescr
retrieveoid(device1, sysdescr)
#function call for rtr2 to get sysName
retrieveoid(device2, sysname)
#function call for rtr2 to get sysDescr
retrieveoid(device2, sysdescr)

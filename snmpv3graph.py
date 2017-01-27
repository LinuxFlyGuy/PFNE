#!/usr/bin/env python

from snmp_helper import snmp_get_oid_v3, snmp_extract

user = pysnmp
auth_key = 'galileo1'
auth_proto = 'sha'
enc_key = 'galileo1'
rtr1 = '184.105.247.70'
rtr2 = '184.105.247.71'
port = 161
snmp_user = (user, auth_key, enc_key)
device1 = (rtr1, port, snmp_user)
device2 = (rtr2, port, snmp_user)
sysname = '1.3.6.1.2.1.1.5.0'
sysdescr = '1.3.6.1.2.1.1.1.0'

#Function to retrieve SNMP data at an OID
def retrieveoid(device, oid):
	r = snmp_get_oid_v3(device, oid)
	info = snmp_extract(r)
	print info + '\n'

retrieveoid(device1, sysname)

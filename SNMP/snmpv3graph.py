#!/usr/bin/env python

import pygal, time
from snmp_helper import snmp_get_oid_v3, snmp_extract

user = 'pysnmp'
auth_key = 'galileo1'
auth_proto = 'sha'
enc_key = 'galileo1'
port = 161
rtr1 = ('184.105.247.70', port)
rtr2 = ('184.105.247.71', port)
snmp_user = (user, auth_key, enc_key)
sysname = '1.3.6.1.2.1.1.5.0'
sysdescr = '1.3.6.1.2.1.1.1.0'

#Function to retrieve SNMPv3 data at an OID
def retrieveoidv3(rtr, user, oid, proto):
	r = snmp_get_oid_v3(rtr, user, oid, proto)
	info = snmp_extract(r)
	print info + '\n'

#Execute this is script is run directly
if __name__ == '__main__':
	retrieveoidv3(rtr1, snmp_user, sysname, auth_proto)
	retrieveoidv3(rtr2, snmp_user, sysname, auth_proto)


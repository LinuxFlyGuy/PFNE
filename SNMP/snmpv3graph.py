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
oids = (
	('sysName' = '1.3.6.1.2.1.1.5.0'),
	('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)
duration = 10

#Function to retrieve SNMPv3 data at an OID
def retrieveoidv3(rtr, user, oid, proto):
	r = snmp_get_oid_v3(rtr, user, oid, proto)
	info = snmp_extract(r)
	print info + '\n'

#Execute this script if run directly
if __name__ == '__main__':
	while duration > 0:
		for n, oid in oids:
			retrieveoidv3(rtr1, snmp_user, oid, auth_proto)
			retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
			print "%s %s" % (n, oid)
		time.sleep(300)
		duration -= 1

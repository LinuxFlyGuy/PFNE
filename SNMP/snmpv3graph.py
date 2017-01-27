#!/usr/bin/env python

import pygal, time
from snmp_helper import snmp_get_oid_v3, snmp_extract

user = 'pysnmp'
auth_key = 'galileo1'
auth_proto = 'sha'
enc_key = 'galileo1'
port = 161
rtr1 = ('184.105.247.70', port)
snmp_user = (user, auth_key, enc_key)
oids = (
	('sysName', '1.3.6.1.2.1.1.5.0'),
	('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)
duration = 12
title = ''
interface = ''
ino = [0]
inu = [0]
outo = [0]
outu = [0]

#Function to retrieve SNMPv3 data at an OID
def retrieveoidv3(rtr, user, oid, proto):
	r = snmp_get_oid_v3(rtr, user, oid, proto)
	info = snmp_extract(r)
	return info

#Execute this script if run directly
if __name__ == '__main__':
	while duration > 0:
		for n, oid in oids:
			datapoint = retrieveoidv3(rtr1, snmp_user, oid, auth_proto)
			if 'sysName' in n:
				title = datapoint
			if 'ifDescr' in n:
				interface = datapoint
			if 'InOctets' in n:
				ino.append(int(datapoint) - ino[-1])
			if 'InUcast' in n:
				inu.append(int(datapoint) - inu[-1])
			if 'OutOctets' in n:
				outo.append(int(datapoint) - outo[-1])
			if 'OutUcast' in n:
				outu.append(int(datapoint) - outu[-1])
		time.sleep(300)
		duration -= 1

	#Generate input/output octets line chart
	chartoctets = pygal.Line()
	chartoctets.title = title + interface + 'Octets'
	chartoctets.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
	chartoctets.add('InOctets', ino)
	chartoctets.add('OutOctets', outo)
	chartoctets.render_to_file('octets.svg')

	#Generate input/output unicast packets line chart
	chartunicast = pygal.Line()
	chartunicast.title = title + interface + 'Unicast Packets'
	chartunicast.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
	chartunicast.add('InUcastPkts', inu)
	chartunicast.add('OutUcastPkts', outu)
	chartunicast.render_to_file('unicast.svg')

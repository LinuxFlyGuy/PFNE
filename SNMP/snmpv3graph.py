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
duration = 13
title = ''
interface = ''
in_octets_prior_value = 0
in_octets_diff = list()
in_unicasts_prior_value = 0
in_unicasts_diff = list()
out_octets_prior_value = 0
out_octets_diff = list()
out_unicasts_prior_value = 0
out_unicasts_diff = list()

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
				in_octets_diff.append(int(datapoint) - in_octets_prior_value)
				in_octets_prior_value = int(datapoint)
			if 'InUcast' in n:
				in_unicasts_diff.append(int(datapoint) - in_unicasts_prior_value)
				in_unicasts_prior_value = int(datapoint)
			if 'OutOctets' in n:
				out_octets_diff.append(int(datapoint) - out_octets_prior_value)
				out_octets_prior_value = int(datapoint)
			if 'OutUcast' in n:
				out_unicasts_diff.append(int(datapoint) - out_unicasts_prior_value)
				out_unicasts_prior_value = int(datapoint)
		time.sleep(300)
                duration -= 1

	#Generate input/output octets line chart
	chartoctets = pygal.Line()
	chartoctets.title = title + interface + ' Octets'
	chartoctets.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
	chartoctets.add('InOctets', in_octets_diff[1:13])
	chartoctets.add('OutOctets', out_octets_diff[1:13])
	chartoctets.render_to_file('octets.svg')

	#Generate input/output unicast packets line chart
	chartunicast = pygal.Line()
	chartunicast.title = title + interface + ' Unicast Packets'
	chartunicast.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
	chartunicast.add('InUcastPkts', in_unicasts_diff[1:13])
	chartunicast.add('OutUcastPkts', out_unicasts_diff[1:13])
	chartunicast.render_to_file('unicast.svg')

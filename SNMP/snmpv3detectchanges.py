#!/usr/bin/env python

import time, pickle, json, yaml, email_helper
from snmp_helper import snmp_get_oid_v3, snmp_extract

user = 'pysnmp'
auth_key = 'galileo1'
auth_proto = 'sha'
enc_key = 'galileo1'
port = 161
rtr2 = ('184.105.247.71', port)
snmp_user = (user, auth_key, enc_key)
sysUptime = '1.3.6.1.2.1.1.3.0'
oids = (
	('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0'),
	('ccmHistoryRunningLastSaved', '1.3.6.1.4.1.9.9.43.1.1.2.0'),
	('ccmHistoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0')
)
#Function to retrieve SNMPv3 data at an OID
def retrieveoidv3(rtr, user, oid, proto):
	r = snmp_get_oid_v3(rtr, user, oid, proto)
	info = snmp_extract(r)
	return info

#Function to write initial files as baseline
def write_files(choice):
	for n, oid in oids:
		data = retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
		if choice == 1:
			f = open(n + '.pkl', "wb")
			pickle.dump(data, f)
			f.close()
		elif choice == 2:
			with open(n + '.json', "w") as f:
				json.dump(data, f)
		elif choice == 3:
			with open(n + '.yml', "w") as f:
				yaml.dump(data, f)
		else:
			print "Something went horribly wrong"
			exit()

#Function to compare current router data to baseline file data
def compare_data(choice):
	for n, oid in oids:
		data = retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
		if choice == 1:
			f = open(n + '.pkl', "rb")
			a = pickle.load(f)
			if data != a:
				timestamp = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				to = 'vagrant83@gmail.com'
				subject = 'Configuration change detected'
				message = '''
					A configuration change was detected at %s

					Regards,
					Myself ''' % timestamp
				sender = 'vagrant83@gmail.com'
				email_helper.send_mail(to, subject, message, sender)
				write_files(choice)
		elif choice == 2:
			with open(n + '.json') as f:
				a = json.load(f)
			if data != a:
				timestamp = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				to = 'vagrant83@gmail.com'
				subject = 'Configuration change detected'
				message = '''
					A configuration change was detected at %s

					Regards,
					Myself ''' % timestamp
				sender = 'vagrant83@gmail.com'
				email_helper.send_mail(to, subject, message, sender)
				write_files(choice)
		elif choice == 3:
			with open(n + '.yml') as f:
				a = yaml.load(f)
			if data != a:
				timestamp = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				to = 'vagrant83@gmail.com'
				subject = 'Configuration change detected'
				message = '''
					A configuration change was detected at %s

					Regards,
					Myself ''' % timestamp
				sender = 'vagrant83@gmail.com'
				email_helper.send_mail(to, subject, message, sender)
				write_files(choice)
		else:
			print "Something went horribly wrong"
			exit()

#Execute this if script is run directly
if __name__ == '__main__':
	print '''Save data in which format?
	1 - Pickle
	2 - JSON
	3 - YAML \n'''
	option = raw_input("Enter the number of your selection: ")
	if int(option) >=1 and int(option) <=3:
		choice = int(option)
	else:
		print "That is not a valid choice; defaulting to Pickle"
		choice = 1
	write_files(choice)
	while True:
		compare_data(choice)
		time.sleep(15)

#!/usr/bin/env python

import smtplib, time, pickle, json, yaml
from email.mime.text import MIMEText
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
to = 'vagrant83@gmail.com'
subject = 'Configuration Change Detected'
sender = 'python@script.net'
#Function to retrieve SNMPv3 data at an OID
def retrieveoidv3(rtr, user, oid, proto):
	r = snmp_get_oid_v3(rtr, user, oid, proto)
	info = snmp_extract(r)
	return info

#Function to send email
def send_mail(receipient, subject, message, sender):
	subject = MIMEText(message)
	message['Subject'] = subject
	message['From'] = sender
	message['To'] = recipient
	smtp_conn = smtplib.SMTP('localhost')
	smtp_conn.sendmail(sender, recipient, message.as_string())
	smtp_conn.quit()
	return True

def write_files(choice):
	for n, oid in oids:
		data = retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
		if choice == 1:
			f = open('configchange.pkl', "wb")
			pickle.dump(data, f)
			f.close()
		elif choice == 2:
			with open('configchange.json', "w") as f:
				json.dump(data, f)
		elif choice == 3:
			with open('configchange.yml', "w") as f:
				yaml.dump(data, f)
		else:
			print "Something went horribly wrong"
			exit()


def compare_data(choice):
	for n, oid in oids:
		data = retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
		if choice == 1:
			f = open('configchange.pkl', "rb")
			a = pickle.load(f)
			if data != a:
				time = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				message = "A configuration change was detected at", time
				send_mail(to, subject, message, sender)
		elif choice == 2:
			with open('configchange.json') as f:
				a = json.loads(f)
			if data != a:
				time = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				message = "A configuration change was detected at", time
				send_mail(to, subject, message, sender)
		elif choice == 3:
			with open('configchange.yml') as f:
				a = yaml.loads(f)
			if data != a:
				time = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
				message = "A configuration change was detected at", time
				send_mail(to, subject, message, sender)
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

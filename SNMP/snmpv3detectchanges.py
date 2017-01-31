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
changes = {}
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
	while True:
		for n, oid in oids:
			data = retrieveoidv3(rtr2, snmp_user, oid, auth_proto)
			if choice == 1:
				f = open('configchange.pkl', "wb")
				pickle.dump(changes, f)
				f.close()
			elif choice == 2:
				with open('configchange.json', "w") as f:
					json.dump(changes, f)
			elif choice == 3:
				with open('configchange.yml', "w") as f:
					f.write(yaml.dump(changes, default_flow_style=False))
			else:
				print "Something went horribly wrong"
			if int(option) == 1:
				f = open('configchange.pkl', "rb")
				a = pickle.load(f)
			elif int(option) == 2:
				with open('configchange.json', "r") as f:
					a = json.loads(f)
			elif int(option) == 3:
				with open('configchange.yml') as f:
					a = yaml.loads(f)
				else:
					print "Something went horribly wrong"
			if data != a:
		to = 'vagrant83@gmail.com'
		subject = 'Configuration Change Detected'
		sender = 'python@script.net'
		time = retrieveoidv3(rtr2, snmp_user, sysUptime, auth_proto)
		send_mail(to, subject, message, sender)
		time.sleep(60)

#!/usr/bin/env python

import telnetlib

#telnet connection parameters
ip = '184.105.247.70'
port = 23
to = 8
user = 'pyclass'
pw = '88newclass'
remote_conn = ''

#interactive menu function
def menu():
	global remote_conn
	print '''1 - Issue Command
2 - Close Connection \n'''
	choice = raw_input('Enter the number of your selection: ')
	if choice == '1':
		comm = raw_input('Type the command to execute: ')
		telnetinteract(comm)
	elif choice =='2':
		remote_conn.close()
		print "The connection has been closed; goodbye"
		exit()
	else:
		print "That is not a valid choice"
		menu()

#function to open telnet connection
def telnetconnect(ip_add, port_num, timeout):
	global remote_conn
	print "Connecting to switch"
	remote_conn = telnetlib.Telnet(ip_add, port_num, timeout)
	x = remote_conn.read_until('sername', timeout)
	print x
	remote_conn.write(user + '\n')
	y = remote_conn.read_until('assword', timeout)
	print y
	remote_conn.write(pw + '\n')
	print "Logged in to switch \n"
	menu()

# function to interact with switch
def telnetinteract(command):
	global remote_conn
	remote_conn.write(command + '\n')
	r = remote_conn.read_very_eager()
	print r.rstrip() + '\n'
	menu()

if __name__ == '__main__':
	telnetconnect(ip, port, to)
	menu()

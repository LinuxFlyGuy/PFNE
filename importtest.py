#!/usr/bin/env python

try:
	from my_func import print_hello
	print_hello()
except ImportError as e: 
	print "Module my_func could not be found."

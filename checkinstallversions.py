#!/usr/bin/env python

import pysnmp, paramiko

print "Yay, I have all of my libraries! \n"

snmp = pysnmp.__version__
mymiko = paramiko.__version__

print "Your installed version of pysnmp is %r. \n" % (snmp)
print "Your installed version of paramiko is %r. \n" % (mymiko)

#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto = cisco_cfg.find_objects(r"^crypto map")
group2 = list()
nonaes = list()

print "\n Here all of the crypto map entries and their children: \n"

for c in crypto:
	print c.text
	for d in c.children:
		print d.text
		if "set pfs group2" in d.text:
			group2.append(c)

print "\n Now let's find all of the entries that are using PFS group2 \n"
for i in group2:
	print i.text

print "\n Now let's show all of the entries that are not using AES encryption \n"
algorithm = cisco_cfg.find_objects(r"set transform-set")
for a in algorithm:
	if "set transform-set AES-SHA" not in a.text:
		nonaes.append(a.parent)
	else:
		continue
for n in nonaes:
	print n.text

#!/usr/bin/env python

import yaml, json

with open("testlist.yml", "r") as f: 
	y = yaml.load(f)
print "Here's the pretty YAML:"
print yaml.dump(y)
with open("testlist.json", "r") as f:
	j = json.load(f)
print "Here's the pretty JSON:"
print json.dumps(j, indent=4)

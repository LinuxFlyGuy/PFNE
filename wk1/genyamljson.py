#!/usr/bin/env python

import yaml, json

testlist = ['item0', 'item1', 'thing2', {'thing3_name': 'Geoffrey'}]

print "Creating YAML file."
with open("testlist.yml", "w") as f:
	f.write(yaml.dump(testlist, default_flow_style=False))
print "Finished creating YAML file."

print "Creating JSON file."
with open("testlist.json", "w") as f:
	json.dump(testlist, f)
print "Finished creating JSON file."

print "Have a great time with your new files!"

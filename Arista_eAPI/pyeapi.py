import pyeapi
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet_sw3")
pynet_sw4 = pyeapi.connect_to("pynet_sw4")

my_config = pynet_sw3.get_config()
for line in my_config:
    print line

my_config2 = pynet_sw3.get_config(as_string=True)
print my_config2

shversion = pynet_sw3.enable("show version")
pprint(shversion)

write = pynet_sw3.enable("write memory")
pprint(write)

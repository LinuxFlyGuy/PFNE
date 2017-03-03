#!/usr/bin/env python

import pyeapi
from pprint import pprint

pynet_sw3 = pyeapi.connect_to("pynet-sw3")

shinterfaces = pynet_sw3.enable("show interfaces")
pprint(shinterfaces)

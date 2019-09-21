#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
       ip, identity, usrname, time, zone, method, path, protocol, status, size = data
	   
       if path[:17] == 'http://www.the-as':
           path = path[31:]
       print path
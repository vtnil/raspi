#!/usr/bin/python

def servo (pin, deg):
  os.system("./servo %s %s" %(pin,deg))

import sys
import os

pin=2
vpin=3

if len(sys.argv)<3:
  print "need two arguments 'vdegr' and 'degr'"
  exit()
else:
  vdeg=int(sys.argv[1]);
  deg=int(sys.argv[2]);

servo(vpin,vdeg)
servo(pin,(180-deg))

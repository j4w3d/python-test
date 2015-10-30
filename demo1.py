#!/usr/bin/python

from sys import argv
try:
  script, first, second, third = argv
except ValueError:
  print '\nusage: demo1.py <arg1> <arg2> <arg3>\n'
  exit()   
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

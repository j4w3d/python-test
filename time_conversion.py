#!/usr/bin/python

input_time=raw_input()
if input_time.find('AM')>-1:
   temp=input_time.strip('AM').split(':')
   hh=int(temp[0])
   mm=int(temp[1])
   ss=int(temp[2])
   if hh==12:
      hh=0


elif input_time.find('PM')>-1:
   temp=input_time.strip('PM').split(':')
   hh=int(temp[0])
   mm=int(temp[1])
   ss=int(temp[2])
   print hh,'::',mm,'::',ss



else:
   print "INVALID time format"


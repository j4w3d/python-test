#!/usr/bin/python

from sys import argv
try:
  script, number = argv
except ValueError:
  print '\nusage: demo1.py number\n'
  exit()   
number=int(number)
if number>6:
  print "no > 6 "
  exit()
a=[]
for i in range(number):
    b=[]
    print "  "*(number-i-1),
    for j in range(i+1):
       if j==0 or i==j:
          b.append(1)      
       else:
          b.append(a[i-1][j-1]+a[i-1][j])
       print " ",b[j],
    print " "
    a.append(b)

print "\n----------------------\n"
for i in a:
  for j in i:
   print " ",j,
  print " ";

#!/usr/bin/python

import MySQLdb,getpass
host=raw_input(" Host : ")
user=raw_input(" User : ")
pswd=getpass.getpass(" Password:")
db=MySQLdb.connect(host,user,pswd)
c=db.cursor()
c.execute("show databases;")
row=c.fetchall()
for r in row:
  if 'schema' in r[0] or 'mysql' in r[0] :
     print r[0],'not dropped'
  else:
     c.execute('drop database '+r[0])

db.close()


#!/usr/bin/python

import MySQLdb,getpass
#host=raw_input(" Host : ")
#user=raw_input(" User : ")
#pswd=getpass.getpass(" Password:")
db=MySQLdb.connect('192.168.0.163','root','python')
c=db.cursor()
c.execute("select user,host from mysql.user")
row=c.fetchall()
user_info=[]
for r in row:
  detail={
     'user':r[0],
     'host':r[1]
       }
  user_info.append(detail)
db.commit()
db.close()


db2=MySQLdb.connect('localhost','root',' ')
c2=db2.cursor()
c2.execute("create database if not exists python_db")
c2.execute("use python_db")
c2.execute("create table if not exists user_info (id int AUTO_INCREMENT PRIMARY KEY,user varchar(30),host varchar(30))")
for u in user_info:
     c2.execute("""INSERT into user_info (user, host) values ('%s', '%s')"""%(u['user'],u['host']))

db2.commit()
db2.close()




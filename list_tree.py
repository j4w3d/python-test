#!/usr/bin/python


import os,time

def sizeformat(data):
    # return in GB format
     if data > 1024*1024*1024:
         data=round(data*1.0/(1024*1024*1024),2)
         return str(data)+" GB"
    # return in MB format                     
     elif data > 1024*1024:
         data=round(data*1.0/(1024*1024),2)
         return str(data)+" MB"
    # return in GB format                     
     elif data > 1024:
         data=round(data*1.0/(1024),2)
         return str(data)+" KB"
     else : # in Bytes
         
         return str(data)+" Bytes"


dir_path='/path/to/directory'
i=1
l=0
fs1=open('skeleton.txt','w')
fs2=open('files_info.txt','w')
total_size=0
total_files=0
total_dirs=0
for root,dir,files in os.walk(dir_path):
    if i==1:
      l=(len(root.split('/')))
      root_data=root.split('/')[-1]
      print root_data
      fs1.write(root_data+'\n')
    else : 
      root_data=" |   "*((len(root.split('/')))-l-1)+" +---"+root.split('/')[-1]
      total_dirs+=1
      print root_data
      fs1.write(root_data+'\n')

    for f in files:
        ff=os.path.join(root,f)
        p=os.stat(ff)
        f_detail=ff+"\n\t\tsize:"+sizeformat(p.st_size)+"\n\t\tcreated:"+time.ctime(p.st_ctime)+"\n\t\tmodified:"+time.ctime(p.st_mtime)+"\n\t\tAccess:"+time.ctime(p.st_atime)
        total_size+=p.st_size
        total_files+=1
        fs2.write('\n')
        fs2.write("FILE"+str(total_files)+"#"+f_detail)
        fs2.write('\n-----------------------------------------------------------------------------------\n')
        f_info= " |   "*((len(root.split('/'))+1)-l)+f
        print f_info
        fs1.write(f_info+'\n')
        

    print " |   "*((len(root.split('/'))+1)-l)
    fs1.write(" |   "*((len(root.split('/'))+1)-l)+'\n')
    i+=1




fs2.write("Total Directories : "+str(total_dirs)+"\nTotal Files : "+str(total_files)+"\nTotal Size : "+sizeformat(total_size))
fs1.close()
fs2.close()

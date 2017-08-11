#-*- coding:utf-8 -*-
import os,sys
count=int(sys.argv[2])
file_path=sys.argv[1]
with open(file_path,'r') as fr:
    for each in fr:
        print (each)
        count-=1
        if count==0:
            break


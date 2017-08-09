#-*- coding:utf-8 -*-
import hashlib,sys
sha256=hashlib.sha256()
# just change 'r' to 'rb'
with open(sys.argv[1],'rb') as fr:
    for each in fr:
        sha256.update(each)
hash_value=sha256.hexdigest()
print hash_value

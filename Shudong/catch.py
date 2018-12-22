#!/usr/bin/env python
#coding=utf-8

import os
import time
for pid in range(125413,126962):
    # try:
    comm = '''
    input your {} comm
    '''.format(pid)
    # comm.replace("\r","")
    # comm.replace("\n","")
    text = os.popen(comm, 'r').read()
    if """"data":{}""" in text:
        print "[-] " + "Gets " + str(pid) + " failed!"
        continue
    # print text
    print "[+] " + "Gets " + str(pid) + " successed!"
    # except:
    #     print "Gets failed!
    # try:
    f = open("./text/" + str(pid) + ".txt",'w')
    f.write(text)
    f.close()
    # except:
    #     print "Write file failed!"
    # time.sleep(2)

    # \{"errcode":0,"errmsg":"","data":\{.*\}\}
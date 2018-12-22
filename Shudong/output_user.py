#!/usr/bin/env python
#coding=utf-8

import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

files = os.listdir("./text")
for file in files:
    if not os.path.isdir(file):
        blog = open("./text/" + file).read()
        print file
        js = json.loads(blog)
        title = js['data']['text']
        auth_uid = js['data']['user']['uid']
        auth_openid = js['data']['user']['openid']
        path = "./user/" + str(auth_uid) + "_" + str(auth_openid) + ".txt"
        f = open(path, 'a+')
        # print js['data']['text']
        f.writelines("Topic: " + str(title))
        f.write('\n')
        f.writelines("Time: " + str(js['data']['time']))
        f.write('\n')

        comments = js['data']['comments']
        comm_list_uid = []
        if comments != []:
            for comm in comments:
                comm_uid = comm['uid']
                comm_openid = comm['openid']
                comm_f = open("./user/" + str(comm_uid) + "_" + str(comm_openid) + ".txt", 'a+')
                if comm_uid != auth_uid and comm_uid not in comm_list_uid:
                    comm_f.writelines("Comment for: " + str(js['data']['text']))
                    comm_f.write("\n")
                    comm_list_uid.append(comm_uid)
                    # print comm_list_uid, comm_uid
                comm_f.writelines("Comment: " + comm['content'])
                comm_f.write('\n')  
                comm_f.close()

        f.write('\n')
        f.close()
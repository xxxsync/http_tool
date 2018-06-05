#!/usr/bin/python3
#xxxsync
#coding=utf-8
import threading;
import sys;
import getopt;
import time;
from http_req import Http_Req;

vip = '10.200.6.171'
vport = 8090
vhttps_port = 443
host = 'www.test.com'
url = '/test.html'
argname = "number"

my_req = Http_Req(vip, vport, vhttps_port, host, url)

def Create_Req(count):
    file1 = open("email_1000.txt", "r", encoding = "utf-8")
    for i in range(count):
        line = file1.readline()
        if not line:
            break;
        line = line.strip('\n')
        my_req.send_http_get(argname, line)
    file1.close()
    time.sleep(1)

def Create_SReq(count):
    file1 = open("email_1000.txt", "r", encoding = "utf-8")
    for i in range(count):
        line = file1.readline()
        if not line:
            break;
        line = line.strip('\n')
        my_req.send_https_get(argname, line)
    file1.close()

def Create_Others():
    for i in range(1):
        my_req.send_http_others("TRACE", argname, "Thisisargtest")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hsi:")
    except getopt.GetoptError:
            print("usage:\n\t-i [count];\n\t-h Create http req;\n\t-s Create https req;")
            sys.exit(2)

    for opt,arg in opts:
        if opt == '-h':
            Create_Req(1)
        elif opt == '-s':
            Create_SReq(1)
        elif opt == '-i':
            Create_Req(int(arg))
        else:
            print("usage:\n\t-i [count];\n\t-h Create http req;\n\t-s Create https req;")

if __name__ == "__main__":
    main()

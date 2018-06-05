#!/usr/bin/python3
#xxxsync
#coding=utf-8
import http.client, threading;
import urllib, ssl;
import time;

class Http_Req:

    def __init__(self, ip, http_port, https_port, host, url):
        self.ip = ip
        self.http_port = http_port
        self.https_port = https_port
        self.host = host
        self.url = url


    def send_http_get(self, argname, argvalue):
        headers = {"Host":self.host,
                   "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
                   "Accept":"image/jpeg, image/gif, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
                   "Accept-Language":"zh-CN",
                   "Accept-Encoding":"gzip, deflate",
                   #"Content-Type":"application/x-www-form-urlencoded",
                   "Connection":"close",
                   "Cookie":"ping_http=test"}
        conn = http.client.HTTPConnection(self.ip, self.http_port)
        conn.connect()
        params=urllib.parse.quote(argvalue)
        conn.request(method="GET", url=self.url+"?"+argname+"="+params, headers = headers)
        response = conn.getresponse();
        print(response.status, response.reason)
        #resdata = response.read()
        #print(resdata)
        conn.close()

    def send_https_get(self, argname, argvalue):
        headers = {"Host":self.host,
                   "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
                   "Accept":"image/jpeg, image/gif, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
                   "Accept-Language":"zh-CN",
                   "Accept-Encoding":"gzip, deflate",
                   #"Content-Type":"application/x-www-form-urlencoded",
                   "Connection":"close",
                   "Cookie":"ping_https=test"}
        gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        conn = http.client.HTTPSConnection(self.ip, self.https_port, context = gcontext)
        conn.connect()
        params=urllib.parse.quote(argvalue)
        conn.request(method="GET", url=self.url+"?"+argname+"="+params, headers = headers)
        response = conn.getresponse();
        print(response.status, response.reason)
        #resdata = response.read()
        #print(resdata)
        conn.close()

    def send_http_post(self, argname, argvalue):
        headers = {"Host": self.host,
                   "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
                   "Accept":"image/jpeg, image/gif, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
                   "Accept-Language":"zh-CN",
                   "Accept-Encoding":"gzip, deflate",
                   #"Content-Length" : "0",
                   "Connection":"close",
                   "Cookie":"ping_http=test"}
        conn = http.client.HTTPConnection(self.ip, self.http_port)
        conn.connect()
        params = urllib.parse.urlencode({argname:argvalue})
        conn.request(method="POST", url=self.url, headers = headers, body = params)
        response = conn.getresponse();
        print(response.status, "\n", response.reason)
        #resdata = response.read()
        #print(resdata)
        conn.close()

    def send_https_post(self, argname, argvalue):
        headers = {"Host": self.host,
                   "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
                   "Accept":"image/jpeg, image/gif, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
                   "Accept-Language":"zh-CN",
                   "Accept-Encoding":"gzip, deflate",
                   #"Content-Length" : "0",
                   "Connection":"close",
                   "Cookie":"ping_https=test"}
        gcontext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        conn = http.client.HTTPSConnection(self.ip, self.https_port, context = gcontext)
        params = urllib.parse.urlencode({argname:argvalue})
        conn.connect()
        conn.request(method="POST", url=self.url, headers = headers, body = params)
        response = conn.getresponse();
        print(response.status, "\n", response.reason)
        #resdata = response.read()
        #print(resdata)
        conn.close()

    def send_http_others(self, method, argname, argvalue):
        headers = {"Host":self.host,
                   "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
                   "Accept":"image/jpeg, image/gif, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
                   "Accept-Language":"zh-CN",
                   "Accept-Encoding":"gzip, deflate",
                   #"Content-Type":"application/x-www-form-urlencoded",
                   "Connection":"close",
                   "Cookie":"ping_http=test"}
        conn = http.client.HTTPConnection(self.ip, self.http_port)
        conn.connect()
        params=urllib.parse.quote(argvalue)
        conn.request(method=method, url=self.url+"?"+argname+"="+params, headers = headers)
        response = conn.getresponse();
        print(response.status, response.reason)
        resdata = response.read()
        #print(resdata)
        conn.close()



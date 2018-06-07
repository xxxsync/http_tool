#!/usr/bin/python
#coding=utf-8
from http.server import BaseHTTPRequestHandler, HTTPServer
import os 
#import SocketServer

rootdir = '/usr/local/apache2/htdocs'
class S(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    def _set_headers(self, content_length, mimetype):
        print("set header...")
        self.send_response(200)
        self.send_header('Content-type', mimetype)
        if(content_length != 0):
            self.send_header('Content-length', content_length)
        self.end_headers()
        self.flush_headers()


    def do_GET(self):
        try:
            if self.path.endswith(".html"):
            	mimetype = "text/html"
            elif self.path.endswith(".png"):
                mimetype = 'image/png'	
            else:
                mimetype = "text/html"
            url = self.path.split("?")
            print(url[0])
            url_path = open(rootdir + url[0], "rb")
            content_length = os.stat(rootdir + url[0]).st_size
            print(content_length, mimetype)
            self._set_headers(content_length, mimetype)
            print('do get header...')
            self.wfile.write(url_path.read())           
            url_path.close()
        except IOError:
            default_str = b"<html><body><h1>Hi! Get!</h1></body></html>"
            self._set_headers(len(default_str), 'text/html')
            self.wfile.write(default_str)
	    

    def do_HEAD(self):
        mimetype = "text/html"
        print('do head header...')
        self._set_headers(0, mimetype)

    def do_TRACE(self):
        mimetype = "text/html"
        print('do trace header...')
        self._set_headers(0, mimetype)
        
    def do_POST(self):
        try:
            if self.path.endswith(".html"):
            	mimetype = "text/html"
            elif self.path.endswith(".png"):
                mimetype = 'image/png'	
            else:
                mimetype = "text/html"
            url = self.path.split("?")
            print(url[0])
            url_path = open(rootdir + url[0], "rb")
            content_length = os.stat(rootdir + url[0]).st_size
            print(content_length, mimetype)
            self._set_headers(content_length, mimetype)
            print('do post header...')
            self.wfile.write(url_path.read())           
            url_path.close()
        except IOError:
            default_str = b"<html><body><h1>Hi! POST!</h1></body></html>"
            self._set_headers(len(default_str), 'text/html')
            self.wfile.write(default_str)
	
        
def run(server_class=HTTPServer, handler_class=S, port=8080):
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print('Starting httpd...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

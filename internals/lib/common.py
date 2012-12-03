#!/usr/bin/env python
# encoding: utf-8
"""
common.py
"""

#AFE Version
version = "2.0"

import SimpleHTTPServer
import time
import SocketServer
import logging
import cgi

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print self.headers
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print self.headers
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            print item
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

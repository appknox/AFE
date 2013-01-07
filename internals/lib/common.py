#!/usr/bin/env python
# encoding: utf-8
"""
common.py
"""

#AFE Version
version = "2.0"

import SimpleHTTPServer, time, SocketServer, logging, cgi, os, cmd, socket, sys, urllib2

class COLOR:
    WHITE = '\033[37m'
    GRAY = '\033[30m'
    BLUE = '\033[34m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    RED = '\033[91m'
    ENDC = '\033[1;m'

class Server:
    """Server class"""

    def __init__(self, ip, port, direction):
        self.ip = ip
        self.port = port
        self.direction = direction
        self.socketConn = None

    def __del__(self):
        try:
            self.socketConn.close()
        except Exception:
            pass

    def connectSocket(self):
        try:
            self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socketConn.connect((self.ip, self.port))
            return True
        except socket.error:
            return False

    def sendData(self, data):
        self.connectSocket()
        self.socketConn.sendall(data)

    def receiveData(self):
        return self.socketConn.recv(2048)

    def closeSocket(self):
        self.socketConn.close()
        self.socketConn = None


class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def __del__(self):
	self.log.close()

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


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

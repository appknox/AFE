#!/usr/bin/python
import time
import socket	#for sockets
import sys	#for exit

class Server:
    """Session class"""

    def __init__(self, ip, port, direction):
        self.ip = ip
        self.port = port
        self.direction = direction
        self.socketConn = None

    def __del__(self):
        try:
            self.socketConn.close()
        # FIXME: Choose specific exceptions to catch
        except Exception:
            pass

    # Returns socket connected status = True/False
    def connectSocket(self):
        try:
            self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #self.socketConn.settimeout(10.0)
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


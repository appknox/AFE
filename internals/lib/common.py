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




class BaseCmd(cmd.Cmd):

    def __init__(self, session):
        cmd.Cmd.__init__(self)
        self.ruler = "-"
        self.doc_header = "Commands - type help <command> for more info"
        self.session = session
        self._hist = []      ## No history yet
        self._locals = {}      ## Initialize execution namespace for user
        self._globals = {}
        self.cmdline = None

    ## Command definitions to support Cmd object functionality ##
    def do_help(self, args):
        """
Get help on commands
'help' or '?' with no arguments prints a list of commands for which help is available
'help <command>' or '? <command>' gives help on <command>
        """
        ## The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    ## Override methods in Cmd object ##
    def preloop(self):
        """
Initialization before prompting user for commands.
Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist = []      ## No history yet
        self._locals = {}      ## Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """
Take care of any unfinished business.
Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)   ## Clean up command completion

    def precmd(self, line):
        """
This method is called after the line has been input but before
it has been interpreted. If you want to modifdy the input line
before execution (for example, variable substitution) do it here.
        """
        self._hist += [ line.strip() ]
        return line

    def postcmd(self, stop, line):
        """
If you want to stop the console, return something that evaluates to true.
If you want to do some post command processing, do it here.
        """
        return stop


    def emptyline(self):
        """
Do nothing on empty input line
        """
        pass

    def default(self, line):
        """
Called on an input line when the command prefix is not recognized.
        """
        print "Command not found\n"
     
    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    def do_clear(self, line):
	    """
This command clears the screen or the terminal window!
	    """
	    if os.name == 'nt':
	        os.system('cls')
	    else:
	        os.system('clear')
    
    def do_exit(self, line):
        """
This command exits to the terminal window!
	""" 
        sys.exit(0)

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

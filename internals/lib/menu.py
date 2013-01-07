#!/usr/bin/python

import argparse, shlex, sys, urllib2, time, SocketServer
from common import Server, version, ServerHandler
from basecmd import *
from subprocess import call
from modules import Modules


class Menu(BaseCmd):

    def __init__(self, conn, session):
        BaseCmd.__init__(self, session)
        self.connected = conn
        self.session = session
        if (conn == 1):
            self.prompt = "*Afe/menu$ "
        else:
            self.prompt = "Afe/menu$ "

    def do_back(self, _args):
        """
Return to home screen
        """
        return -1


    def do_devices(self, _args):
        """
List Connected Devices 
        """
        call(["adb", "devices"])

    def do_modules(self, args):
	    """
Shows all the modules present in the Modules directory
	    """
	    subconsole = Modules(self.connected, self.session)
	    subconsole.cmdloop()
	
    def do_query(self, args):
        """
Query the TCP Server!
    Usage: query <arguments> [<arguments> ...]
For getting the content providers, which are exported or not
    Usage: query exported
For querying the content providers,
    Usage: query "[Arguments]"
           [Arguments]:
           get --url   = The content provider URI
               --proj  = The Projections, seperated by comma
     Example Usage:
           query "get --url content://dcontent/providers"
        """
        try:
            parser = argparse.ArgumentParser(prog="query", add_help = False)
            parser.add_argument('argu', metavar="<arguments>", nargs='+')
            splitargs = parser.parse_args(shlex.split(args))
            sendbuf = ' '.join(splitargs.argu)
            sendbuf1 = sendbuf.strip()
            if(self.connected == 1):
                self.session.sendData(sendbuf + "\n")
                resp = self.session.receiveData()
                print resp
            else:
                print "**Not connected to the AFE SERVER App !"
        except:
            pass
    def do_serve(self, args):
	    """
Starts a Server in Localhost with your predefined port!
    Usage: serve -p --port <port>
           Default Port is 8080
	    """
            try:
                parser = argparse.ArgumentParser(prog="serve", add_help = False)
                parser.add_argument('--port', '-p', metavar = '<port>', type=int)
                splitargs = parser.parse_args(shlex.split(args))
                if (splitargs.port):
                    PORT = int(splitargs.port)
                else:
                    PORT = 8080
                
                Handler = ServerHandler
                httpd = SocketServer.TCPServer(("", PORT), Handler)
                print "serving at port ", PORT
                httpd.serve_forever()
            except KeyboardInterrupt:
                httpd.server_close()
                print time.asctime(), "Server Stops - At this point"
            except:
                pass

#!/usr/bin/python
# encoding: utf-8
import argparse, shlex, sys, urllib2, time, SocketServer, base64, os, ntpath
from common import Server, version, ServerHandler
from basecmd import *
from subprocess import call
from modules import Modules
from exploit import Exploits

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break


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
	
    def do_exploit(self, args):
	    """
Shows all the modules present in the Modules directory
	    """
	    subconsole = Exploits(self.connected, self.session)
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
           app <appname space> = Give the app name space to check if the app exists or not
     Example Usage:
           query "get --url content://dcontent/providers"
           query "app com.afe.socket"
        """
        try:
            parser = argparse.ArgumentParser(prog="query")
            subparsers = parser.add_subparsers(help='sub-command help')
            parser_get = subparsers.add_parser('get', help="get help")
            parser_get.add_argument('--url', metavar="<URL>", dest='url', help='The content provider URI')
            parser_get.add_argument('--proj', metavar="<PROJECTIONS>", dest='proj', help='The Projections, seperated by comma')
            parser_app = subparsers.add_parser('app', help="Give the app name space to check if the app exists")
            parser_app.add_argument('package', metavar="<PACKAGE NAME>", dest='package', help='Give the app package name to check if the app exists or not')
            parser.add_argument('--file', '-f', metavar = '<file>', dest='file')
            splitargs = parser.parse_args(shlex.split(args))
            if(self.connected == 1):
                if(splitargs.file):
                    if(os.path.isfile(splitargs.file)):
                        fname = path_leaf(splitargs.file)
                        try:
                            fsize = os.stat(splitargs.file).st_size
                        except e:
                            print e
                        print "Sending file " + fname + " of size " + str(fsize)
                        init = fname + " : " + str(fsize)
                        self.session.sendData(init + "\n")
                        resp = self.session.receiveData()
                        if resp == "ok":
                            fin = open(splitargs.file, "rb")
                            binary_data = fin.read()
                            fin.close()
                            self.session.sendData(sendbuf + "\n")
                            resp = self.session.receiveData()
                            print "Data Sent !!"
                        else:
                            print "Something went wrong !"
                    else:
                        print "False"
                elif (splitargs.argu):
                    sendbuf = ' '.join(splitargs.argu)
                    sendbuf = sendbuf.strip()
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

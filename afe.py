#!/usr/bin/python
#
# License: Refer to the README in the root directory
#
import os
import xml.dom.minidom
import argparse, shlex, sys, urllib2
from xml.dom.minidom import parseString
from internals.lib.basecmd import BaseCmd
from internals.lib.menu import Menu
from internals.lib.server import Server
from internals.lib.common import version

class Afe(BaseCmd):

    def __init__(self):
        BaseCmd.__init__(self, None)
        self.prompt = "Afe$ "
        self.connected = 0
        #self.session = None
        self.intro = """
---- The Android Framework For Exploitation v2.0  ----
 _______  _______  _______                _______     _______ 
(  ___  )(  ____ \(  ____ \    |\     /|  / ___   )   (  __   )
| (   ) || (    \/| (    \/ _  | )   ( |  \/   )  |   | (  )  |
| (___) || (__    | (__    (_) | |   | |      /   )   | | /   |
|  ___  ||  __)   |  __)       ( (   ) )    _/   /    | (/ /) |
| (   ) || (      | (       _   \ \_/ /    /   _/     |   / | |
| )   ( || )      | (____/\(_)   \   /    (   (__/\ _ |  (__) |
|/     \||/       (_______/       \_/     \_______/(_)(_______)
                                                            
Copyright Reserved : XYS3C (Visit us at http://xysec.com)
----------------------------------------------------------
'help <command>' or '? <command>' gives help on <command>
        """

    #def do_exit(self, _args):
    #    """
#Exits from AFE
#        """
#        return -1

    def do_version(self, _args):
        """
Version and author information
        """
        print "\nAFE V", version, "\n"
        print "XYSEC @ http://xysec.com\n"
        
    def do_connect(self, args):
        """
Connects to a remote TCP Server
usage: connect [--port <port>] ip
Use adb forward tcp:12346 tcp:12346 when using an emulator or usb-connected device
        """
        try:        
            parser = argparse.ArgumentParser(prog="connect", add_help = False)
            parser.add_argument('ip')
            parser.add_argument('--port', '-p', metavar = '<port>')
            splitargs = parser.parse_args(shlex.split(args))
            if not splitargs:
                return
            ip = splitargs.ip
            if (splitargs.port):
                port = int(splitargs.port)
            else:
                port = 12346
            self.session = Server(ip, port, "bind")
            self.session.sendData("ping\n")
            resp = self.session.receiveData()
            if (resp == "pong"):
                print "**Connected !"
                self.prompt = "*Afe$ "
                self.connected = 1
            else:
                print "**Not Connected !** There is some Problem, Try Again !"
        except:
            pass
        
    def do_menu(self, args):
	"""
Menu Screen, to cook with different recepies available ! 
	"""
	subconsole = Menu(self.connected, self.session)
	subconsole.cmdloop()

            
    def do_update(self, args):
        """
Check if there is an updated release available from http://afe-framework.com
        """
        

if __name__ == '__main__':

    os.system('clear')
    try:
        console = Afe()
        console.cmdloop()
    except:
	    pass

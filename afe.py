#!/usr/bin/python

import argparse, shlex, sys, urllib2, os, xml.dom.minidom
from xml.dom.minidom import parseString
from internals.lib.common import *
from internals.lib.basecmd import *
from internals.lib.menu import Menu
import readline
import rlcompleter

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

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

    def do_version(self, _args):
        """
Version and author information
        """
        print "\nAFE V" + version + "\n"
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

    def chunk_read(response, chunk_size=8192, report_hook=None):
           total_size = response.info().getheader('Content-Length').strip()
           total_size = int(total_size)
           bytes_so_far = 0
           data = []
           
           while 1:
               chunk = response.read(chunk_size)
               bytes_so_far += len(chunk)
               
               if not chunk:
                   break
               
               data += chunk
               if report_hook:
                   report_hook(bytes_so_far, chunk_size, total_size)
           
           return "".join(data)

    def _chunk_report(bytes_so_far, chunk_size, total_size):
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))

        if bytes_so_far >= total_size:
            sys.stdout.write('\n')
            
    def do_update(self, args):
        """
Check if there is an updated release available from http://afe-framework.com
        """
        print "\nChecking for updates \n"
        try:
            file = urllib2.urlopen("http://afe-framework.com/manifest.xml", timeout=5)
            data = file.read()
            file.close()
            dom = parseString(data)
            #retrieve the first xml tag (<version>version number</version>):
            xmlTag = dom.getElementsByTagName('version')[0].toxml()
            #strip off the tag (<version>version no</version> ---> version no):
            retversion = xmlTag.replace('<version>','').replace('</version>','')
            if (retversion != version):
                print "\nNot the latest Version! Please update it !\n"
                dum = raw_input("Do you want to update it now? (Y/n) ")
                if (dum.lower() == 'y'):
                    xmlfromtag = dom.getElementsByTagName('from')[0].toxml()
                    durl = xmlfromtag.replace('<from>','').replace('</from>','')
                    response = urllib2.urlopen(durl)
                    print durl
                    myFile = chunk_read(response, report_hook=chunk_report)
                    myFile = open('AFE-Chunked.zip', 'w')
                    myFile.write(fil)
                    myFile.close()
            else:
                print "\nYour AFE Version " + version + " is currently the updated and latest version !\n"
        except urllib2.URLError:
            print "\nCouldn't reach http://afe-framework.com\n"
        

if __name__ == '__main__':

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        console = Afe()
        console.cmdloop()
    except:
	    pass

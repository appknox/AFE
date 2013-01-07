#!/usr/bin/python

import os, os.path, sys, argparse, shlex, signal, subprocess
from basecmd import *
from subprocess import call

class Module(object):

    def __init__(self):
        """ Arbitary constructor """
        self.path = "miscellaneous"

    def execute(self, session, arg):
        """ Arbitary function """

class Modules(BaseCmd):

    def __init__(self, conn, session):
        BaseCmd.__init__(self, session)
        self.connected = conn
        self.session = session
        if (conn == 1):
            self.prompt = "*Afe/menu/modules$ "
        else:
            self.prompt = "Afe/menu/modules$ "
        self.modules = {} # list of modules 
        self.do_reload(None)
    
    def do_back(self, _args):
        """
Return to main menu
        """
        return -1

    def _find_modules(self):
	    module_dir = os.getcwd() + "/modules"
	    dir_list = [d for d in os.listdir(module_dir) if os.path.isdir(module_dir+"/"+d)]
	    return dir_list
	
    def _list_modules(self, dir_list):
	    self.modules = dir_list
		
	
    def do_list(self, _args):
	    """
List all available modules
	    """
	    for module in sorted(self.modules):
		    print module
		
    def do_reload(self, _args):
	    """
Reloads the Plugins which are loaded in the memory
	    """
	    modulenames = self._find_modules()
	    self._list_modules(modulenames)

    def preexec_function():
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    def preexec():
	    os.setpgrp()

    def do_run(self, args):
        """
Run a custom module
usage: run [--arg <arg>] module
        """

        # Define command-line arguments using argparse
        parser = argparse.ArgumentParser(prog = 'run', add_help = False)
        parser.add_argument('module')
        parser.add_argument('--arg', '-a', metavar = '<arg>')
        try:
            splitargs = parser.parse_args(shlex.split(args))
            self.modules.index(splitargs.module)
            # Load module
        except ValueError:
	        pass
	        print splitargs.module
	        print "Error : Module not Found, please Reload"
        except:
                pass
        else:
	        print "Module found !"
	        module_dir_run = os.getcwd() + "/modules/" + splitargs.module
	        print module_dir_run
	        if os.name == 'nt':
	            path = module_dir_run+'/run.bat'
	        else:
	            path = module_dir_run+'/run.sh'
	        if os.path.isfile(path):
	            if (splitargs.arg):
	                try:
	                    call([path, splitargs.arg])
	                except:
	                    pass
	            else:
	                try:
	                    call([path])
	                except:
	                    pass
	        else:
	            print "Not found : " + path 
	        #subprocess.Popen([module_dir_run + '/run.sh'], shell = False)

        
    def complete_run(self, text, line, begidx, endidx):
        if not text:
            completions = self.modules[:]
        else:
            completions = [ f
                            for f in self.modules
                            if f.startswith(text)
                            ]
        return completions

    def do_info(self, args):
        """
Get information about a custom module
usage: info module
        """

        # Define command-line arguments using argparse
        parser = argparse.ArgumentParser(prog = 'info', add_help = False)
        parser.add_argument('module')
        try:
            splitargs = parser.parse_args(shlex.split(args))
            self.modules.index(splitargs.module)

            # Load module
        except ValueError:
	        pass
	        print splitargs.module
	        print "Error : Module not Found, please Reload"
        except:
                pass
        else:
	        module_info = os.getcwd() + "/modules/" + splitargs.module + "/" + splitargs.module + ".info"
	        try:
	            with open(module_info) as a_file:
		            print a_file.read()
                except IOError:
	            pass
	            print "No info was found for the module " + splitargs.module
                except:
                    pass

    def complete_info(self, text, line, begidx, endidx):
        if not text:
            completions = self.modules[:]
        else:
            completions = [ f
                            for f in self.modules
                            if f.startswith(text)
                            ]
        return completions
#!/usr/bin/python
#
# License: Refer to the README in the root directory
#

import os, os.path, sys
import argparse, shlex
from basecmd import BaseCmd
import subprocess
from subprocess import call
import signal

class Module(object):

    def __init__(self):
        """ Non-existent constructor """
        self.path = "miscellaneous"

    def execute(self, session, arg):
        """ Abstract execution function """

class Modules(BaseCmd):

    def __init__(self, conn, session):
        BaseCmd.__init__(self, session)
        self.connected = conn
        self.session = session
        if (conn == 1):
            self.prompt = "*Afe/menu/modules$ "
        else:
            self.prompt = "Afe/menu/modules$ "
        self.modules = {} # A dictionary of module classes
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
        # Ignore the SIGINT signal by setting the handler to the standard
        # signal handler SIG_IGN.
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

            # Split arguments using shlex - this means that parameters with spaces can be used - escape " characters inside with \
            splitargs = parser.parse_args(shlex.split(args))
            self.modules.index(splitargs.module)
            # Load module
        # FIXME: Choose specific exceptions to catch
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
	        call([module_dir_run+'/run.sh'])
	        #subprocess.Popen([module_dir_run + '/run.sh'], shell = False)

        
    def do_info(self, args):
        """
Get information about a custom module
usage: info module
        """

        # Define command-line arguments using argparse
        parser = argparse.ArgumentParser(prog = 'info', add_help = False)
        parser.add_argument('module')

        try:

            # Split arguments using shlex - this means that parameters with spaces can be used - escape " characters inside with \
            splitargs = parser.parse_args(shlex.split(args))
            self.modules.index(splitargs.module)

            # Load module
        # FIXME: Choose specific exceptions to catch
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


 
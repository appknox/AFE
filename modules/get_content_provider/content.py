#!/usr/bin/env python
#----------------------------------------------------------------------------------------------#
#Android Framework for Exploitation v-1                                                        #
# (C)opyright 2010 - XYS3C                                                                     #
#---Important----------------------------------------------------------------------------------#
#                     *** Do NOT use this for illegal or malicious use ***                     #
#              The programs are provided as is without any guarantees or warranty.             #
#---Defaults-----------------------------------------------------------------------------------#
import os
import subprocess
import glob
import shutil
import time
def extract_apk():
  for filename in os.listdir(os.getcwd()):
   if filename.endswith('.apk'):
      print "Apk file found"
      print filename
      cmd = 'apktool d '+filename
      s = subprocess.check_output(cmd.split())



def searchproviders(location):
   for dir_path, dirs, file_names in os.walk(location):
      for file_name in file_names:
         fullpath = os.path.join(dir_path, file_name)
         for line in file(fullpath):
            if "CONTENT://" in line.upper():
                print line[line.upper().find("CONTENT"):]

print "---The Android Exploitation Framework ---"
print " _______  _______  _______    _               _______     __   "
print "(  ___  )(  ____ \(  ____ \  ( )  |\     /|  (  __   )   /  \  "
print "| (   ) || (    \/| (    \/  | |  | )   ( |  | (  )  |   \/) ) "
print "| (___) || (__    | (__      (_)  | |   | |  | | /   |     | | "
print "|  ___  ||  __)   |  __)      _   ( (   ) )  | (/ /) |     | | "
print "| (   ) || (      | (        ( )   \ \_/ /   |   / | |     | | "
print "| )   ( || )      | (____/\  | |    \   /    |  (__) | _ __) (_"
print "|/     \||/       (_______/  (_)     \_/     (_______)(_)\____/"
print ""                                                               
print "Copyright Reserved : XYS3C (Visit us at http://xysec.com)"
print"----------------------------------------------------------------"
print "Files Available in the Input Folders:"
print "----LIST----"
os.chdir("../../Input")
for files in glob.glob("*.apk"):
    print "* " + files
origapp = raw_input("Enter the name of the apk you want to check the content query: ")
print "********************************"
while not os.path.isfile(origapp):
	print "APK not found, try again !"
	print "----LIST-----"
	for files in glob.glob("*.apk"):
	    print "* " + files
	origapp = raw_input("Enter the name of the apk you want to check the content query: ")
tmp = os.getcwd()+"/../temp"
shutil.copy(origapp,tmp)
os.chdir("../temp")
print "Decompiling Original App"
print "******************"
os.system('../bin/apktool d '+origapp)
print "Decompiled"
print "******************"
tmpfol = origapp.replace(' ', '')[:-4]
neworigapp = os.getcwd()+"/"+tmpfol
searchproviders(neworigapp)
dum = raw_input("Press ENTER to continue")
#print os.getcwd()
##### ALWAYS AT THE END TO CLEAR TEMP FILES########
print "Clearing Temporary files"
shutil.rmtree(tmpfol)
os.remove(origapp)
#logging.info("The modified APK is replaced/added in the Output folder !")
print "***********************************************"
dum = raw_input("Press ENTER to continue")
time.sleep(3)
